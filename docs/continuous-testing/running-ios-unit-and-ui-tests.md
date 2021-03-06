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

We will use a Ruby script here to tell Appcircle to run our unit and UI tests.

```ruby
# Instal dependencies
require 'open3'
require 'pathname'

# Check & validate Enviroment Variables
def env_has_key(key)
	return (ENV[key] != nil && ENV[key] !="") ? ENV[key] : abort("Missing #{key}.")
end

$project_path = ENV["AC_PROJECT"] || abort('Missing project path.')
$repository_path = ENV["AC_REPOSITORY_DIR"]
$project_full_path = $repository_path ? (Pathname.new $repository_path).join($project_path) : $project_path
$scheme = env_has_key("AC_SCHEME")
$output_path = env_has_key("AC_OUTPUT_DIR")
$test_result_path = "#{$output_path}/test.xcresult"

# Create a function to run test commands
def run_command(command, skip_abort)
  puts "@[command] #{command}"
  status = nil
  stdout_str = nil
  stderr_str = nil
  Open3.popen3(command) do |stdin, stdout, stderr, wait_thr|
    stdout.each_line do |line|
      puts line
    end
    stdout_str = stdout.read
    stderr_str = stderr.read
    status = wait_thr.value
  end
  unless status.success?
    puts stderr_str
    unless skip_abort
      exit 1
    end
  end
end

# Command to tell Xcode to run tests with parameters
command_xcodebuild_test = "xcodebuild -project #{$project_full_path} -scheme #{$scheme} -destination 'platform=iOS Simulator,name=iPhone 11,OS=latest' -resultBundlePath #{$test_result_path} test COMPILER_INDEX_STORE_ENABLE=NO"

# Run our function and perform the tests
run_command(command_xcodebuild_test,false)

exit 0
```

### Getting test results

Unit & UI test results will be packed along with the `.ipa` file generated after the build if you also sign your artifact using your provisioning profile. You can download test results in the same `.zip` archive and you will see the `test.xcresult.zip` file that includes test data.

If you don't sign your build artifact, your test results will be included in the `xcarchive` file. You can alternatively disable your build and sign steps in your workflow and get only test results without building or signing your application.

You can use 3rd party tools like :link: [**XCParse**](https://github.com/ChargePoint/xcparse) or :link: [**XCTestHTMLReport**](https://github.com/TitouanVanBelle/XCTestHTMLReport) to view your test results in a more user-friendly way.
