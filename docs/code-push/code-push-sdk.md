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

Using commandline to install SDK. Please run this command in project root direction.

```bash
npm i @appcircle/react-native-code-push
```

Usign `package.json` file to add SDK. Please add SDK to dependencies section in `package.json`.

```json package.json
"dependencies": {
    "@appcircle/react-native-code-push": "0.0.2-alpha.3",
    
    //Other Dependencies here
}
```

**Note:** If you add the SDK directly to your `package.json` file instead of using the command line, you must run `npm install` in the project directory afterwards to install the dependency.

## CodePush Configurations in Project


To ensure that your app receives the correct updates, you must configure the appropriate deployment key in your project. Each deployment channel created in Appcircle has a unique key, which must be specified in your CodePush configuration. This allows your app to connect to the correct environment, such as staging or production.

To ensure that apps can properly receive updates, the `Server URL` and `Deployment Key` must be correctly added to the native code of your project. For more information about, please visit the [**Deployment Keys**](/code-push/code-push-profile/code-push-release-management#deployment-keys) documentation.

Instructions on how to add these configurations for both iOS and Android platforms are provided below.

:::info Server URL

If you are using a self‑hosted version of Appcircle, use the **ServerURL** value defined for your self‑hosted instance.  
For Appcircle Cloud, the **ServerURL** is `https://my.appcircle.io/codepush`.

:::

<Tabs defaultValue="react-native-ios" values={[
{ label: 'Info.plist for iOS', value: 'react-native-ios' },
{ label: 'Strings.xml for Android', value: 'react-native-android' },
]}>

  <TabItem value="react-native-ios">
    ```swift
    <key>CodePushServerURL</key>
        <string>https://my.appcircle.io/codepush</string>

    <key>CodePushDeploymentKey</key>
        <string>YOUR_DEPLOYMENT_KEY</string>  
    ```
  </TabItem>

  <TabItem value="react-native-android">
  
    ```java
    <string moduleConfig="true" name="CodePushServerUrl">https://my.appcircle.io/codepush</string>

    <string moduleConfig="true" name="CodePushDeploymentKey">YOUR_DEPLOYMENT_KEY</string>
    ```
  </TabItem>

</Tabs>

#### Plugin Installation and Configuration for React Native 0.60 version and above (Android)

1. In your android/settings.gradle file, make the following additions at the end of the file:

```java
include ':app', ':appcircle_react-native-code-push'
project(':appcircle_react-native-code-push').projectDir = new File(rootProject.projectDir, '../node_modules/@appcircle/react-native-code-push/android/app')
```

2. In your android/app/build.gradle file, add the codepush.gradle file as an additional build task definition to the end of the file:

```java
apply from: "../../node_modules/@appcircle/react-native-code-push/android/codepush.gradle"
```

3. Update the MainApplication file to use CodePush via the following changes:

For React Native 0.73 and above: update the MainApplication.kt

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

For React Native 0.72 and below: update the MainApplication.java

```java
// 1. Import the plugin class.
import com.microsoft.codepush.react.CodePush;

public class MainApplication extends Application implements ReactApplication {

    private final ReactNativeHost mReactNativeHost = new ReactNativeHost(this) {
        ...

        // 2. Override the getJSBundleFile method in order to let
        // the CodePush runtime determine where to get the JS
        // bundle location from on each app start
        @Override
        protected String getJSBundleFile() {
            return CodePush.getJSBundleFile();
        }
    };
}
```


### SDK Integration and Basic Usage

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

Alternatively, if you want fine-grained control over when the check happens (like a button press or timer interval), you can call `CodePush.sync()` at any time with your desired `SyncOptions`, and optionally turn off CodePush's automatic checking by specifying a manual `checkFrequency`:

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
