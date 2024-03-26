---
title: Automated Tests
metaTitle: Automated Tests
metaDescription: Automated Tests
sidebar_position: 5
---

import ContentRef from '@site/src/components/ContentRef';
import NarrowImage from '@site/src/components/NarrowImage';

# Automated Tests

Appcircle currently supports the following mobile automation testing tools:

- [Appium](../workflows/common-workflow-steps/index.md#appium-server)
- [BrowserStack](../workflows/android-specific-workflow-steps/index.md#browserstack-app-automate---espresso)
- [Maestro](../workflows/common-workflow-steps/index.md#maestro-cloud-upload)
- [Testinium](../workflows/common-workflow-steps/index.md#testinium)

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

Appcircle's BrowserStack App Automate - Espresso step already parses JUnit Test reports. The above code sample is only given as an example.

:::

The [Test Report Step](../continuous-testing/running-android-unit-tests.md) only requires a path for the test and code coverage results. For the above example, it is `$AC_OUTPUT_DIR/myreport.xml`. If you want to see your tests results on Appcircle, you need to create compatible test and code covarage results on Appcircle.