---
title: Publishing Release Notes
metaTitle: Publishing Release Notes
metaDescription: Publishing Release Notes
sidebar_position: 7
---

# Publishing Release Notes

You can use [Release Notes Component](https://github.com/appcircleio/appcircle-release-notes-component/) to create release notes during your workflow. You can enrich the contents of your release notes with environment variables or with Ruby snippets. If you want to add your own release notes as a file, you can also give the path to the file. This component creates **release-notes.txt** with given options and copies to *$AC_OUTPUT_DIR* path. This release notes will be used for the following places:

- Distribution Portal
- Enterprise Store
- Google Play

Appcircle currently doesn't publish release notes to TestFlight. Since TestFlight doesn't allow uploding change log with the binary. You can only upload *what to test part* **AFTER** the binary is processed which may take hours.

Release Notes component should be in your workflow to create rich release notes. It is suggested that it should be just before the Export Build Artifacts step so that you can have access to the all build artifacts such as git commit message, test results or build logs.

![](<https://cdn.appcircle.io/docs/assets/report-component.png>)

## Example Release Notes

Release notes component allows putting Environment Variables or Ruby snippets inside your release notes. Release notes template is written in ERB. Please check [Ruby documentation](https://docs.ruby-lang.org/en/2.7.0/ERB.html) for the usage of ERB. We will list couple of templates to get you started.

## Default template

```ruby
Branch: $AC_GIT_BRANCH
Commit Hash:  <%= ENV['AC_GIT_COMMIT'][0..6] %>
Commit Message: $AC_COMMIT_MESSAGE
```

Above template will print something like below

```
Branch: main
Commit Hash: 1234567
Commit Message: My commit messsage
```


## Adding git log of last 5 commits

```ruby
Branch: $AC_GIT_BRANCH
Commit Hash:  <%= ENV['AC_GIT_COMMIT'][0..6] %>
Commit Message: $AC_COMMIT_MESSAGE
Git Log:
<%= `git --git-dir=$AC_REPOSITORY_DIR/.git log -n 5 --pretty=format:'- %an: %s'` %>
```

Above template will print something like below

```
Branch: main
Commit Hash: 1234567
Commit Message: My commit messsage
Git Log:
- John: Enable code coverage
- Jane: Add Info.plist file
- Tom: Add certificates
- John: Removed launch tests
- Jane: Initial commit
```

Please check [Release Notes Component](https://github.com/appcircleio/appcircle-release-notes-component/) documentation for more information.