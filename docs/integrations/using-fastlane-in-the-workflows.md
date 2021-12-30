---
title: Using Fastlane in the Workflows
metaTitle: Using Fastlane in the Workflows
metaDescription: Using Fastlane in the Workflows
sidebar_position: 2
---

# Using Fastlane in the Workflows

Appcircle supports \_fastlane \_for build automation as a supplementary feature to Appcircle's own build automation.

With Appcircle, you can automate your build and signing processes with the flexible workflow structure and you can also use \_fastlane \_as a workflow step within the build workflows.

To use fastlane, Appcircle expects the presence of a fastfile in your repository.

### Adding \_fastlane \_to the Appcircle Build Workflow as a Step

![](https://cdn.appcircle.io/docs/assets/Fastlane-Appcircle.png)

1. To utilize _fastlane \_in your builds, open the [workflow editor](../workflows/why-to-use-workflows.md) and add the “**fastlane**” step after the "**Git Clone**" step. If you want to run a specific \_fastlane \_command, you can add a "**Custom Script**" step anywhere after the \_fastlane_ step.
2. Once added, click on the \_fastlane \_step to configure it. Fastlane is easy to use with Appcircle just with two options.
3. The "**Fastlane Directory**" option is used to specify the fastfile path . If you keep your fastfile in its default location, it is automatically used without the need to change this field.
4. With the "**Fastlane Lane**" option, you can specify which lane to use.
5. Once everything is set up, press **Save** to save your step configuration. Then you can configure and run your build just like any other app.

![](<https://cdn.appcircle.io/docs/assets/image (68).png>)

Appcircle also supports building and signing the app independently with the "Build" and "Sign" steps in the workflow. These steps can be used in parallel with _fastlane_.

### Running the Build Workflow

To run the build workflow that includes the \_fastlane \_step, you can start a [manual build or trigger an automatic build](../build/build-manually-or-with-triggers.md) just like a standard build.

The full output of the \_fastlane \_execution can be viewed in the build log in real-time or after the build.

### Deploying the Build Output

You can use \_fastlane \_to deploy the built apps to the supported third-party services supported or you can use the [Appcircle Distribute module](../distribute/create-or-select-a-distribution-profile.md) to share the app with the testers or send it to the public app stores.
