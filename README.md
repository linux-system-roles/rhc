# rhc

![rhc](https://github.com/linux-system-roles/template/workflows/tox/badge.svg)

An ansible role which connects RHEL systems to Red Hat.

## Requirements

The role requires subscription-manager, which is available from the standard
RHEL repositories, and usually installed by default on RHEL. On other
distributions it will be installed if not already.

The role requires also insights-client, which is available from the standard
RHEL repositories, in case the Insights support is enabled (and it is by
default).

In addition, the role requires rhc, which is available from the standard RHEL
repositories, in case the Insights remediation is enabled (and it is by
default).

### Collection requirements

The role requires modules from `community.general`.  If you are using
`ansible-core`, you must install the `community.general` collection.  Use the
file `meta/collection-requirements.yml` to install it:

```bash
ansible-galaxy collection install -vv -r meta/collection-requirements.yml
```

If you are using Ansible Engine 2.9, or are using an Ansible bundle which
includes these collections/modules, you should have to do nothing.

## Role Variables

```yaml
    rhc_state: present
```

Whether the system is connected to Red Hat; valid values are `present`
(the default, to ensure connection), `absent`, and `reconnect`.

When using `reconnect`, the system will be first disconnected in case
it was already connected; because of this, the role will always report a
"changed" status.

```yaml
    rhc_organization: "your-organization"
```

The organization of the user. This *must* be specified when connecting if
either:

* the user belongs to more than one organization
* using activation keys (see `rhc_auth` below)

```yaml
    rhc_auth: {}
```

The authentication method used to connect a system. This must be specified
in case a system may need to connect (e.g. in case it was not before).
There are few possible authentication methods; only one can be specified at
a time.

**NB**: the variables used for authentication are considered secrets, and thus
they ought to be secured. We recommend the usage of Ansible Vault as source
for them. The references below only describe which keys exists and what they
are for.

For authenticating using username & password, specify the `login` dictionary
using the following mandatory keys:

```yaml
rhc_auth:
  login:
    username: "your-username"
    password: "your-password"
```

using `rhc_organization` if needed.

For authenticating using activation keys, specify the `activation_keys`
dictionary using the following mandatory keys, together with `rhc_organization`:

```yaml
rhc_auth:
  activation_keys:
    keys: ["key-1", ...]
rhc_organization: "your-organization"
```

```yaml
    rhc_server: {}
```

The details of the registration server to connect to; it can contain the
following optional keys:

```yaml
rhc_server:
  hostname: "hostname"
  port: 443
  prefix: "server-prefix"
  insecure: false
```

* `hostname` is the hostname of the server
* `port` is the port to which connect to on the server
* `prefix` is the prefix (starting with `/`) for the API calls to the server
* `insecure` specifies whether to disable the validation of the SSL certificate
  of the server

```yaml
    rhc_baseurl: ""
```

The base URL for receiving content from the subscription server.

```yaml
    rhc_repositories: []
```

A list of repositories to enable or disable in the system. Each item is a
dictionary containing two keys:

* `name` is the name of a repository; this keys is mandatory
* `state` is the state of that repository in the system, and it can be `enabled`
  or `disabled`; this key is optional, and `enabled` if not specified

```yaml
rhc_repositories:
  - {name: "repository-1", state: enabled}
  - {name: "repository-2", state: disabled}
```

```yaml
    rhc_release: "release"
```

A release to set for the system. Typically used for locking a RHEL system to
a certain minor version of RHEL.

Use `{"state":"absent"}` (and not `""`) to actually unset the release set for
the system.

```yaml
    rhc_insights:
      state: present
```

Whether the system is connected to Insights; valid values are `present`
(the default, to ensure connection), and `absent`.

```yaml
    rhc_insights:
      autoupdate: true
```

Whether the system automatically updates the dynamic configuration. It is
enabled by default.

```yaml
    rhc_insights:
      remediation: present
```

Whether the system is configured to run the Insights remediation; valid values
are `present` (the default, to ensure remediation), and `absent`.

Please note that the Insights remediation is supported only on RHEL 8.4 or
greater, as the needed packages are available only starting from that version;
on older versions, this parameter has no effect.

```yaml
    rhc_insights:
      tags: {}
```

A dictionary of tags that is added to the system record in Host Based Inventory
(HBI); typically used for the grouping and tagging of systems, and to search
for systems in the inventory.

Possible values of this variable:

* `null` or an empty value (e.g.: `{}`): the tags file content is not changed
* `{state: absent}`: all the tags are removed (by removing the tags file)
* any other value: the file is created with the specified tags

Since the tags are arbitrary values for the tagging of systems, there is no
fixed format. In the specified dictionary, the keys are strings, and the type
of the values can be any data type (strings, numbers, lists, dictionaries,
etc).

Example of the tags configured in the `insights-client`
[documentation](https://access.redhat.com/documentation/en-us/red_hat_insights/2023/html/client_configuration_guide_for_red_hat_insights/con-insights-client-tagging-overview_insights-cg-adding-tags):

```yaml
rhc_insights:
  tags:
    group: _group-name-value_
    location: _location-name-value_
    description:
      - RHEL8
      - SAP
    key 4: value
```

```yaml
    rhc_proxy: {}
```

The details of the proxy server to use for connecting:

```yaml
rhc_proxy:
  hostname: "proxy-hostname"
  scheme: http
  port: 4321
  username: "proxy-hostname"
  password: "proxy-password"
```

* `hostname` is the hostname of the proxy server
* `scheme` is the scheme to use for the proxy server, usually "http" or "https",
  defaulting to "http"
* `port` is the port to which connect to on the proxy server
* `username` is the username to use for authenticating on the proxy server;
  it can be not specified if the proxy server does not require authentication
* `password` is the password to use for authenticating on the proxy server;
  it can be not specified if the proxy server does not require authentication

Use `{"state":"absent"}` to reset all the proxy configurations to empty
(effectively disabling the proxy server).

**NB**: the variables used for the authentication on the proxy server are
considered secrets, and thus they ought to be secured. We recommend the usage
of Ansible Vault as source for them.

```yaml
    rhc_environments: []
```

The list of environments to which register to when connecting the system.

*NB*:

* this only works when the system is being connected from an unconnected state
  -- it cannot change the environments of already connected systems
* this requires the environments to be enabled on the registration server;
  in Red Hat Satellite or Katello, this feature is called "Content Views"

## Example Playbooks

Ensure the connection to Red Hat including Insights, authenticating using
username & password:

```yaml
- name: Register systems
  hosts: all
  vars:
    rhc_auth:
      login:
        username: "your-username"
        password: !vault |
          $ANSIBLE_VAULT;1.2;AES256;dev
          ....
  roles:
    - linux-system-roles.rhc
```

Ensure that certain RHEL 9 repositories are enabled, and another one is not:

```yaml
- name: Ensure RHEL 9 repositories are enabled
  hosts: all
  vars:
    rhc_repositories:
      - {name: "rhel-9-for-x86_64-baseos-rpms", state: enabled}
      - {name: "rhel-9-for-x86_64-appstream-rpms", state: enabled}
      - {name: "codeready-builder-for-rhel-9-x86_64-rpms", state: disabled}
  roles:
    - linux-system-roles.rhc
```

Ensure that a RHEL 8 system is locked on RHEL 8.6:

```yaml
- name: Ensure systems are locked at RHEL 8.6
  hosts: all
  vars:
    rhc_release: 8.6
  roles:
    - linux-system-roles.rhc
```

Ensure that a system is connected to Insights, without optional features such
as automatic updates and remediation:

```yaml
- name: Ensure systems are connected to Insights
  hosts: all
  vars:
    rhc_insights:
      autoupdate: false
      remediation: absent
  roles:
    - linux-system-roles.rhc
```

## License

MIT
