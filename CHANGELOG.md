Changelog
=========

[1.2.4] - 2023-07-31
--------------------

### Bug Fixes

- fix: use rhc_organization and rhc_baseurl only when specified (#127)

[1.2.3] - 2023-07-19
--------------------

### Bug Fixes

- fix: enable remediation only on RHEL >= 8.4 (#116)
- fix: facts being gathered unnecessarily (#124)

### Other Changes

- tests: tests_environments: fix distro version check (#117)
- ci: Add pull request template and run commitlint on PR title only (#121)
- ci: Rename commitlint to PR title Lint, echo PR titles from env var (#122)
- ci: ansible-lint - ignore var-naming[no-role-prefix] (#123)

[1.2.2] - 2023-06-08
--------------------

### Other Changes

- perf: manually query for subscription status only when changing release (#114)

  After commit bdfeb32fa3ff665e8e0fa8bfab63393786412b0f (i.e. the drop of the fake credentials), the registration status before invoking the `redhat_subscription` module is needed only because of the release setting. This is because the `redhat_subscription` module only sets a release when registering; on an already registered system, the `rshm_release` module is needed.
  
  Hence, limit the query of the system registration status only in case there is a release change (i.e. `rhc_release` is different than null).
  
  Followup of commit bdfeb32fa3ff665e8e0fa8bfab63393786412b0f

- tests: ensure to always unregister (#115)

  Wrap a couple of Insights tests into blocks, so it is possible to always ensure the unregistration at the end of the tests, even in case of failure.
  
  There should be no behaviour change w.r.t. what the tests themselves check.


[1.2.1] - 2023-06-06
--------------------

### Other Changes

- refactor: drop fake credential workaround (#111)

[1.2.0] - 2023-06-06
--------------------

### New Features

- feat: implement rhc_proxy.scheme (#106)

### Bug Fixes

- fix: correctly set release using new behavior of rhsm_release (#108)

### Other Changes

- refactor: pass rhc_baseurl directly to redhat_subscription (#105)
- test: add check for proxy scheme (#107)
- chore(meta): temporarily stop supporting Fedora (#109)
- build: require community.general 6.6.0 (#110)

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
