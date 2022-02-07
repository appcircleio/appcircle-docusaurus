---
title: iOS Certificates & Provisioning Profiles
metaTitle: iOS Certificates & Provisioning Profiles
metaDescription: iOS Certificates & Provisioning Profiles
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';

# iOS Certificates & Provisioning Profiles

<iframe width="600" height="315" src="https://www.youtube.com/embed/BTmOJTn3kuY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

You need to have your iOS Certificates and Provisioning Profiles ready to be able to build and deploy your applications to Apple Appstore.

:::info

For app builds, the signing identities are not mandatory. (e.g. you can use unsigned apps to run on the simulator or for use on third party platforms that resign your app such as AWS Device Farm)

However, unsigned binaries cannot be installed on actual devices; therefore they cannot be used in the Appcircle Distribute module.

:::

You can obtain your developer certificates and provisioning profiles from the Apple Developer Portal:

[https://developer.apple.com/support/code-signing/](https://developer.apple.com/support/code-signing/)

## iOS Code Signing Overview

### iOS Certificates

Certificate files can be in .p12 file format as a private-public key pair. There are 2 main types of iOS certificates:

**1. Apple Development:** Used for development and testing.

The development certificates allow deploying apps to the developer devices (connected physically for testing and debugging) during the actual development process on Xcode.

The common practice is to generate this certificate automatically on Xcode through manual generation is also available. Binaries built with a development certificate cannot be distributed.

**2. Apple Distribution:** Used for submitting applications to the App Store, or for Ad Hoc and Enterprise distribution. (Refer to the provisioning profiles section for the differences between these distribution types.)

In most cases, you will be using a distribution certificate with the combination of a provisioning profile to build and distribute apps in Appcircle.

There is a one-to-many relationship between certificates and provisioning profiles, so you may have multiple provisioning profiles associated with a single certificate.

### iOS Provisioning Profiles

Provisioning profiles can be in .mobileprovision file format. There are 4 main types of iOS certificates:

**1. Apple App Development:** Used to install development applications on test devices. This provisioning profile type is matched with a development certificate to enable app deployment during development. This is used mainly for debugging or functional testing.

**2. Ad Hoc:** Used for installing an application on a limited number of registered devices.

Ad Hoc profiles enable the installation of the binary on a specified device pool. This allows application testing on actual devices while limiting the app distribution to external parties by requiring all devices to be registered in the Apple Developer Portal to run any app signed by the Ad Hoc certificate of the same developer account.

There is a limit on the number of devices registered for Ad Hoc distribution and for the deployments with a development profile. This limit resets yearly.

For this purpose, you need to get the UDID information of your test devices, register them in the Apple Developer Portal, and then generate an Ad Hoc provisioning profile. You can then upload this file to the Appcircle Signing Identities module to be used in builds.

Please note that every time you add a new device, you have to regenerate the provisioning profile and reupload it to Appcircle. (Regeneration of the associated certificate is not necessary as long as it is valid.)

For more information on getting the UDID and registering it, please refer to the following Apple Developer guide. This guide walks you through all the steps necessary to get a device assigned to your Apple Developer account: [https://developer.apple.com/documentation/xcode/distributing-your-app-to-registered-devices](https://developer.apple.com/documentation/xcode/distributing-your-app-to-registered-devices);

You can use the Appcircle Distribute module to deploy apps built with an ad hoc profile. (If the receiving device is registered, of course.)

**3. App Store:** Used for submitting applications to the Apple App Store.

App Store profiles allow you to build store-ready versions of your app to be submitted to the App Store or to TestFlight. You can use the Appcircle Store Submit module to upload apps signed with an App Store profile to App Store Connect.

You cannot use the Appcircle Distribute module to deploy apps built with an App Store profile. (You can still share the binary but it cannot be installed on the target device.) The only valid target is for the apps signed with this profile is App Store Connect.

**4. Enterprise (In-House):** Used for in-house application distribution for the enterprises enrolled in the Apple Developer Enterprise Program.

This profile type is only available with the Apple Developer Enterprise program with strict requirements for registration. The apps signed with an enterprise profile can be installed freely on any device without going through the App Store or the Ad Hoc device registration.

The user will only be displayed a trust warning for the first time they are running an app signed with a specific enterprise certificate and then the app can be run just like an app downloaded from the App Store.

There are certain limitations that are mandated by the Apple Developer Enterprise program agreement such as the apps can only be used for work purposes by the actual employees of the enterprise, so it's not a free-for-all certificate to bypass the App Store processes. Apple reserves the right to revoke your certificate at any time in case of a violation.

You can use the Appcircle Distribute module or the Enterprise App Store module (coming soon) to deploy apps built with an enterprise profile to any device.

There is no need for device registration, but Apple requires the binary to be protected and not open for public download, so you can use the enrollment feature of the Appcircle Distribute module to protect the app distribution.

## Using the Appcircle Signing Identities Module for iOS;

### 1. Get iOS Provisioning Profiles from Apple

**If you want to upload provisioning profiles manually, **skip to step 2.

**Prerequisite**: To list all the signing identities saved in your Apple Developer Account, you need to add an App Store Connect API Key. Visit the link below for instructions.

<ContentRef url="/account/adding-an-app-store-connect-api-key">Adding an App Store Connect API Key</ContentRef>

When you go to add a new Provisioning Profile, you'll see the option **Get Provisioning Profiles from App Store Connect**. Select it to see the list of identities fetched from Apple.

![](https://cdn.appcircle.io/docs/assets/add-certificates-2-low.jpg)

You can select to download the provisioning profile from the list. **If you don't want Appcircle to keep the provisioning profile**, you can make our build agents to keep a reference. This way, our agents will fetch the profiles** before every build and dismiss them **when the build is finalized.

![](https://cdn.appcircle.io/docs/assets/certificate-list-2-low.jpg)

After saving, you can **skip to step 3**.

### 2. Generate Or Upload iOS Certificates

To generate or upload your iOS certificate, select **iOS Certificates** from the signing module.

:::info

All types of iOS certificates are supported, including development, ad hoc, in-house, or App Store distribution.

:::

Click on "Add New" button to upload or create your iOS Certificate.

![](https://cdn.appcircle.io/docs/assets/02-01-Add-iOS-Certificates.jpg)

You can either upload your readily available certificate bundle (P12) along with the bundle password or create a certificate signing request (CSR) to generate a new certificate from the Apple Developer portal and then upload the certificate (CER) to create a certificate bundle (P12). No Mac device is needed.

![](https://cdn.appcircle.io/docs/assets/02-02-Add-iOS-Certificates.jpg)

To generate your iOS certificates, simply fill in your details and Appcircle will provide a CSR (certificate signing request) which you can use on Apple Developer Portal to generate your signing certificate.

- Download your CSR file
- Upload it to the Apple Developer Portal for certificate creation
- Download your generated CER file from the Apple Developer portal
- Upload the CER file to the signing identities module by clicking on the upload button next to the CSR file.
- Your CSR will now be converted to a P12 file as an iOS signing certificate. (Please note that the P12 file comes with an empty password.);

![](https://cdn.appcircle.io/docs/assets/02-07-Generate-iOS-Cert.jpg)

To upload your iOS certificate, select "Upload Certificate Bundle (.p12)" button and upload your pre-obtained iOS certificate file.

![](https://cdn.appcircle.io/docs/assets/02-02-Upload-iOS-Certificates.jpg)

You can see a list of your created or uploaded certificates. Each certificate will display the certificate name, certificate type (development, ad-hoc, in-house, or app store distribution) along with expiration dates.

![](https://cdn.appcircle.io/docs/assets/02-08-CertificateList.jpg)

### 2. Upload iOS Provisioning Profiles

Simply upload your provisioning profiles obtained from the Apple Developer portal.

![](https://cdn.appcircle.io/docs/assets/02-03-Upload-Provisioning-Profile.jpg)

:::info

Provisioning profile and certificate matching will be done automatically. You can also have multiple provisioning profiles to use in different applications with different Apple developer accounts.

:::

You can list and manage your provisioning profiles here. If there is a matching certificate, the profile will show a green check mark to indicate that. If not, you will see a red cross mark indicating there's no certificate matching the provisioning profile.

You can also see the matching application ID and expiration date of the profiles here.

![](https://cdn.appcircle.io/docs/assets/02-07-Provision-Details.jpg)

### **3. Assign signing identities in the Build module for distribution**

For both iOS or Android build projects, you need to assign your signing identities to your build profile for distribution. The distribution-ready binaries will be signed with the selected signing identities both in manual and automatic distribution cases.

![](https://cdn.appcircle.io/docs/assets/03-02-iOS-Build-Signing.jpg)

:::warning

If your app has multiple targets such as watchOS, Widgets etc, you need to add all the provisioning profiles for every bundle id. Click **+** button and add related bundle id and provisioning profile.

:::

:::info

[Have questions? Contact us here.](https://appcircle.io/support/)

:::
