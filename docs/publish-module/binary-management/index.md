---
title: Binary Management
description: Learn how to manage binaries in Appcircle
tags: [publish module, binary management]
---

# Binary Management

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';
import PatDanger from '@site/docs/\_pat-usage-workflows-danger.mdx';
import EnvGroupSetCaution from '@site/docs/\_env-group-set-on-config-caution.mdx';
import NewerVersionCodeCaution from '@site/docs/\_newer-version-code-caution.mdx';

Appcircle supports publishing the application to the stores without using the Build module. To add an application version manually, you need to add a publish profile beforehand and then **Open** its details.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-manuel.png' />

You can then upload the application by clicking on the **Add Version** button on the right.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-upload.png' />

When the upload is completed successfully, the relevant application versions will appear in the list.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-publishBinaryList.png' />

:::caution BUNDLE ID AND PACKAGE NAME MUST BE UNIQUE
You can install iOS app versions with different BundleIDs under the same Publishing Profile. However, you can only initiate the Publish process with the binary that matches the BundleID specified when creating the profile or within the profile itself.

Similarly, for Android Publish Profiles, all app versions must have identical Package Names within the Android Publish Profile.

You can view the Bundle ID (iOS) and Package Name (Android) beneath the Publish Profile name. Users can also verify this information by selecting the [Binary Information](/publish-module/publish-information/binary-information) for an app version under the actions menu.
:::

### BundleID Matching

When a binary BundleID uploaded to the Publish profile does not match the master BundleID specified for the profile, a warning icon will appear next to the binary. This icon indicates that the BundleID of the related binary does not match. For this reason, you **cannot start the Publish process** with the mismatched binary and send your application to the stores.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE3923-binaryMatch.png' />

:::caution BundleID Matching

Note that you cannot mark your application version with a mismatched BundleID as a [**Release Candidate**](/publish-module/publish-information/marking-release-candidates). 

For BundleID change, you can use the [**Resign Binary**](/publish-module/publish-information/resign-binary) feature in the Action button or upload a matching binary.

:::

Afterwards, you can start submitting your application to the stores with the publish flow that you have configured.

<Screenshot url='https://cdn.appcircle.io/docs/assets/publish-version-list.png' />

For this, click on the **Actions** button for the relevant version and go to **Details**. From there, you can manually **Start Flow** for the uploaded application version.

## Store Status

Appcircle now allows you to track the App Store status of your applications directly within the Publish module. This powerful feature is tailored for **Enterprise License** holders, ensuring continuous monitoring of your application's deployment status.

<Screenshot url='https://cdn.appcircle.io/docs/assets/be-3681-publish-store-status.png' />

### How It Works

- **Enterprise License**: This feature is accessible to users with an enterprise license.
- **Continuous Monitoring**: Once a version is set as a **Release Candidate**, it is automatically monitored **every 30 minutes** to check its status on **TestFlight** and the **App Store Distribution**.
- **Priority on Distribution**: If the version is available in both **TestFlight** and **App Store Distribution**, the system prioritizes the status from **App Store Distribution**.
- **Version Status**: If a version has **never** been submitted to the **App Store**, it will show as **`Not Available`**.
- **Completion of Distribution**: When a version reaches **`Ready for Distribution`**, Appcircle stops monitoring it, allowing you to focus resources on versions that still require attention.

:::caution Store Credentials Required
Ensure you select store credentials in the [Publish settings](/publish-module/publish-settings#store-credentials) to start monitoring. If the credentials are **not** selected, the status will display as **`Not Available`**.
:::

This streamlined approach ensures that you are always informed of your application's status, simplifying management and enhancing your deployment strategy directly from the Appcircle dashboard.

### Filter By Status

In the Publish module, where your Publish profiles are listed, you can use the filter option to display specific Publish profiles based on their latest store status.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3106-publishfilter1.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3106-publishfilter2.png' />

:::tip

The iOS Publish filter options will only display the available statuses from the existing Publish profiles in your profile list.

:::

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3106-publishfilter3.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE-3106-publishfilter4.png' />

## FAQ

### How can I get a binary from another organization to use in the Publish Module ?

Let’s assume there are two organizations: Organization A and Organization B.
In Organization A, we have a build profile that generates an IPA, APK, or AAB.
In Organization B, we have a Publish profile that we want to send the binary to.

In Organization A's build profile workflow, after the build step, we can add a [Custom Script](/workflows/common-workflow-steps/custom-script/) step that includes the code snippet below to transfer the binary generated in Organization A to the Publish profile in Organization B. In order to do this, we need [Appcircle CLI](/appcircle-api-and-cli/cli-authentication), so this code snippet sets up the necessary information and sends binary with parameters.

```bash
#Bash script
sudo npm install -g @appcircle/cli
appcircle login --pat $ORG_B_PERSONAL_API_TOKEN
# If an IPA or AAB is required, change *.apk to *.ipa or *.aab
appcircle publish profile version upload \
  --platform <string> \
  --publishProfileId "$ORG_B_PUBLISH_PROFILE_ID" \
  --app "$AC_OUTPUT_DIR"/*.apk \
  --markAsRc <boolean> \
  --summary <string>
```

:::info

- --platform "ios" or "android" **[REQUIRED]** Specifies the platform for the binary.
- --markAsRc true/false  **[OPTIONAL]** Marks the binary as a release candidate automatically. (Default: `false`)
- --summary "Release Notes" **[OPTIONAL]** Adds release notes to the app version.  
  Note: To include release notes, the version must first be marked as a release candidate.  

:::

:::caution

Ensure that, uploading a binary to a Publish profile will require exact same **Package Name** or **Bundle ID**

:::

<NewerVersionCodeCaution />

The key point here is that we need two essential parameters to make this work.
- `ORG_B_PERSONAL_API_TOKEN` => Organization PAT (Personal API Token) from Organization B 
- `ORG_B_PUBLISH_PROFILE_ID` => Publish profile ID from Organization B

`$AC_OUTPUT_DIR` is an automatically generated environment variable. [Reserved Variables](/environment-variables/appcircle-specific-environment-variables/)

To generate Personal API Token, follow this documentation [API authentication](/appcircle-api-and-cli/api-authentication/)

To obtain the Publish profile ID, follow the steps below: 
1. Log in to organization B.
2. Go to Publish module.
3. Select the desired Publish profile
4. Copy it from the URL. `https://my.appcircle.io/publish/android/123456f-7d89-4545-5454-123456789abc`
5. Then the Publish profile ID is => `123456f-7d89-4545-5454-123456789abc`

After collecting the essential parameters, they have to be set in the [Environment Variables](/environment-variables/) as 
ORG_B_PERSONAL_API_TOKEN,
ORG_B_PUBLISH_PROFILE_ID

<PatDanger />

<EnvGroupSetCaution />