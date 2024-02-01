---
title: What are Workflows and How to Use Workflows?
metaTitle: What are Workflows and How to Use Workflows?
metaDescription: What are Workflows and How to Use Workflows?
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# What are Workflows and How to Use Them?

<Tabs
  defaultValue="ios"
  values={[
    { label: 'iOS', value: 'ios' },
    { label: 'Android', value: 'android' },
    { label: 'React Native', value: 'reactnative' },
    { label: 'Flutter', value: 'flutter' },
  ]}
>
  <TabItem value="ios">
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/WOQedZ15z6s"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </TabItem>
  <TabItem value="android">
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/FcZv2cCnGFA"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </TabItem>
  <TabItem value="reactnative">
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/bo0fWk9cATA"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </TabItem>
  <TabItem value="flutter">
    <iframe
      width="560"
      height="315"
      src="https://www.youtube.com/embed/vKFfNvJvRDs"
      title="YouTube video player"
      frameborder="0"
      allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
      allowfullscreen
    ></iframe>
  </TabItem>
</Tabs>

A workflow is a ladder of steps taken to build your applications.

Each step has a different purpose and the workflow can be customized by modifying step parameters and inputs, running custom scripts, or re-ordering steps.

Workflows allow you to have complete control on your build process and enhance it with third-party services and features.

:::caution

Please note that modifying workflow steps may cause your builds to fail, so utmost care is recommended when editing workflows.

:::

### Setting Up Workflows

To access the workflow editor for a build profile, click the Workflows button in the context menu of the build profile, accessible from the top of the profile details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (181).png' />

