---
title: Running Unit & UI Tests
description: Easily run Unit and UI tests for your iOS applications during builds. Improve app quality with Appcircle's testing features.
tags: [ios, mobile, testing, unit-test, ui-test]
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';
import Screenshot from '@site/src/components/Screenshot';
import NarrowImage from '@site/src/components/NarrowImage';

# Running iOS Unit & UI Tests

You can easily run your Unit and UI tests for your iOS applications during builds.

Unit tests usually test a piece of your code and confirm the code behaves as expected in certain conditions.

### Creating tests for iOS applications

Unit tests are created in Xcode using the XCTest framework. Test methods are stored in `XCTestCase` subclass.

You can create unit tests in Xcode using the **Test Navigator**. Open the **Test Navigator** and click on the + icon in the lower left corner. Select **New Unit Test Target**. You should see the bundle and the `XCTestCase` subclass created.

You can now use XCTAssert functions to test your models or other assets.

<Screenshot url='https://cdn.appcircle.io/docs/assets/14-01-iOS-Unit-Tests.jpg' />

### Performing iOS application tests in Appcircle

To run your tests during the build process, you can simply add the **Xcodebuild for Unit and UI Tests** step in your workflows.

Make sure the step is after the **Xcode Select** step and before **Export Build Artifacts**. You can optionally run a regular build afterwards by adding **Xcodebuild for Devices/Simulators** step after the **Xcodebuild for Unit and UI Tests** step.

See the following page on our documentation to learn more about adding new workflow steps:

<ContentRef url="/workflows">What are Workflows and How to Use Them?</ContentRef>

To learn more about **Xcodebuild for Unit and UI Tests** step, visit its source on Github:

https://github.com/appcircleio/appcircle-ios-test-component

### Getting test results

#### Code Signing Enabled Builds

If you have **Xcodebuild for Unit and UI Tests** step in your workflow, Unit & UI test results will be created along with the .ipa file in the **Export Build Artifacts** step. You can download test results in the same `.zip` archive and you will see the `test.xcresult.zip` file that includes test data.

#### Not Signed Builds

If you don't sign your builds, your test results will be included in the `xcarchive` file created during **Export Build Artifacts**. You can alternatively disable your build and sign steps in your workflow and get only test results without building or signing your application.

---

:::info

Optionally, you can use 3rd party tools like :link: [**XCParse**](https://github.com/ChargePoint/xcparse) or :link: [**XCTestHTMLReport**](https://github.com/TitouanVanBelle/XCTestHTMLReport) to view your test results in a more user-friendly way.

:::

### Generating Test Report

If you add [Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) to your workflow, Appcircle will show the result of your tests and code coverage with a clean UI.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-report-overview.png' />

You must add this component **after** the `Xcodebuild for Unit and UI Tests` so that it can parse test results. Your workflow should look like the below.

<Screenshot url="https://cdn.appcircle.io/docs/assets/ios-unit-test-workflow-overview.png" />

[Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) shows both test and coverage results. To show coverage results, you must enable **Code Coverage** in Xcode's scheme settings.

<Screenshot url='https://cdn.appcircle.io/docs/assets/test-reports4.png' />

:::warning

There's one important setting that you should change. If any workflow steps fail, Appcircle automatically skips other steps and jumps directly to the Export Build Artifacts step. However, it is possible that some of your tests may fail. **If Test Report Component doesn't run, reports will not be generated.** You should turn on the following toggles so that Test Report Component always runs whether your tests fail or pass.

- Always run this step even if the previous steps fail to **ON**
- Continue with the next step even if this step fails to **ON**

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/ios-unit-test-report-steps-on.png" />

### Showing Test Reports

Appcircle can show passing and failing tests in compact UI. If your tests generate artifacts, those artifacts are also displayed with your test cases.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-result-overview.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-workflow-ui-detail.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-workflow-coverage.png' />

## Automated Tests

Appcircle currently supports the following mobile automation testing tools:

- [Appium](/workflows/common-workflow-steps/#appium-server)
- [BrowserStack App Automate (XCUI)](/workflows/ios-specific-workflow-steps/browserstack-app-automation)
- [Maestro](/workflows/common-workflow-steps/maestro-cloud-upload)
- [Testinium](/workflows/common-workflow-steps/testinium)

Each service allows you to run your tests on real devices, and test scenarios can be started with the artifacts created on Appcircle. Rich reports can be managed by visiting the web site of each service.

However, if your tool supports producing the following test report formats, you can also see the test results on Appcircle. Appcircle's Test Report currently supports the following test and coverage formats:

**Test Format**

- Xcode 13+ `.xctest`
- JUnit `.xml`

**Coverage Format**

- JaCoCo `.xml`
- Cobertura `.xml`
- Lcov `lcov.info`

For example, BrowserStack allows you to [export test results](https://www.browserstack.com/docs/app-automate/xcuitest/view-test-reports) as JUnit. You can get the results of your tests and code coverage results from BrowserStack by using a simple bash script.

```bash
curl -u "$AC_BROWSERSTACK_USERNAME:$AC_BROWSERSTACK_ACCESS_KEY" \
--output $AC_OUTPUT_DIR/myreport.xml \
-X GET "https://api-cloud.browserstack.com/app-automate/espresso/v2/builds/$BUILD_ID/sessions/$SESSION_ID/report"

```

:::info

Appcircle's [**BrowserStack App Automate(XCUI)**](https://docs.appcircle.io/workflows/ios-specific-workflow-steps/browserstack-app-automation) step already parses JUnit Test reports. The above code sample is only given as an example.

:::
