---
title: Manual Builds
description: Learn how to start manual builds on Appcircle
tags: [build, manual build]
sidebar_position: 6
---

# Starting a Manual Build

To initiate a build in Appcircle, follow these steps:

- Click on the Start Build button to begin the process.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start1.png' />

- Appcircle will prompt you to choose a configuration and workflow settings from the saved configurations. Select the appropriate settings that match your project requirements.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start2.png' />

- Once the configurations are selected, click the Start button to start the build.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start3.png' />

- Users can monitor the progress, results, and logs of the workflow steps in real-time via the interface.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start4.png' />

- After the build is complete, you have the option to download the build logs for reference or troubleshooting purposes.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE5278-start5.png' />

- Upon completion, the binary along with the artifacts will be displayed on the selected branch. These can be accessed for deployment or further use.

By following these steps, you can efficiently manage and monitor your builds in Appcircle.

For more detailed information on builds with different types of projects, please refer to the [Platform Build Guides](/build/platform-build-guides) documentation.

#### Build Statuses

- **Success**: The build has finished successfully with no failures in the workflow steps.
- **Failed**: The build has failed due to one or more workflow steps failing.
- **Warning**: The build has finished with a failed workflow step that does not affect the final outcome.
- **Timeout**: The build exceeded the timeout limit and ended prematurely.
- **Canceled**: The build was canceled by the user.