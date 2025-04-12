---
title: Testing Distribution
description: Learn how to create a distribution profile and share your builds with testers in Appcircle
tags: [distribution, distribution profile, testing distribution, testers, faq]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';
import PatDanger from '@site/docs/\_pat-usage-workflows-danger.mdx';

In order to share your builds with testers, you can create distribution profiles and assign testing groups to the distribution profiles.

<Screenshot url='https://cdn.appcircle.io/docs/assets/distribution-start.png' />

> Note that an empty Testing Distribution profile named **Send to Myself** will be created automatically for you.

:::info

A distribution profile corresponds to the multiple versions of the same application for iOS and Android. You do not need to create multiple Testing Distribution profiles for iOS and Android applications of the same application.
:::

<iframe width="600" height="315" src="https://www.youtube.com/embed/vZ3p5uZZcmk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## [Distribution Profile](/testing-distribution/create-or-select-a-distribution-profile)

To share builds with testers, distribution profiles should be created and testing groups assigned to these profiles.

## [Testing Groups](/testing-distribution/testing-groups)

The testing group feature is used to manage and organize testers. Different versions of applications can be distributed to specific groups based on testing needs, such as OS versions, features, devices, and more.

## [Re-sign Binaries](/testing-distribution/resigning-binaries)

Re-signing is the process of modifying an existing binary with a new signing certificate or keystore, required when an application needs to be published under a different developer account or when updating an existing application. This process involves removing the original signature and replacing it with a new one.

## [Testing Portal](/testing-distribution/testing-portal)

Appcircle has a separate distribution screen designed to make it easy for test group developers and testers download the distributed applications easily.

## [Reporting](/testing-distribution/reports)

Optimize your application management with detailed reports. Utilize the App Sharing Report and App Versions Report to gain insights and make informed decisions about your app's distribution and evolution.

## FAQ

### How can I get a binary from another organization for use in the Testing Distribution module?

Let’s assume there are two organizations: Organization A and Organization B.
In Organization A, we have a build profile that generates an IPA/APK.
In Organization B, we have a testing distribution profile that we want to send the binary to.

In Organization A's build profile workflow, just before the [Export Build Artifacts](/workflows/common-workflow-steps/export-build-artifacts/) step, we can add a [Custom Script](/workflows/common-workflow-steps/custom-script/) step that includes the code snippet below to transfer the binary generated in Organization A to the Testing Distribution profile in Organization B. In order to do this, we need [Appcircle CLI](/appcircle-api-and-cli/cli-authentication), so this code snippet sets up the necessary information and sends binary with parameters.

```bash
#Bash script
sudo npm install -g @appcircle/cli
appcircle login --pat $ORG_B_PERSONAL_API_TOKEN
#if ipa or aab is required change it to *.ipa or *.aab 
#in the --app "$AC_OUTPUT_DIR"/*.apk code line down below
appcircle testing-distribution upload \
  --distProfileId "$ORG_B_TEST_DIST_PROFILE_ID" \
  --message "Release Notes" \
  --app "$AC_OUTPUT_DIR"/*.apk
```

The key point here is that we need two essential parameters to make this work.
- `ORG_B_PERSONAL_API_TOKEN` => Organization PAT (Personal API Token) from Organization B 
- `ORG_B_TEST_DIST_PROFILE_ID` => Testing Distribution profile ID from Organization B

To generate Personal API Token, follow this documentation [API authentication](/appcircle-api-and-cli/api-authentication/)

Testing Distribution profile ID is simply logging in to the organization B, selecting the desired testing distribution profile, and dividing the URL.
For example, let's assume this is the URL after selecting the Testing Distribution profile.
`https://my.appcircle.io/distribute/detail/123456f-7d89-4545-5454-123456789abc`

Then the testing distribution profile ID is => `123456f-7d89-4545-5454-123456789abc`

`$AC_OUTPUT_DIR` is an automatically generated environment variable. [Reserved Variables](/environment-variables/appcircle-specific-environment-variables/)

After collecting the essential parameters, they have to be set in the [Environment Variables](/environment-variables/) as 
ORG_B_PERSONAL_API_TOKEN,
ORG_B_TEST_DIST_PROFILE_ID

<PatDanger />

:::caution

Set the environment variable group to be used in the Organization A build profile configurations.

:::

### No files or multiple files were received from autodistribute;

A successful distribution depends on a correctly signed binary. Please check if the [signing configuration](/build/build-process-management/configurations#signing-configuration) is correct.

You can also check the list of the [generated build artifacts](/build/build-process-management#binary-actions) to confirm the output. In Android, you can also check the `ac_post_process_output.json` file in the build artifacts to see if the APKs are signed or not.

In Android, please also check if gradle sign is being used for the selected build variant. If gradle sign works alongside with Appcircle signing, you will receive multiple APKs.

### Deleted versions still occupy storage space

The master version of any artifact deployed from the Build to the Testing Distribution is stored within the build artifacts section. Once you delete such a version from the Testing Distribution, only the reference is removed and the binary is still available within the build artifacts of the related build. You also need to remove the binary from the build artifacts to save storage.

### Access Denied on builds

On some distributed apps, the **Access Denied** error can be bypassed by one of these steps:

- Launching the distribution link on a different browser and Incognito Mode
- Clearing the browser cache if the link is pasted to a browser instead of in-line browser on mail applications
- If there is an authorization configuration on Distribution, clearing the authorization temporarily