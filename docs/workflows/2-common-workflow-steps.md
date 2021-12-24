---
title: "Common Workflow Steps"
metaTitle: "Common Workflow Steps"
metaDescription: "Common Workflow Steps"
---
# Common Workflow Steps

The steps listed below are common across all build profiles regardless of the target OS and platform.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## Component Downloader

This is a built-in step present within the build agent and executed before every step in the workflow. It is responsible for downloading the sources of the next step/component in the workflow.

## Activate SSH Key

This step sets up your SSH key in the build machine if you used one to connect your repository. This allows the build machine to connect to your private repository using your SSH key.

[https://github.com/appcircleio/appcircle-activate-ssh-key-component](https://github.com/appcircleio/appcircle-activate-ssh-key-component)

## Custom Scripts

You can use custom scripts for additional functionalities in your builds. Appcircle will run the commands in your custom scripts and perform the specified actions. These scripts will be run on the build agent and you can use any functionality of the virtual machine as you need.

[https://github.com/appcircleio/appcircle-custom-script-component/](https://github.com/appcircleio/appcircle-custom-script-component/)

## Git Clone

Clones the Git repository to the build agent with the given arguments.

[https://github.com/appcircleio/appcircle-git-clone-component](https://github.com/appcircleio/appcircle-git-clone-component)

## Export Build Artifacts

Exports the specified build artifacts from the build agent to the Appcircle dashboard. The exported files will be available for download from the artifacts section of the completed build.

[https://github.com/appcircleio/appcircle-export-build-artifacts](https://github.com/appcircleio/appcircle-export-build-artifacts)
