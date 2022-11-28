---
title: Running iOS Unit & UI Tests
metaTitle: Running iOS Unit & UI Tests
metaDescription: Running iOS Unit & UI Tests
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';

# Running iOS Unit & UI Tests

Appcircle helps you perform unit and UI tests for your iOS applications at once.

Unit tests usually test a piece of your code and confirm the code behaves as expected in certain conditions.

### Creating tests for iOS applications

Unit tests are created in Xcode using the XCTest framework. Test methods are stored in `XCTestCase` subclass.

You can create unit tests in Xcode using the **Test Navigator**. Open the **Test Navigator** and click on the + icon in the lower left corner. Select **New Unit Test Target**. You should see the bundle and the `XCTestCase` subclass created.

You can now use XCTAssert functions to test your models or other assets.

![](https://cdn.appcircle.io/docs/assets/14-01-iOS-Unit-Tests.jpg)

### Performing iOS application tests in Appcircle

To run your tests during the build process, you can simply use a custom script in your build profile.

Simply go to your build workflow and add a custom script after the **Xcode Select** step so that tests will be run before the actual build starts.

See the following page on our documentation to learn more about creating custom workflow steps:

<ContentRef url="/workflows/why-to-use-workflows">What are Workflows and How to Use Them?</ContentRef>

You can use Appcircle's Xcodebuild for Unit and UI Tests component to run your unit and UI tests.

https://github.com/appcircleio/appcircle-ios-test-component


### Getting test results

Unit & UI test results will be packed along with the `.ipa` file generated after the build if you also sign your artifact using your provisioning profile. You can download test results in the same `.zip` archive and you will see the `test.xcresult.zip` file that includes test data.

If you don't sign your build artifact, your test results will be included in the `xcarchive` file. You can alternatively disable your build and sign steps in your workflow and get only test results without building or signing your application.

You can use 3rd party tools like :link: [**XCParse**](https://github.com/ChargePoint/xcparse) or :link: [**XCTestHTMLReport**](https://github.com/TitouanVanBelle/XCTestHTMLReport) to view your test results in a more user-friendly way.

### Generating Test Report

Appcircle has [Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) which can show the result of your tests and code coverage in a beautiful UI.

![](https://cdn.appcircle.io/docs/assets/test-reports1.png)

You must add this component **after** the `Xcodebuild for Unit and UI Tests` so that it can parse test results. Your workflow should look like the below.

![](https://cdn.appcircle.io/docs/assets/test-reports2.png)

[Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) shows both test and coverage results. To show coverage results, you must enable **Code Coverage** in the scheme settings. 

![](https://cdn.appcircle.io/docs/assets/test-reports4.png)

:::warning

There's one important setting that you should change. If any workflow steps fail, Appcircle automatically skips other steps and jumps directly to the Export Build Artifacts step. However, it is possible that some of your tests may fail. If Test Report Component doesn't run, reports will not be generated. You should turn on the following toggles so that Test Report Component always runs whether your tests fail or pass.

- Always run this step even if the previous steps fail 
- Continue with the next step even if this step fails

:::

![](https://cdn.appcircle.io/docs/assets/test-reports3.png)

### Showing Test Reports

Appcircle can show passing and failing tests in compact UI. If your tests generate artifacts, those artifacts are also displayed with your test cases.

![](https://cdn.appcircle.io/docs/assets/test-reports5.png)

![](https://cdn.appcircle.io/docs/assets/test-reports6.png)

![](https://cdn.appcircle.io/docs/assets/test-reports7.png)
