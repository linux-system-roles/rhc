Changelog
=========

[1.6.11] - 2025-04-28
--------------------

### Other Changes

- ci: In test plans, prefix all relate variables with SR_ (#222)
- ci: Fix bug with ARTIFACTS_URL after prefixing with SR_ (#223)
- tests: Cleanup candlepin container (#224)
- tests: update location of Candlepin container (#225)
- ci: several changes related to new qemu test, ansible-lint, python versions, ubuntu versions (#226)
- ci: use tox-lsr 3.6.0; improve qemu test logging (#228)
- ci: skip storage scsi, nvme tests in github qemu ci (#229)

[1.6.10] - 2025-02-26
--------------------

### Other Changes

- ci: ansible-plugin-scan is disabled for now (#212)
- ci: bump ansible-lint to v25; provide collection requirements for ansible-lint (#215)
- ci: Check spelling with codespell (#217)
- ci: Revert .pandoc_template because it contains a typo in Licence (#218)
- ci: Add test plan that runs CI tests and customize it for each role (#219)
- tests: adjust UUID checks to newer versions of insights-core (#220)

[1.6.9] - 2025-01-27
--------------------

### Bug Fixes

- fix: use the right systemd service for remediations in EL 10+ (#209)

### Other Changes

- tests: stop adding pools to the activation key (#210)

[1.6.8] - 2025-01-09
--------------------

### Other Changes

- ci: Use Fedora 41, drop Fedora 39 (#206)
- ci: Use Fedora 41, drop Fedora 39 - part two (#207)

[1.6.7] - 2024-10-30
--------------------

### Other Changes

- ci: Add tags to TF workflow, allow more [citest bad] formats (#198)
- ci: ansible-test action now requires ansible-core version (#200)
- ci: add YAML header to github action workflow files (#201)
- refactor: Use vars/RedHat_N.yml symlink for CentOS, Rocky, Alma wherever possible (#203)
- tests: simplify distro check in tests_environments.yml (#204)

[1.6.6] - 2024-08-09
--------------------

### Bug Fixes

- fix: drop usage of "auto_attach" of the "redhat_subscription" module (#189)

### Other Changes

- ci: Add tft plan and workflow (#187)
- ci: Update fmf plan to add a separate job to prepare managed nodes (#190)
- tests: factorize & fix URL for candlepin owner (#191)
- ci: Bump sclorg/testing-farm-as-github-action from 2 to 3 (#192)
- ci: Add workflow for ci_test bad, use remote fmf plan (#193)
- ci: Fix missing slash in ARTIFACTS_URL (#194)
- tests: switch to an SCA account for Candlepin (#195)
- tests: run podman directly instead of using containers.podman (#196)

[1.6.5] - 2024-07-02
--------------------

### Bug Fixes

- fix: add support for EL10 (#184)

### Other Changes

- ci: ansible-lint action now requires absolute directory (#183)

[1.6.4] - 2024-06-11
--------------------

### Other Changes

- ci: use tox-lsr 3.3.0 which uses ansible-test 2.17 (#178)
- ci: tox-lsr 3.4.0 - fix py27 tests; move other checks to py310 (#180)
- ci: Add supported_ansible_also to .ansible-lint (#181)

[1.6.3] - 2024-04-04
--------------------

### Other Changes

- chore: I added PR description to changelog by mistake (#174)

[1.6.2] - 2024-04-04
--------------------

### Other Changes

- chore: Fix indentation in CHANGELOG (#172)

[1.6.1] - 2024-04-02
--------------------

### Bug Fixes

- fix: Ignore ansible_host: "" (#169)

### Other Changes

- ci: Bump ansible/ansible-lint from 6 to 24 (#168)
- ci: Bump mathieudutour/github-tag-action from 6.1 to 6.2 (#170)

[1.6.0] - 2024-02-21
--------------------

### New Features

- feat: Add a display name parameter (#166)

[1.5.1] - 2024-02-09
--------------------

### Other Changes

- Revert "tests: temporarily pin Candlepin to 4.4.2" (#161)
- ci: fix python unit test - copy pytest config to tests/unit (#162)
- tests: rename tests_insights_ansible_host.yaml (#164)

[1.5.0] - 2024-01-23
--------------------

### New Features

- feat: add ansible host parameter to insights configuration (#155)

### Other Changes

- tests: temporarily pin Candlepin to 4.4.2 (#159)

[1.4.1] - 2024-01-16
--------------------

### Other Changes

- ci: support ansible-lint and ansible-test 2.16 (#156)
- ci: Use supported ansible-lint action; run ansible-lint against the collection (#157)

[1.4.0] - 2023-12-12
--------------------

### New Features

- feat: support again EL7 (#151)

### Other Changes

- tests: force recreating Candlepin container (#152)
- tests: manually stop the Candlepin container (#153)

[1.3.0] - 2023-12-04
--------------------

### New Features

- feat: support for ostree systems (#145)

### Other Changes

- build(deps): Bump actions/checkout from 3 to 4 (#133)
- ci: ensure dependabot git commit message conforms to commitlint (#136)
- ci: tox-lsr version 3.1.1 (#141)
- tests: use the containers.podman collection (#144)
- tests: start candlepin container as privileged on EL 7 (#146)
- chore: set a bash shebang recognized by ansible-test (#148)
- ci: Bump actions/github-script from 6 to 7 (#149)

[1.2.5] - 2023-09-07
--------------------

### Other Changes

- ci: Add markdownlint, test_html_build, and build_docs workflows (#129)

  - markdownlint runs against README.md to avoid any issues with
    converting it to HTML
  - test_converting_readme converts README.md > HTML and uploads this test
    artifact to ensure that conversion works fine
  - build_docs converts README.md > HTML and pushes the result to the
    docs branch to publish dosc to GitHub pages site.
  - Fix markdown issues in README.md
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

- docs: Make badges consistent, run markdownlint on all .md files (#130)

  - Consistently generate badges for GH workflows in README RHELPLAN-146921
  - Run markdownlint on all .md files
  - Add custom-woke-action if not used already
  - Rename woke action to Woke for a pretty badge
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

- ci: Remove badges from README.md prior to converting to HTML (#131)

  - Remove thematic break after badges
  - Remove badges from README.md prior to converting to HTML
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

[1.2.5] - 2023-09-07
--------------------

### Other Changes

- ci: Add markdownlint, test_html_build, and build_docs workflows (#129)

  - markdownlint runs against README.md to avoid any issues with
    converting it to HTML
  - test_converting_readme converts README.md > HTML and uploads this test
    artifact to ensure that conversion works fine
  - build_docs converts README.md > HTML and pushes the result to the
    docs branch to publish dosc to GitHub pages site.
  - Fix markdown issues in README.md
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

- docs: Make badges consistent, run markdownlint on all .md files (#130)

  - Consistently generate badges for GH workflows in README RHELPLAN-146921
  - Run markdownlint on all .md files
  - Add custom-woke-action if not used already
  - Rename woke action to Woke for a pretty badge
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

- ci: Remove badges from README.md prior to converting to HTML (#131)

  - Remove thematic break after badges
  - Remove badges from README.md prior to converting to HTML
  
  Signed-off-by: Sergei Petrosian <spetrosi@redhat.com>

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
