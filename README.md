# rhc
![rhc](https://github.com/linux-system-roles/template/workflows/tox/badge.svg)

An ansible role which registers/connects RHEL systems to Red Hat.

## Requirements

subscription-manager and insights-client. Both are available from the standard
RHEL repositories, and subscription-manager is installed by default.

## Role Variables

None at the moment.

## Dependencies

None.

## Example Playbook

Simple Registration to Red Hat including Insights:

```yaml
- hosts: all
  roles:
    - linux-system-roles.rhc
```

## License

MIT
