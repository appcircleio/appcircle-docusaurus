---
title: Running Android Unit Tests
metaTitle: Running Android Unit Tests
metaDescription: Running Android Unit Tests
sidebar_position: 2
---

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
