---
title: CodePush SDK
description: Learn how to integrate Appcircle CodePush SDK to React Native projects.
tags: [appcircle codepush, sdk, codepush, react native]
sidebar_position: 2
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# CodePush SDK

This section provides comprehensive guidance on how to integrate the Appcircle CodePush SDK into your React Native project, enabling seamless over-the-air (OTA) updates that improve user experience by delivering updates without requiring users to download a new version from the app store.

https://www.npmjs.com/package/@appcircle/react-native-code-push

## React Native Project Integration

To start using the Appcircle CodePush feature, the first step is to integrate the [**Appcircle CodePush SDK**](https://www.npmjs.com/package/@appcircle/react-native-code-push) into your project. You can do this by installing the SDK directly via npm or by adding the dependency to your `package.json` file.

1. To install the SDK using the command line, run the following command in the root directory of your project.

```bash
npm i @appcircle/react-native-code-push
```

2. Using `package.json` file to add the SDK: 
Add the SDK to dependencies section in your `package.json` file.

```json package.json
"dependencies": {
    "@appcircle/react-native-code-push": "0.0.3",
    
    //Other Dependencies here
}
```

**Note:** If you add the SDK directly to your `package.json` file instead of using the command line, you must run `npm install` in the project directory afterwards to install the dependency.

## CodePush Configurations in Project

To ensure that your app receives the correct updates, you must configure the appropriate deployment key in your project. Each deployment channel created in Appcircle has a unique key, which must be specified in your CodePush configuration. This allows your app to connect to the correct environment, such as `Staging` or `Production`.

To ensure that apps can properly receive updates, the `Server URL` and `Deployment Key` must be correctly added to the native code of your project. For more information, please visit the [**Deployment Keys**](/code-push/code-push-profile/code-push-release-management#deployment-keys) documentation.

Instructions on how to add these configurations for both iOS and Android platforms are provided below.

:::info Server URL

If you are using a self‑hosted version of Appcircle, use the **ServerURL** value defined for your self‑hosted instance.  
For Appcircle Cloud, the **ServerURL** is `https://api.appcircle.io/codepush`.

:::

<Tabs defaultValue="react-native-ios" values={[
{ label: 'Info.plist for iOS', value: 'react-native-ios' },
{ label: 'Strings.xml for Android', value: 'react-native-android' },
]}>

  <TabItem value="react-native-ios">
    ```swift
    <key>CodePushServerURL</key>
        <string>https://api.appcircle.io/codepush</string>

    <key>CodePushDeploymentKey</key>
        <string>YOUR_DEPLOYMENT_KEY</string>  
    ```
  </TabItem>

  <TabItem value="react-native-android">
  
    ```java
    <string moduleConfig="true" name="CodePushServerUrl">https://api.appcircle.io/codepush</string>

    <string moduleConfig="true" name="CodePushDeploymentKey">YOUR_DEPLOYMENT_KEY</string>
    ```
  </TabItem>

</Tabs>

#### Enabling CodePush Code Signing

To leverage Appcircle's CodePush Code Signing capability for release validation, you must integrate the public key you generated locally into your project configuration. Using this key pair, the Appcircle CodePush SDK verifies the signature of each incoming release against the key embedded in the app and decides whether the update can be applied. If verification fails, the update is blocked and will not be installed by the device. 

For complete setup instructions, refer to the CodePush Code Signing [documentation.](/code-push/code-push-code-signing)

### SDK Installation and Configuration

The SDK installation and configuration steps for `iOS` and `Android` are detailed below.

#### Compatible React Native Versions

**Appcircle CodePush SDK** supports React Native **0.76+** and **the new architecture**.

If you are using React Native version **0.75 or earlier**, you need to use the **Microsoft CodePush SDK** to enable Appcircle CodePush functionality. 

| React Native Version(s)                    | SDK                                 |
|--------------------------------------------|-------------------------------------|
| Below 0.76 | Use [**Microsoft SDK**](https://github.com/microsoft/react-native-code-push)| 
| 0.76 and above | Use [**Appcircle CodePush SDK**](https://www.npmjs.com/package/@appcircle/react-native-code-push) |

:::caution If Using Microsoft SDK

If you are using Microsoft SDK, make sure to add the **Appcircle Server URL** and **Deployment Key** correctly in your `info.plist` and `strings.xml` file. For detailed information, please navigate to the [**React Native Project Configuration**](/code-push/code-push-sdk#react-native-project-integration) section.

:::

#### For iOS

Follow the installation steps below to use the CodePush SDK in your iOS applications.

1. Run `cd ios && pod install && cd ..` to install all the necessary **CocoaPods** dependencies.​

2. Open up the AppDelegate.m file, and add an import statement for the CodePush headers:

```swift
#import <CodePush/CodePush.h>

```

3. Find the following line of code, which sets the source URL for bridge for production releases:

```swift
return [[NSBundle mainBundle] URLForResource:@"main" withExtension:@"jsbundle"];

```

4. Replace it with this line:

```swift
return [CodePush bundleURL];

```

This change configures your app to always load the most recent version of your app's JS bundle. On the first launch, this will correspond to the file that was compiled with the app. However, after an update has been pushed via CodePush, this will return the location of the most recently installed update.

Your sourceURLForBridge method should look like this:

```swift
- (NSURL *)sourceURLForBridge:(RCTBridge *)bridge
{
  #if DEBUG
    return [[RCTBundleURLProvider sharedSettings] jsBundleURLForBundleRoot:@"index"];
  #else
    return [CodePush bundleURL];
  #endif
}
```

#### For Android

1. In your `android/settings.gradle` file, make the following additions at the end of the file:

```java
include ':app', ':appcircle_react-native-code-push'
project(':appcircle_react-native-code-push').projectDir = new File(rootProject.projectDir, '../node_modules/@appcircle/react-native-code-push/android/app')
```

2. In your `android/app/build.gradle` file, add the `codepush.gradle` file as an additional build task definition to the end of the file:

```java
apply from: "../../node_modules/@appcircle/react-native-code-push/android/codepush.gradle"
```

3. Update the MainApplication file to use CodePush via the following changes:

Update the `MainApplication.kt`.

```java
// 1. Import the plugin class.
import com.microsoft.codepush.react.CodePush


class MainApplication : Application(), ReactApplication {

override val reactNativeHost: ReactNativeHost =
    object : DefaultReactNativeHost(this) {
        ...

        // 2. Override the getJSBundleFile method in order to let
        // the CodePush runtime determine where to get the JS
        // bundle location from on each app start
        override fun getJSBundleFile(): String {
            return CodePush.getJSBundleFile() 
        }
    };
}
```

### SDK Basic Example Usage

After installing the SDK, you need to import and configure it within your React Native project. Below is a basic example of how to use the Appcircle CodePush SDK:

Wrap your root component with the CodePush higher-order component:

- For class component

```javascript
import CodePush from '@appcircle/react-native-code-push';

class MyApp extends Component {
}

MyApp = codePush(MyApp);
```

- For functional component

```javascript
import CodePush from '@appcircle/react-native-code-push';

let MyApp: () => React$Node = () => {
}

MyApp = codePush(MyApp);
```

If you would like your app to discover updates more quickly, you can also choose to sync up with the CodePush server every time the app resumes from the background.

- For class component

```javascript
let codePushOptions = { checkFrequency: codePush.CheckFrequency.ON_APP_RESUME };

class MyApp extends Component {
}

MyApp = codePush(codePushOptions)(MyApp);
```

- For functional component

```javascript
let codePushOptions = { checkFrequency: codePush.CheckFrequency.ON_APP_RESUME };

let MyApp: () => React$Node = () => {
}

MyApp = codePush(codePushOptions)(MyApp);
```

Alternatively, if you want fine-grained control over when the check occurs (such as a button press or timer interval), you can call `CodePush.sync()` at any time with your desired `SyncOptions`. You can also disable CodePush’s automatic checking by setting the `checkFrequency` to manual.

```javascript
let codePushOptions = { checkFrequency: codePush.CheckFrequency.MANUAL };

class MyApp extends Component {
    onButtonPress() {
        codePush.sync({
            updateDialog: true,
            installMode: codePush.InstallMode.IMMEDIATE
        });
    }

    render() {
        return (
            <View>
                <TouchableOpacity onPress={this.onButtonPress}>
                    <Text>Check for updates</Text>
                </TouchableOpacity>
            </View>
        )
    }
}

MyApp = codePush(codePushOptions)(MyApp);
```

This configuration ensures that your app checks for updates when it starts, and installs them on the next app restart. You can customize the behavior further using CodePush options based on your needs.

## FAQ

### How to Use CodePush with New Architecture on Android?

[**Appcircle CodePush SDK**](https://www.npmjs.com/package/@appcircle/react-native-code-push) supports the new architecture on Android for React Native versions 0.76 and above.

If you are having trouble using CodePush with new architecture in your Android app, you can update
your `MainApplication.kt` file as follows:

```kotlin
// 1. import UnstableReactNativeAPI
import com.facebook.react.common.annotations.UnstableReactNativeAPI 

@OptIn(UnstableReactNativeAPI::class)  // 2. add this line here
class MainApplication : Application(), ReactApplication {

...

// 3. replace these lines
override val reactHost: ReactHost
        get() = getDefaultReactHost(applicationContext, reactNativeHost)

// with the following lines
    override val reactHost: ReactHost
        get() = getDefaultReactHost(
            applicationContext,
            PackageList(this).packages.apply {
                // Packages that cannot be autolinked yet can be added manually here, for example:
                // add(MyReactNativePackage())
            },
            jsMainModulePath = "index",
            jsBundleAssetPath = "index.android.bundle",
            jsBundleFilePath = CodePush.getJSBundleFile(),
            isHermesEnabled = BuildConfig.IS_HERMES_ENABLED,
            useDevSupport = BuildConfig.DEBUG,
        )
```

### How to Fix `A JS bundle file named "null" could not be found within the downloaded contents` Error on Android?

If you are using [**Microsoft CodePush SDK**](https://github.com/microsoft/react-native-code-push)  with the new architecture enabled, you may encounter this error when attempting to push OTA updates. If that happens, you can follow [**these instructions**](https://github.com/microsoft/react-native-code-push/issues/2083#issuecomment-1411745157) to resolve it. 

Alternatively, you can use the [**Appcircle CodePush SDK**](https://www.npmjs.com/package/@appcircle/react-native-code-push), which supports the new architecture for React Native 0.76 and above.

### Does Appcircle CodePush support Expo projects?

No, Appcircle CodePush currently supports only bare React Native projects. Managed Expo apps are not supported at this time.