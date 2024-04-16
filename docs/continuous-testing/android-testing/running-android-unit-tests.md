---
title: Running Unit Tests
description: Learn how to run unit tests for Android applications in Appcircle
tags: [unit tests, android, android unit tests, testing, continuous testing]
sidebar_position: 2
---

import Screenshot from '@site/src/components/Screenshot';
import ContentRef from '@site/src/components/ContentRef';

# Running Android Unit Tests

Application tests are essential when it comes to improving and maintaining product quality and performing routine checks which are difficult for humans to perform regularly.

Unit tests are usually considered first as they run really fast and are relatively easier to write and measure.

We will create a local unit test here as an example and show you how to run the test during your build process.

### Creating unit tests

First, please add test dependencies to your `build.gradle` file:

```groovy
dependencies {
    // Required for local unit tests (JUnit 4 framework)
    testImplementation 'junit:junit:4.12'
}
```

Create your test file in your project’s `module-name/src/test/java/` folder.

```java
package com.example.appcircle_sample_android;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Example local unit test, which will execute on the development machine (host).
 *
 * @see <a href="http://d.android.com/tools/testing">Testing documentation</a>
 */
public class URLValidatorUnitTest {

    @Test
    public void invalid_url_test() {
        boolean isValid = URLValidator.isValid("http:/www.google.com");
        assertFalse(isValid);
    }

    @Test
    public void valid_url_test() {
        boolean isValid = URLValidator.isValid("https://www.google.com");
        assertTrue(isValid);
    }
}
```

This example checks to see if the provided URL is valid.

### Running your unit tests in Appcircle

To run your unit test during the build process, you can simply use a custom script in your build profile.

Simply go to your build workflow and add a custom script after the **Sign Application** step.

See the following page on our documentation to learn more about creating custom workflow steps:

<ContentRef url="/workflows/common-workflow-steps/build-and-test/custom-script">Working with Custom Scripts</ContentRef>

Add the following Bash script to your custom script step:

```bash
cd $AC_REPOSITORY_DIR
./gradlew testRelease # or you can use 'testDebug'
mv app/build/reports/tests $AC_OUTPUT_DIR
mv app/build/test-results $AC_OUTPUT_DIR
```

This simple Bash script will trigger your unit test and output the test results to be packed along with your binary files. You will get the test results both in `xml` and `html` formats.

<Screenshot url='https://cdn.appcircle.io/docs/assets/Screenshot 2020-04-28 20.47.05.png' />

### Generating Test Report

Appcircle has [Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) which can show the result of your tests and code coverage in a beautiful UI.

<Screenshot url="https://cdn.appcircle.io/docs/assets/android-unit-test-report-overview.png" />

You must add this component **after** running your tests so that it can parse test results. Your workflow should look like the below.

<Screenshot url="https://cdn.appcircle.io/docs/assets/android-unit-test-workflow.png" />

[Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) shows both test and coverage results. This component supports the following Test and Coverage Formats

- Xcode
- JUnit
- JaCoCo
- Cobertura
- lcov.info

You must configure the **Test Report Component** and enter the path of code coverage and test results paths. For example, if you run your tests with an emulator, your files will be generated in the following folders.

- **Code Coverage Files:** `$AC_COVERAGE_RESULT_PATH`
- **Test Results:** `$AC_OUTPUT_DIR/test-results`

You must configure the component to parse those folders.

<Screenshot url="https://cdn.appcircle.io/docs/assets/android-unit-test-report-workflow.png" />

:::warning

There's one important setting that you should change. If any workflow steps fail, Appcircle automatically skips other steps and jumps directly to the Export Build Artifacts step. However, it is possible that some of your tests may fail. **If Test Report Component doesn't run, reports will not be generated.** You should turn on the following toggles so that Test Report Component always runs whether your tests fail or pass.

- Always run this step even if the previous steps fail to **ON**
- Continue with the next step even if this step fails to **ON**

:::

<Screenshot url="https://cdn.appcircle.io/docs/assets/android-unit-test-report-steps-on.png" />

:::caution

If you're using UI tests with emulators, you must select an Intel device (**Default Intel Pool**) since M1 virtual machines (**Default M1 Pool**) don't support nested virtualization. Unit tests can work for both pools.

:::

### Showing Test Reports

Appcircle can show passing and failing tests in compact UI. If your tests generate artifacts, those artifacts are also displayed with your test cases.

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-result-overview.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-workflow-ui-detail.png' />

<Screenshot url='https://cdn.appcircle.io/docs/assets/ios-unit-test-workflow-coverage.png' />

## Automated Tests

Appcircle currently supports the following mobile automation testing tools:

- [Appium](/workflows/common-workflow-steps/#appium-server)
- [BrowserStack App Automate - Espresso](/workflows/android-specific-workflow-steps/distribution/browserstack-app-automate-espresso)
- [Maestro](/workflows/common-workflow-steps/#maestro-cloud-upload)
- [Testinium](/workflows/common-workflow-steps/#testinium)

Each service allows you to run your tests on real devices, and test scenarios can be started with the artifacts created on Appcircle. Rich reports can be managed by visiting the web site of each service.

However, if your tool supports producing the following test report formats, you can also see the test results on Appcircle. Appcircle's Test Report currently supports the following test and coverage formats:

**Test Format**

- Xcode 13+ `.xctest`
- JUnit `.xml`

**Coverage Format**

- JaCoCo `.xml`
- Cobertura `.xml`
- Lcov `lcov.info`

For example, BrowserStack allows you to [export test results](https://www.browserstack.com/docs/app-automate/espresso/view-test-reports) as JUnit. You can get the results of your tests and code coverage results from BrowserStack by using a simple bash script.

```bash
curl -u "$AC_BROWSERSTACK_USERNAME:$AC_BROWSERSTACK_ACCESS_KEY" \
--output $AC_OUTPUT_DIR/myreport.xml \
-X GET "https://api-cloud.browserstack.com/app-automate/espresso/v2/builds/$BUILD_ID/sessions/$SESSION_ID/report"

```

:::info

Appcircle's [**BrowserStack App Automate - Espresso**](/workflows/android-specific-workflow-steps/distribution/browserstack-app-automate-espresso) step already parses JUnit Test reports. The above code sample is only given as an example.

:::
