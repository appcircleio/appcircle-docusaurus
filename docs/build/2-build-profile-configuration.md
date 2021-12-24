---
title: "Build Profile Configuration Overview"
metaTitle: "Build Profile Configuration Overview"
metaDescription: "Build Profile Configuration Overview"
---
# Build Profile Configuration Overview

Configuring a build profile has some basic steps that need to be completed before starting a build.

### Project details configuration

Every build profile needs to know project details regardless of the project being iOS or Android project. Project details can be entered manually or can be fetched from your project automatically by Appcircle.

You can also enable or disable automatic builds for the current branch.

![](<../assets/image (169).png>)



### Signing configuration

Both iOS and Android applications need to be digitally signed by their developers in order to be able to be installed on real devices or submitted to app stores.

iOS certificates and Android keystores can be generated within Appcircle or pre-obtained certificates can be uploaded. iOS provisioning profiles need to be obtained from Apple Developer account and uploaded to Appcircle.

![](<../assets/image (170).png>)

###

### Distribution configuration

Distribution is a critical step when it comes to test your application on real devices. You may need multiple testers and test groups to download, install and test your application and make sure it works on different devices and operating system versions.

Distribution configuration allows you to set up which testing groups will receive your application after the build is complete. You can manually send your binary file to testers or Appcircle can do this for you.

You can select a previously created distribution profile or create a new one on this window. Use the top input box to enter a name for the new distribution profile you want to create. Press enter or click on the green + icon on the right to create the distribution profile.

Finally, check Auto Distribute if you want your build to be deployed to the Testing Distribution automatically and Auto Deployment if you want the build to be deployed to Store Submission automatically.

![](<../assets/image (171).png>)



### Environment variables configuration

You can define variables and secrets to be incorporated during the build in the Environment Variables submodule so that you don't need to store certain keys and configurations within the repository.

![](<../assets/image (172).png>)



### Workflows and Triggers

For advanced configuration, you can utilize [workflows](../workflows/why-to-use-workflows.md) and for automatic builds, you can utilize [triggers](build-manually-or-with-triggers.md#automatic-build).

These options are available at the profile level in the profile context menu.

![](<../assets/image (188).png>)

