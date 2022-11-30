---
title: Running Android Unit Tests
metaTitle: Running Android Unit Tests
metaDescription: Running Android Unit Tests
sidebar_position: 2
---

import ContentRef from '@site/src/components/ContentRef';
import NarrowImage from '@site/src/components/NarrowImage';

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

<ContentRef url="/integrations/working-with-custom-scripts">Working with Custom Scripts</ContentRef>

Add the following Bash script to your custom script step:

```bash
set -ex
cd $AC_REPOSITORY_DIR
./gradlew test
mv app/build/reports/tests $AC_OUTPUT_DIR
mv app/build/test-results $AC_OUTPUT_DIR
```

This simple Bash script will trigger your unit test and output the test results to be packed along with your binary files. You will get the test results both in `xml` and `html` formats.

![](<https://cdn.appcircle.io/docs/assets/Screenshot 2020-04-28 20.47.05.png>)

### Generating Test Report

Appcircle has [Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) which can show the result of your tests and code coverage in a beautiful UI.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/test-reports1.png" />

You must add this component **after** running your tests so that it can parse test results. Your workflow should look like the below.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/test-reports8.png" />

[Test Report Component](https://github.com/appcircleio/appcircle-test-report-component) shows both test and coverage results. This component supports the following Test and Coverage Formats

- Xcode
- JUnit
- JaCoCo
- Cobertura
- lcov.info

You must configure the **Test Report Component** and enter the path of code coverage and test results paths. For example, if you run your tests with an emulator, your files will be generated in the following folders.

- **Code Coverage Files:** $AC_REPOSITORY_DIR/app/build/reports/coverage/androidTest/debug/connected/
- **Test Results:** $AC_REPOSITORY_DIR/app/build/outputs/androidTest-results/connected/

You must configure the component to parse those folders.

<NarrowImage src="https://cdn.appcircle.io/docs/assets/test-reports9.png" />

:::warning

There's one important setting that you should change. If any workflow steps fail, Appcircle automatically skips other steps and jumps directly to the Export Build Artifacts step. However, some of your tests may fail. If Test Report Component doesn't run, reports will not be generated. You should turn on the following toggles so that Test Report Component always runs whether your tests fail or pass.

- Always run this step even if the previous steps fail 
- Continue with the next step even if this step fails

:::

<NarrowImage src="https://cdn.appcircle.io/docs/assets/test-reports3.png" />

:::caution

If you're using UI Tests with Emulators, you must select Intel Device since M1 Virtual Machines don't support nested virtualization. 

:::

### Showing Test Reports

Appcircle can show passing and failing tests in compact UI. If your tests generate artifacts, those artifacts are also displayed with your test cases.

![](https://cdn.appcircle.io/docs/assets/test-reports5.png)

![](https://cdn.appcircle.io/docs/assets/test-reports6.png)

![](https://cdn.appcircle.io/docs/assets/test-reports7.png)
