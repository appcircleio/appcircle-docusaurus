---
title: Appcircle CodePush SDK
description: Learn how to integrate Appcircle CodePush SDK to React Native projects.
tags: [appcircle codepush, sdk, codepush, react native]
sidebar_position: 2
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Appcircle CodePush SDK

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

### SDK Integration in Project

After installing the SDK, you need to import and configure it within your React Native project. Below is a basic example of how to use the Appcircle CodePush SDK:

```javascript
import codePush from '@appcircle/react-native-code-push';

let App = () => {
  // Your app component logic
};

App = codePush({
  checkFrequency: codePush.CheckFrequency.ON_APP_START,
  installMode: codePush.InstallMode.ON_NEXT_RESTART,
})(App);

export default App;
```

This configuration ensures that your app checks for updates when it starts, and installs them on the next app restart. You can customize the behavior further using CodePush options based on your needs.


## CodePush Configurations in Project


To ensure that your app receives the correct updates, you must configure the appropriate deployment key in your project. Each deployment channel created in Appcircle has a unique key, which must be specified in your CodePush configuration. This allows your app to connect to the correct environment, such as staging or production.

To ensure that apps can properly receive updates, the `Server URL` and `Deployment Key` must be correctly added to the native code of your project. For more information about, please visit the [**Deployment Keys**](/code-push/code-push-profile/code-push-release-management#deployment-keys) documentation.

Instructions on how to add these configurations for both iOS and Android platforms are provided below.


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



