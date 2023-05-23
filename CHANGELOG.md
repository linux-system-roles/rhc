Changelog
=========

[1.1.3] - 2023-05-23
--------------------

### Bug Fixes

- fix: fix filename with insights-client tags

### Other Changes

- Minimize Ansible facts needed
- ci: Add commitlint GitHub action to ensure conventional commits with feedback
- docs: Consistent contributing.md for all roles - allow role specific contributing.md section
- docs: remove unused Dependencies section in README
- ci: update tox-lsr to version 3.0.0

[1.1.2] - 2023-04-14
--------------------

### Bug Fixes

- Do not pass fake creds when activation keys are specified (#92)

### Other Changes

- Fix minor ansible-lint issues (#88)

[1.1.1] - 2023-03-16
--------------------

### Bug Fixes

- README: improve the role documentation a bit (#76)
- workaround insights-client issue with /usr/bin/python

### Other Changes

- tests: refactor Candlepin setup (#75)
- tests: do not deploy Candlepin in tests_release (#78)
- add and remove selinux ports for proxy access
- tests: refactor Insights setup (#80)

[1.1.0] - 2023-02-15
--------------------

### New Features

- Implement "rhc_state: reconnect" (#43)
- Implement "rhc_insights.remediation"
- Implement rhc_environments (#48)
- rhc_repository: setting default state of repo to enabled (#65)
- Implemented "rhc_insights.tags" parameter
- meta: stop supporting EL7 (#66)
- Added "rhc_insights.autoupdate" parameter (#67)

### Bug Fixes

- Fix rhc_auth.activation_keys.keys (#54)
- Fix rhc_insights.remediation when absent (#70)

### Other Changes

- Add check for non-inclusive language
- ansible-lint 6.x fixes

[1.0.0] - 2022-12-15
--------------------

### New Features

- initial version

### Bug Fixes

- none

### Other Changes

- none
