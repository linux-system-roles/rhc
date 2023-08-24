# Candlepin-based tests

Testing the registration to Red Hat requires a Candlepin server.
The setup of the integration tests deploys one by default directly from
upstream sources.

It is possible to use an external Candlepin server instead; to do this,
a configuration file must be created with details of that server:

```yaml
lsr_rhc_test_data:
  candlepin_host: candlepin.hostname
  candlepin_port: port
  candlepin_prefix: /candlepin
  candlepin_insecure: 1
  reg_username: "username"
  reg_password: "password"
  reg_activation_keys:
    - "key1"
    - "key2"
  reg_organization: "organization"
  baseurl: "https://base-url"
  repositories:
    - {name: "repo1", state: enabled}
    - {name: "repo2", state: disabled}
  release: "some-release"
  proxy_noauth_hostname: proxy-without-auth.hostname
  proxy_noauth_scheme: http
  proxy_noauth_port: port
  proxy_auth_hostname: proxy-requiring-auth.hostname
  proxy_auth_scheme: http
  proxy_auth_port: port
  proxy_auth_username: "proxy-username"
  proxy_auth_password: "proxy-password"
  proxy_nonworking_hostname: must-not-exist.hostname
  proxy_nonworking_port: invalid-port
  proxy_nonworking_username: "wrong-username"
  proxy_nonworking_password: "wrong-password"
  envs_register:
    - "Environment 1"
  env_nonworking: "not-a-valid-environment"
  insights: false
```

- `candlepin_host` & `candlepin_port` are the hostname & the port of Candlepin
- `candlepin_prefix` is the path under which Candlepin listens to
- `candlepin_insecure` specifies whether do not validate the Candlepin SSL
  certificate (needed usually in self-deployments)
- `reg_username`, `reg_password`, `reg_activation_keys` & `reg_organization`
  are the credentials of the user to use in the vast majority of the
  registration tests; `reg_organization` can be specified as `null` in case
  `reg_username` belongs to only one organization, and only for tests in which
  activation keys are not used
- `baseurl` is the base URL for receiving content
- `repositories` is a list of repositories to use in tests for content,
  and to assert for enablement/disablement; it has the same format of the
  `rhc_repositories` parameter of the `rhc` role
- `release` is a release to set for the system; it has the same format of the
  `rhc_release` parameter of the `rhc` role
- the various `proxy_*` variables represent proxy-related bits:
  - `proxy_noauth_hostname` & `proxy_noauth_port` are the hostname & the port
     of a proxy server that does not require authentication
  - `proxy_noauth_scheme` is the scheme for the proxy server that does not
     require authentication; it can be not specified if the proxy type is "http"
  - `proxy_auth_hostname`, `proxy_auth_port`, `proxy_auth_username` &
     `proxy_auth_password` are the hostname & the port of a proxy server that
      requires authentication, together with the credentials for it
  - `proxy_auth_scheme` is the scheme for the proxy server that requires
     authentication; it can be not specified if the proxy type is "http"
  - `proxy_nonworking_hostname`, `proxy_nonworking_port`,
     `proxy_nonworking_username` & `proxy_nonworking_password` are wrong details
     of proxy server configuration bits
- `envs_register` is a list of working environments to use when registering a
  system, and there must be at least one; if environments are not supported or
  enabled in the Candlepin instance, this needs to be set to `null`
- `env_nonworking` is an environment that does not exist
- `insights` specifies whether Insights works with the specified
  `candlepin_host`

To use this custom configuration, set the `LSR_RHC_TEST_DATA` environment
variable to the full path of that file.
