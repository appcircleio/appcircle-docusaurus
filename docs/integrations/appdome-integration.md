---
title: Appdome Integration
metaTitle: Appdome Integration
metaDescription: Appdome Integration
sidebar_position: 11
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

[Appdome Build-2Secure](https://apis.appdome.com/docs/integrate-in-cicd) automates the integration of advanced security features, adaptive protections, code-signing, and certification processes into mobile applications, enhancing security without the need for manual coding or code analysis.

For detailed information on the benefits Appdome Build-2Secure adds to your mobile app, refer to the blog post:

<ContentRef url="https://appcircle.io/blog/elevate-your-mobile-app-security-with-appdome-and-a-guide-to-integration-with-appcircle">Elevate Your Mobile App Security with Appdome and A Guide to Integration with Appcircle</ContentRef>

## Step 1: Add Appdome Build-2Secure step in your workflows

Ensure that your application (APK, AAB, or IPA) is built before adding the Appdome Build-2Secure step.

<Screenshot url='https://cdn.appcircle.io/docs/assets/video-appdome-blog-1.gif' />

## Step 2: Configure the Appdome Build-2Secure step inputs

Fill in the Appdome Build-2Secure component inputs with the Appdome credential.

<Screenshot url='https://cdn.appcircle.io/docs/assets/appdome-blog-1.png' />

:::caution
Enter confidential information as [secret environment variables](https://docs.appcircle.io/environment-variables/managing-variables#adding-key-and-text-based-value-pairs).
:::

:::caution
Ensure the [environment variable group](https://docs.appcircle.io/environment-variables/managing-variables#using-environment-variable-groups-in-builds) is selected in the configuration.
:::

Below is the list of inputs that are required to use Appdome Build-2Secure for iOS and Android.

:::info
Optional inputs are marked as `(optional)` explicitly. Otherwise that's a mandatory input which must have a valid value.
:::

### Common Inputs

- **Appdome API Key:** Get this key from Appdome. Follow [this document](https://apis.appdome.com/docs/getting-started#getting-and-resetting-your-appdomes-build2secure-api-token) for more information.
- **Appdome Fusion Set ID:** Get this ID from Appdome. Follow [this document](https://apis.appdome.com/docs/getting-started#getting-a-fusion-sets-id) for more information.
- **Appdome Team ID (optional):** If you use a team account, insert your team's ID. Follow [this document](https://apis.appdome.com/docs/getting-started#getting-a-teams-id) for more information.
- **Signing Method:** Automatically sign applications using the Appdome service. Follow [this document](https://www.appdome.com/how-to/devsecops-automation-mobile-cicd/automated-signing-secured-android-ios/automatic-code-signing-for-secured-android-apps-on-appdome/) for more information.

### Android Specific Inputs

- **App File Path:** The app URL or path that's accessible from Appcircle.
  - Use `$AC_APK_PATH` or `$AC_AAB_PATH` as default values.
- **Google Play Signing (optional):** If true, distribute through the Google Play App Signing program. Details [here](https://www.appdome.com/how-to/devsecops-automation-mobile-cicd/automated-signing-secured-android-ios/automatic-code-signing-for-secured-android-apps-on-appdome/).
- **Build with Logs (optional):** If "true", enable diagnostic logs. Details [here](https://www.appdome.com/how-to/devsecops-automation-mobile-cicd/test-secured-mobile-apps/appdome-diagnostic-logs-for-troubleshooting-secured-apps/).

### iOS Specific Inputs

<Screenshot url='https://cdn.appcircle.io/docs/assets/appdome-blog-2.png' />

- **App File Path:** IPA file path or URL should be accessible from Appcircle.
  - Use `$AC_EXPORT_DIR/<myappname>.ipa` as the default value.
- **iOS Entitlement File Paths:** Obtain from Xcode. Details [here](https://www.appdome.com/how-to/devsecops-automation-mobile-cicd/automated-signing-secured-android-ios/extract-and-use-ios-entitlements-files-for-signing-secured-ios-app/).
- **iOS Provisioning Profiles:** Paths of the provisioning profiles. Details [here](https://www.appdome.com/dev-sec-blog/best-practices-for-signing-ios-applications/).
- **iOS Certificate File Path:** Paths of the certificate file with a `.p12` extension. Details [here](https://www.appdome.com/dev-sec-blog/best-practices-for-signing-ios-applications/).
- **iOS Certificate Password:** Password for the added certificate. Details [here](https://www.appdome.com/dev-sec-blog/best-practices-for-signing-ios-applications/).

## Step 3: Start build

Start the build with the configuration set and workflow that you configured for Appdome.

<Screenshot url='https://cdn.appcircle.io/docs/assets/appdome-blog-3.png' />

## Step 4: Get DevSecOps Certified and secured app with Build-2Secure

The Appdome step produces a protected app (APK, IPA, or AAB) and a [Certified Secure™](https://www.appdome.com/certified-secure-mobile-devsecops-certification/), ensuring that the mobile application has undergone a thorough security certification process, meeting the highest standards of security and protection.

**Download artifacts** from the **Builds** list using the actions menu on build detail.

<Screenshot url='https://cdn.appcircle.io/docs/assets/video-appdome-blog-2.gif' />

Additionally, the following outputs can be used in the next steps:

- **`AC_APPDOME_SECURED_IPA_PATH`:** Local path of the secured IPA file for iOS projects.
- **`AC_APPDOME_SECURED_APK_PATH`:** Local path of the secured APK file (available when 'Signing Method' is set to 'On-Appdome' or 'Private-Signing').
- **`AC_APPDOME_SECURED_AAB_PATH`:** Local path of the secured AAB file (available when 'Signing Method' is set to 'On-Appdome' or 'Private-Signing').
- **`AC_APPDOME_PRIVATE_SIGN_SCRIPT_PATH`:** Local path of the .sh sign script file (available when 'Signing Method' is set to 'Auto-Dev-Signing').
- **`AC_APPDOME_CERTIFICATE_PATH`:** Local path of the `certificate.pdf` file.

Moreover, you can access the source code for this integration on GitHub:

- For **iOS** Appdome Build-2Secure source code, visit the following repository:

[https://github.com/appcircleio/appcircle-ios-appdome-component](https://github.com/appcircleio/appcircle-ios-appdome-component)

- For **Android** Appdome Build-2Secure source code,, visit the following repository:

[https://github.com/appcircleio/appcircle-android-appdome-component](https://github.com/appcircleio/appcircle-android-appdome-component)