The workflow list will be displayed. To view the [Workflow Steps](why-to-use-workflows.md#worfklow-steps) of a workflow, click on it from the workflow list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (197).png' />

To create a new workflow, press the "New" button at the top of the workflow list and select a template from the default workflows. Then edit the workflow name and press enter. You can also upload your workflow as a YAML file.

<Screenshot url="https://cdn.appcircle.io/docs/assets/workflow-create-edit.png" />

To rename/delete a current workflow, press the "Edit" button at the top of the workflow list and then click on the context menu that appears next to the workflow items.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (183).png' />

You can use the "Clone" option to create a new workflow based on the currently available ones. You can [select different workflows for different build scenarios](../build/build-manually-or-with-triggers.md) (e.g. separate workflows for production and development).

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (184).png' />

### Worfklow Steps

<Screenshot url="https://cdn.appcircle.io/docs/assets/workflow-ios-showcase.png" />

Appcircle will build your application with the steps defined in the workflow. Steps will be executed in order from the top to the bottom.

You can customize each step for specific configurations with your application structure. Step parameters can be modified, outputs of each step can be used in another step and step versions can be selected accordingly.

### Workflow Marketplace

Appcircle's powerful Workflow Editor has a built-in Workflow Marketplace that allows you to select and insert an unlimited amount of steps to your workflow.

You can find the full list of available workflow steps in our workflow marketplace at:;

[https://www.appcircle.io/integrations/](https://www.appcircle.io/integrations/)

You can add platform-specific workflow steps, custom scripts, and other steps into your workflow and re-order them as you like. You can also remove the steps you don't need. You can backup your current workflow by clicking the **Download YAML** button at the bottom.

<Screenshot url='https://cdn.appcircle.io/docs/assets/workflow-ios-download-yaml-showcase.png' />

To access the Workflow Marketplace, click on the **Manage Workflow** button. You will see the Workflow Marketplace on the right and your Workflow steps on the left.

You can now drag and drop steps into your workflow. Any unwanted workflow steps can be removed by clicking on the delete button on the right side of each step.

You can also reorder steps so that they will be executed in the order you specify.

<Screenshot url='https://cdn.appcircle.io/docs/assets/08-08-WF_Reorder.gif' />

###

### Editing Workflow Settings

Each workflow step has its own set of configuration options, which can be set by clicking on the step in the workflow screen.

The first three items are common for all steps and they are set individually for each step:

- **Step Execution Active:** To enable/disable the step execution without removing it from the workflow

- **Continue with the next step even if this step fails:** If a step is optional or its result should not cause a build error, you can select this option to continue the workflow if this particular step fails. In default workflows, this option is `on` for specific steps. And since this step is active, the build status will appear as "Warning" when other steps in the build are successful. Detailed explanation about this state is given in the [Build Warning Status](#build-warning-status) section.

- **Workflow Step Version:** You can select a specific version of a step with which to execute your build. If you select a version with an asterisk (\*), you will receive the minor updates to the workflow step automatically. The major versions may include added or removed input fields and manual version selection is required for major version updates.;

The items in the "Inputs" section are specific to that step. The reserved environment variables are assigned to these fields by default and the values of these variables are set in the build configuration.

<Screenshot url='https://cdn.appcircle.io/docs/assets/image (187).png' />

### Using Output Variables

Appcircle can generate output for each workflow after the workflow components are run during build. These outputs can be assigned to default variables to be used in the next steps.

If we examine the **"Android Sign"** step of an Android project, we see that it gives the output **"Signed_APK_PATH"**. After running this step in this workflow, it will show us the directory of the produced file.

<Screenshot url='https://cdn.appcircle.io/docs/assets/output-var-main.png' />

:::info
In order to use the relevant output, previously assigned variables cannot be changed.
:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/outputvar-custom-1.png' />

After the build process, we can see the equivalent of the **"AC_SIGNED_APK_PATH"** variable that we printed on the screen in the Custom Script.

<Screenshot url='https://cdn.appcircle.io/docs/assets/outputvar-custom-2.png' />

:::info
Each output variable produced can only be used within the relevant build. After the build is finished, a variable belonging to the previous build will not be available during the new build.
:::

#### Workflow Components That Can Produce Output Variable

|Platform|Component Name|Output Variables|
|----------|----------|-----------|
|Common|Activate SSH Private Key  |SSH_AUTH_SOCK |
|Common|Upload Files to Amazon S3  |AC_AWS_UPLOAD_URL |
|Android|Appdome Build-2Secure for Android  |AC_APPDOME_SECURED_APK_PATH, AC_APPDOME_SECURED_AAB_PATH, AC_APPDOME_PRIVATE_SIGN_SCRIPT_PATH, AC_APPDOME_CERTIFICATE_PATH |
|Android|Android Build|AC_APK_PATH, AC_AAB_PATH|
|Android|Android Build for UI Testing|AC_APK_PATH, AC_TEST_APK_PATH|
|Android|Increment Build and Version Number|AC_ANDROID_NEW_VERSION_CODE, AC_ANDROID_NEW_VERSION_NAME|
|Android|Android Dependency Report|AC_ANDROID_DEPENDENCY_REPORT_PATH|
|Android|Flutter Build for Android|AC_APK_PATH, AC_AAB_PATH|
|Android|Android App Post-Processor|AC_ANDROID_POST_PROCESS_OUTPUT_PATH|
|Android|Android Re-Sign|AC_SIGNED_APK_PATH, AC_SIGNED_AAB_PATH|
|Android|Android Sign|AC_SIGNED_APK_PATH, AC_SIGNED_AAB_PATH|
|Android|Test Reports|AC_TEST_REPORT_JSON_PATH|
|Android|Android Unit Tests|AC_TEST_RESULT_PATH|
|Android|AppSweep Mobile Security Testing|AC_APPSWEEP_URL|
|Common|AWS Device Farm Deploy and Run|AWS_RUN_ARN, AWS_TEST_RESULT, AWS_OUTPUT_DEVICEPOOL_ARN, AWS_OUTPUT_APPUPLOAD_ARN|
|Android|Bundle Universal Apk|AC_SIGNED_APK_PATH|
|Common|Flutter Install|PATH|
|Common|Flutter Test|AC_TEST_RESULT_PATH|
|Common|Flutter Build for Web|AC_FLUTTER_WEB_PATH|
|Common|Git Clone|AC_REPOSITORY_DIR|
|iOS|Appdome Build-2Secure for iOS|AC_APPDOME_SECURED_IPA_PATH, AC_APPDOME_PRIVATE_SIGN_SCRIPT_PATH, AC_APPDOME_CERTIFICATE_PATH|
|iOS|Xcodebuild Build for Testing|AC_TEST_APP_PATH, AC_UITESTS_RUNNER_PATH, AC_XCTEST_PATH, AC_UITESTS_RUNNER_IPA_PATH, AC_XCTEST_ZIP_PATH, AC_TEST_IPA_PATH|
|iOS|Xcodebuild for Devices|AC_ARCHIVE_PATH, AC_ARCHIVE_METADATA_PATH, AC_EXPORT_DIR|
|iOS|Xcodebuild for iOS Simulator|AC_SIMULATOR_APP_PATH|
|iOS|Increment Build and Version Number|AC_IOS_NEW_BUILD_NUMBER|
|iOS|Install Certificates & Profiles|AC_KEYCHAIN_PATH, AC_KEYCHAIN_PASSWORD|
|iOS|Xcodebuild for Unit and UI Tests|AC_TEST_RESULT_PATH|
|iOS|Test Reports|AC_TEST_REPORT_JSON_PATH|
|Android|Android Metadata|AC_METADATA_OUTPUT_PATH|
|Common|Repeato Test Runner|AC_REPEATO_REPORT, AC_REPEATO_JUNIT_REPORT, AC_TEST_RESULT_PATH|
|iOS|Slather|AC_SLATHER_OUTPUT_PATH|
|iOS|Swiftlint|AC_LINT_OUTPUT_PATH|
|Common|Testinium|AC_TESTINIUM_RESULT_FAILURE_SUMMARY, AC_TESTINIUM_RESULT_ERROR_SUMMARY, AC_TESTINIUM_RESULT_SUCCESS_SUMMARY|
|iOS|Xcode Select|XCODE_DEVELOPER_DIR_PATH|
|Common|Snyk Scan Security|AC_SNYK_REPORT, AC_SNYK_MONITOR_EXPLORE_LINK|

#### Build Warning Status

When we start a build, if we have activated the "Continue with the next step even if this step fails" setting for a component we use in the workflow and this step fails during the build, Appcircle will show the build status as "Warning" if the build is completed successfully for other steps.

In order to simulate the warning state and see its results on the pipeline, we can basically write a script that will fail in Custom Script.

<Screenshot url='https://cdn.appcircle.io/docs/assets/status-warning-1.png' />

"Continue with the next step even if this step fails" must be `on` in this case.

<Screenshot url='https://cdn.appcircle.io/docs/assets/status-warning-2.png' />

We are starting a build, and we see that it fails in the pipeline.

<Screenshot url='https://cdn.appcircle.io/docs/assets/status-warning-3.png' />

And the build status will now appear as "Warning".

<Screenshot url='https://cdn.appcircle.io/docs/assets/status-warning-4.png' />
