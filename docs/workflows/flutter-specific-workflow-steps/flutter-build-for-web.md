---
title: ​Flutter Build for Web
metaTitle: ​Flutter Build for Web
metaDescription: ​Flutter Build for Web
sidebar_position: 5
---

import Screenshot from '@site/src/components/Screenshot';

# ​Flutter Build for Web

This component allows you to build your web applications. Please note that it requires the preceding [**Flutter Install**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps#flutter-install) and [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) steps to run.

### Prerequisites
| Prerequisite Workflow Step                      | Description                                     |
|-------------------------------------------------|-------------------------------------------------|
| [**Git Clone**](https://docs.appcircle.io/workflows/common-workflow-steps/#git-clone) | This step will clone your project through the connected git provider and create the `$AC_REPOSITORY_DIR` variable. |
| [**Flutter Install**](https://docs.appcircle.io/workflows/flutter-specific-workflow-steps#flutter-install) | This step will install the [Flutter SDK version](https://flutter-ko.dev/development/tools/sdk/releases). If the version is not specified, it will install the latest **stable** version. |

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2855-flutterWebOrder.png' />

:::warning
This step is particularly dependent on the **Flutter Install** step. If the Flutter SDK is not installed, the step will give an error that the required command was not found.
:::

### Input Variables

You can find all the parameters required for this step in the table below, with their descriptions in detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE2855-flutterWebInput.png' />

| Variable Name                 	       | Description                         | Status 			|
|-------------------------------|------------------------------------------------|------------------|
| `$AC_FLUTTER_PROJECT_DIR`     | This parameter is used as the repository path. This path is created immediately after the **Git Clone** step. If the **Git Clone** step is not used, this path cannot be found. | Required|


### Output Variables

| Variable Name                 	       | Description                         |
|-------------------------------|------------------------------------------------|
| `$AC_FLUTTER_WEB_PATH`        | This path is created after the **Flutter Build for Web** step is completed and stores the generated Web application. | 


To access the source code of this component, please use the following link:

https://github.com/appcircleio/appcircle-flutter-web-build-component