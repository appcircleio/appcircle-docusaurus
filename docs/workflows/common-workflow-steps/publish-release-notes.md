---
title: Publish Release Notes
description: Learn to publish release notes for your app versions. Communicate updates and changes effectively with Appcircle.
tags: [build, test, release, notes, workflow, step]
sidebar_position: 7
---

import Screenshot from '@site/src/components/Screenshot';

# Publish Release Notes

You can use the **Publish Release Notes** step to generate release notes during your workflow. These release notes can be enriched with environment variables or Ruby snippets, and you also have the option to include your own release notes file by specifying its path. This component generates a `release-notes.txt` file with the provided options and copies it to the `$AC_OUTPUT_DIR` path. The generated release notes will be utilized in the following areas:

- Distribution Portals (such as [Appcircle Testing Distribution](/distribute) or [Firebase App Distribution](https://github.com/appcircleio/appcircle-firebase-distribution-component) step)
- [Enterprise App Store](/enterprise-appstore)
- Publishing (to [Google Play](/publish-integrations/android-publish-integrations/send-to-googleplay) or Approval Email steps)

:::caution

Appcircle currently does not publish release notes to TestFlight, as TestFlight does not allow uploading a changelog with the binary. You can only upload the "what to test" section **AFTER** the binary is processed, which may take several hours.

:::

### Prerequisites

There are no prerequisites required before using the **Publish Release Notes** step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/workflow-publish-release-notes-edit.png' />

:::warning

To create rich release notes, the Release Notes component should be included in your workflow. It is recommended to place it just before the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step so that you can have access to all build artifacts, such as git commit messages, test results, or build logs.

:::

### Input Variables

You can find all the parameters required for this step in the table below, along with detailed descriptions.

<Screenshot url='https://cdn.appcircle.io/docs/assets/workflow-publish-release-notes-input.png' />

| Variable Name                | Description                                                                                                                                                                                                                   | Status   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| `$AC_RELEASE_NOTES_PATH`     | Specifies the path of the release notes. You can override the `AC_RELEASE_NOTES_PATH` environment variable or provide its full path, e.g., `./release-notes.txt`. If the path is empty, release notes will be auto-generated. | Optional |
| `$AC_RELEASE_NOTES_TEMPLATE` | This variable is an ERB template. You can enrich the contents of your release notes with environment variables or Ruby snippets.                                                                                              | Optional |

### Output Variables

| Variable Name | Description                                                                                                                                                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ` `           | This step creates the `release-notes.txt` file. It does not keep this file in a variable, but you can access this file via [**Download Artifacts**](/workflows/common-workflow-steps/export-build-artifacts#download-exported-artifacts). |

<Screenshot url='https://cdn.appcircle.io/docs/assets/workflow-publish-release-notes-output.png' />

:::warning

Don't forget to use the [**Export Build Artifacts**](/workflows/common-workflow-steps/export-build-artifacts) step to access the release notes output and distribute it after the build.

:::

---

To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-flutter-web-build-component
