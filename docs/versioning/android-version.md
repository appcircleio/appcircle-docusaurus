---
title: Android Versioning
metaTitle: Android Versioning
metaDescription: Android Versioning
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';
import VersionPlayground from '@site/src/components/VersionPlayground';
import Screenshot from '@site/src/components/Screenshot';

## Enabling Version Management

In order to manage version code and version name with Appcircle, two requirements must be met:

- The build's Version Management toggle must be turned on and required input values must be entered
- **Increment Build and Version Number** component 1.0.* or higher must be in your workflow

<Screenshot url="https://cdn.appcircle.io/docs/assets/versioning-android-configuration.png" />
<Screenshot url="https://cdn.appcircle.io/docs/assets/versioning-android-workflow.png" />

The Versioning tab manages the input values of the component. It is not recommended to change the values of the component with the workflow editor. Instead, it would be best if you always used the Versioning UI to manage the settings.

:::caution

Gradle files are written in Groovy language. Therefore it can use functions or environment variables during the build. This component doesn't cover all the edge cases. Please test your workflow thoroughly and make sure that it works as intended. 

:::



### Managing Version Code
The versioning system needs a version code source and an offset to calculate the new version code. There are two source types for the version code. 


**Version Code Source**

- Environment Variable
- Gradle

If you select **Environment Variable**, you need to write the source environment variable into `Version Code`. The default value for this input is `$AC_BUILD_NUMBER`. This variable increases after every build. You can also use other environment variables that you create or select from the config screen. Environment variables must start with the `$` sign.

If you select Gradle, the version code will be read from build.gradle file. If you want to use different flavor, please set them in the **Advanced Settings** section.

**Offset**

If you select `$AC_BUILD_NUMBER` as your version code source, the version code in your project can be different. To synchronize version code, you can use the offset. The offset value is a number to be added or subtracted from the *Version Code Source*. Negative values can be written such as -10.

### Managing Version Name
The versioning system needs a version name source and an offset to calculate the new version name. There are two source types for the version name. 

**Version Name Source**

- Environment Variable
- Gradle

If you select Environment Variable, you need to write the source environment variable into `Version Name` You can use any environment variable that you create or select from the config screen. Environment variables must start with the `$` sign.

If you select Gradle, the version name will be read from the given Android project. 

**Offset**

To synchronize version names, you can use the offset. The offset value is a number to be added or subtracted from the *Version Name Source*. Negative values can be written such as -10.

**Increment**

You can increase the major, minor, or patch value of the version name. For version name 2.5.1, values can be summarized below.

|Part |Value|
|-----|-----|
|Major|  2  |
|Minor|  5  |
|Patch|  1  |

**Omit Zero Patch Version**

If true, omits zero in the patch version. So *42.10.0* will become *42.10* and *42.10.1* will remain *42.10.1*. The default is false.

### Advanced Settings

This component works on standard build.gradle files. If you use flavors in your build.gradle, you can set the flavor name. However, please be aware that flavor support is not foolproof. Due to dynamic nature of build.gradle file, it may not cover all the cases. 

### Output Values
After the version code or version name update, new values will be written to two environment variables. 

|Value |Explanation|
|-----|-----|
|`$AC_ANDROID_NEW_BUILD_NUMBER`| Changed version code|
|`$AC_ANDROID_NEW_VERSION_NUMBER`| Changed version name|

You can use the above values in the remaining steps of your workflow. 

### Best Practices

The versioning system works by consuming environment variables. Even though it's easier to configure it by using UI, sometimes you may want to change them on the fly. Your commit messages or tags can be used to override those settings. The name of the variables and expected values can be found below.

|Value |Explanation|
|-----|-----|
|`$AC_BUILD_NUMBER_SOURCE`| Version code source type(env,gradle)|
|`$AC_ANDROID_BUILD_NUMBER`| Version code to set. If `$AC_BUILD_NUMBER_SOURCE` is set to gradle, this variable will be read from the project|
|`$AC_BUILD_OFFSET` | The number to be added or subtracted from the `$AC_ANDROID_BUILD_NUMBER`|
|`$AC_VERSION_NUMBER_SOURCE` | Version name source type(env,gradle)|
|`$AC_ANDROID_VERSION_NUMBER` | Version name to set. If `$AC_VERSION_NUMBER_SOURCE` is set to gradle, this variable will be read from the project|
|`$AC_VERSION_STRATEGY` | Version Increment Strategy|
|`$AC_VERSION_OFFSET` | The number to be added or subtracted from the `$AC_ANDROID_VERSION_NUMBER`|
|`$AC_FLAVOR` | Build flavor|
|`$AC_OMIT_ZERO_PATCH_VERSION` | If true omits zero in patch version|


Since you can use any environment variables for the version code and version name, you can consume Appcircle's various environment variables during the build. Appcircle gives plenty of information related to your repo and project. 

Let's see a couple of ways to utilize those values.

**Using Commit Messages**

We can extract the commit message and set the version name from the message. Commit message is stored inside `$AC_COMMIT_MESSAGE`. Let's say we want to use the version name from the commit message. Let's assume that the commit message is `[VERSION] 1.2.3` Since we will use a calculated value, we have to change our `$AC_VERSION_NUMBER_SOURCE` as well. We also set the offset value as 0 so that the calculated value can be applied directly. We can use the following custom script to extract this information.

```ruby
commit_message = ENV['AC_COMMIT_MESSAGE']
# extract commit message with regex
version = commit_message.match(/\[VERSION\] (.*)/)
if version
  version = version[1]
  open(ENV['AC_ENV_FILE_PATH'], 'a') { |f|
    f.puts "AC_VERSION_NUMBER_SOURCE=env"
    f.puts "AC_VERSION_OFFSET=0"
    f.puts "AC_ANDROID_VERSION_NUMBER=#{version}"
}
end
```

Just add this script as a custom script above the Increment Android Version Component. The type of the script must be set as ruby.

**Using Tags**

It is also possible to extract the version name from the Git tags. The following example assumes that the commit has a single tag. If you tag your version with `release-1.2.3`, the following script will extract the version name from the tag. 

```ruby
commit_message = ENV['AC_COMMIT_TAGS']
version = commit_message.match(/release-(.*)/)
if version
  version = version[1]
  open(ENV['AC_ENV_FILE_PATH'], 'a') { |f|
    f.puts "AC_VERSION_NUMBER_SOURCE=env"
    f.puts "AC_VERSION_OFFSET=0"
    f.puts "AC_ANDROID_VERSION_NUMBER=#{version}"
}
end
```

### Versioning Playground

You can use the below playground to test the effect of different options

<VersionPlayground title="Version Code" subtitle="Version Name"/>