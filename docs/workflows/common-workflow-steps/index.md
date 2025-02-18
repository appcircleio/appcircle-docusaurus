---
title: Common Workflow Steps
description: Common workflow steps in Appcircle
tags: [workflow, steps, common]
---

import Screenshot from '@site/src/components/Screenshot';

# Common Workflow Steps

The steps listed below are common across all build profiles regardless of the target OS and platform.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## [Activate SSH Key](/workflows/common-workflow-steps/active-ssh-private-key)

This step sets up your SSH key in the build machine if you used one to connect your repository. This allows the build machine to connect to your private repository using your SSH key.

## [Add a Badge to Your App Icon](/workflows/common-workflow-steps/add-badge-app-icon)

With Appcircle's **Add Badge to Your App Icon** component, you can add badges and version information to your app icon, which you can also customize. This helps testers easily identify the version they are testing directly on the application icon.

## [Appium Server](/workflows/common-workflow-steps/appium-server)

This step installs [Appium Server](https://appium.io/) and starts it.

## [Authenticate with Netrc](/workflows/common-workflow-steps/authenticate-with-netrc)

The `.netrc` file contains login and initialization information used by the auto-login process. You can use this component to add credentials for hosts such as your repositories or external hosts. Git automatically recognizes the .netrc file. However, if you want to use the .netrc file with curl, you need to append the `-n` command line parameter. You may also use the `--netrc-optional` parameter if you don't always use the `.netrc` file with curl.

## [AWS Device Farm and Deploy](/workflows/common-workflow-steps/aws-device-farm-and-deploy)

**AWS Device Farm** is an application testing service that enables you to run your tests concurrently on multiple mobile devices to speed up the execution of your tests and generates videos and logs to help you quickly identify issues with your app.

## [Cache Push](/workflows/common-workflow-steps/build-cache/cache-push)

Learn to streamline your workflows by pushing data to cache with our easy-to-follow cache-push tutorial. Ideal for improving build performance.

## [Cache Pull](/workflows/common-workflow-steps/build-cache/cache-pull)

Discover the essentials of cache retrieval in our cache-pull guide. Speed up your build processes by mastering the art of efficiently pulling cached data.

## [Custom Script](/workflows/common-workflow-steps/custom-script)

You can use **Custom Script** steps for additional functionalities in your builds. Appcircle will run the commands in your custom scripts and perform the specified actions. These scripts will be run on the runner and you can use any functionality of the build environment as you need.

## [Code Reviews with Danger](/workflows/common-workflow-steps/danger)

**Danger** runs during your CI process and gives teams the chance to automate common code review chores. This provides another logical step in your build, through this Danger can help lint your rote tasks in daily code review. You can use Danger to codify your team’s norms. Leaving humans to think about harder problems.

https://blog.appcircle.io/article/danger-in-ci-automate-your-mobile-code-reviews

## [Data Theorem Mobile Secure](/workflows/common-workflow-steps/data-theorem-mobile-secure)

This component scans your app using Mobile Secure.

## [Export Build Artifacts](/workflows/common-workflow-steps/export-build-artifacts)

Exports the specified build artifacts from the build agent to the Appcircle dashboard. The exported files will be available for download from the artifacts section of the completed build.

## [Fastlane](/workflows/common-workflow-steps/fastlane)

Appcircle supports **Fastlane** for build automation as a supplementary feature to Appcircle's own build automation.

With Appcircle, you can automate your build and signing processes with the flexible workflow structure, and you can also use Fastlane as a workflow step within the build workflows.

## [File Size Check](/workflows/common-workflow-steps/file-size-check)

This component checks the file size and either warn or fail the workflow.

## [Firebase App Distribution](/workflows/common-workflow-steps/firebase-app-distribution)

Send your apps to be distributed via Firebase App Distribution.

https://github.com/appcircleio/appcircle-firebase-dsym-upload-component

## [Fortify On Demand](/workflows/common-workflow-steps/fod-mobile-assesment)

This step installs [Fortify on Demand](https://www.microfocus.com/en-us/cyberres/application-security/fortify-on-demand/) and submits a Fortify on Demand Mobile Assessment.

## [FTP Upload](/workflows/common-workflow-steps/ftp-upload)

This component uploads file or folders to given FTP server.

## [Git Clone](/workflows/common-workflow-steps/git-clone)

Clones the Git repository to the build agent with the given arguments.

## [Maestro Cloud Upload](/workflows/common-workflow-steps/maestro-cloud-upload)

This component uploads both your app binary and flows to Maestro Cloud.

## [Repeato Mobile Test Automation](/workflows/common-workflow-steps/repeato-test-runner)

This component creates and automates UI tests for iOS and Android.

## [Release Notes](/workflows/common-workflow-steps/publish-release-notes)

You can use **Release Notes** component to create release notes during your workflow.

## [Repeato Test Runner](/workflows/common-workflow-steps/repeato-test-runner)

**Repeato** is a test automation platform designed for mobile applications. It enables developers to create, manage, and execute automated tests for mobile apps across different platforms and devices. Repeato supports various testing frameworks and provides features for test script creation, test execution, result analysis, and reporting. It helps streamline the testing process, improve test coverage, and enhance the overall quality of mobile applications.

## [Saucectl Run](/workflows/common-workflow-steps/saucectl-run)

The `saucectl` command line interface orchestrates the relationship between your tests in your framework, and the rich parallelization, test history filtering, and analytics of Sauce Labs. saucectl performs the underlying business logic to access the tests in your existing framework, runs them in the Sauce Labs Cloud, then securely transmits the test assets to the Sauce Labs platform, where you can review, share, and evaluate your test outcomes at scale.

## [Select Java Version](/workflows/common-workflow-steps/select-java-version)

The **Select Java Version** step updates the JDK and Java version to the selected one during the build process.

## [Set Environment Variable](/workflows/common-workflow-steps/set-environment-variable)

The **Set Environment Variable** step enables the setting of environment values for specified keys. Although creating environment variables via the Environment Variables page is typically recommended, this step provides flexibility to modify environment variables directly within the build workflow when necessary.

## [Snyk Scan Security](/workflows/common-workflow-steps/snyk-scan-security)

By utilizing this step, you will be able to test your project dependencies for vulnerabilities during builds and use **Snyk** to monitor your projects.

## [SonarQube](/workflows/common-workflow-steps/sonarqube)

You can use **SonarQube** component to check your code quality.

## [Testinium](/workflows/common-workflow-steps/testinium)

The **Testinium** step allows users to upload their mobile applications to **Testinium** and run a test plan.

## [Testinium](/workflows/common-workflow-steps/testinium-upload-app)

The **Testinium Upload App** step enables uploading mobile applications to the **Testinium** platform for automated testing directly from Appcircle.

## [Testinium Run Test Plan](/workflows/common-workflow-steps/testinium-run-test-plan)

The **Testinium Run Test Plan** step allows users to run automated tests on their mobile applications using **Testinium** directly from the Appcircle.

## [Upload Files to Amazon S3](/workflows/common-workflow-steps/upload-files-to-amazon-s3)

The **Upload Files to Amazon S3** step in Appcircle enables direct uploading of any file or folder to the designated Amazon S3 bucket during the build process.