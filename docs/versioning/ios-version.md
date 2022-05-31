---
title: iOS Versioning
metaTitle: iOS Versioning
metaDescription: iOS Versioning
sidebar_position: 1
---

import ContentRef from '@site/src/components/ContentRef';
import VersionPlayground from '@site/src/components/VersionPlayground';

## Enabling Version Management

In order to manage build and version numbers with Appcircle, two requirements must be met:

- The build or Version Management toggle must be turned on and required input values must be entered
- **Increment Build and Version Number** component 2.0.* or higher must be in your workflow

![](<https://cdn.appcircle.io/docs/assets/ios-versioning1.png>)
![](<https://cdn.appcircle.io/docs/assets/ios-versioning2.png>)

The Versioning tab manages the input values of the component. It is not recommended to change the values of the component with the workflow editor. Instead, it would be best if you always used the Versioning UI to manage the settings.

### Managing Build Number
The versioning system needs a build number source and an offset to calculate the new build number. There are two source types for the build number. 


**Build Number Source**

- Environment Variable
- Xcode

If you select **Environment Variable**, you need to write the source environment variable into `Build Number`. The default value for this input is `$AC_BUILD_NUMBER`. This variable increases after every build. You can also use other environment variables that you create or select from the config screen. Environment variables must start with the `$` sign.

If you select Xcode, the build number will be read from the given Xcode project. Archive configuration and the first app target will be used to read that value from the plist file. If you want to use different configurations or targets, please set them in the **Advanced Settings** section.

**Offset**

If you select `$AC_BUILD_NUMBER` as your build number source, the build number in your project can be different. To synchronize build numbers, you can use the offset. The offset value is a number to be added or subtracted from the *Build Number Source*. Negative values can be written such as -10.

### Managing Version Number
The versioning system needs a version number source and an offset to calculate the new version number. There are three source types for the build number. 


**Version Number Source**

- Environment Variable
- Xcode
- App Store

If you select Environment Variable, you need to write the source environment variable into `Version Number` You can use any environment variable that you create or select from the config screen. Environment variables must start with the `$` sign.

If you select Xcode, the version number will be read from the given Xcode project. Archive configuration and the first app target will be used to read that value from the plist file. If you want to use different configurations or targets, please set them with Advanced settings.

The App Store option allows you to get the version number from the App Store directly. If you select App Store, the bundle id of your application must be entered. If your app is only available in selected countries, you must also enter an optional country code, ex: `us`

Please be aware that selecting this option is not a foolproof method. App Store endpoint may not be available during your build due to network issues or App Store instabilities.

**Offset**

To synchronize version numbers, you can use the offset. The offset value is a number to be added or subtracted from the *Version Number Source*. Negative values can be written such as -10.

**Increment**

You can increase the major, minor, or patch value of the build number. For version number 2.5.1, values can be summarized below.

|Part |Value|
|-----|-----|
|Major|  2  |
|Minor|  5  |
|Patch|  1  |

**Omit Zero Patch Version**

If true, omits zero in the patch version. So *42.10.0* will become *42.10* and *42.10.1* will remain *42.10.1*. The default is false.

### Advanced Settings

![](<https://cdn.appcircle.io/docs/assets/ios-versioning3.png>)

This component updates all runnable targets. If you only want to update selected targets, enable the `MANUALLY SELECTED TARGETS` option and write the targets' names. 

The versioning system will update the project's build or version number according to the target's release configuration. If you want to use another `xcconfig` please enable the `MANUALLY SELECTED XCCONFIG` toggle and write the name of the `xcconfig`.

### Output Values
After the build or version number update, new values will be written to two environment variables. 

|Value |Explanation|
|-----|-----|
|`$AC_IOS_NEW_BUILD_NUMBER`| Changed build number|
|`$AC_IOS_NEW_VERSION_NUMBER`| Changed version number|

You can use the above values in the remaining steps of your workflow. 

### Best Practices

The versioning system works by consuming environment variables. Even though it's easier to configure it by using UI, sometimes you may want to change them on the fly. Your commit messages or tags can be used to override those settings. The name of the variables and expected values can be found below.

|Value |Explanation|
|-----|-----|
|`$AC_BUILD_NUMBER_SOURCE`| Build number source type(env,xcode)|
|`$AC_IOS_BUILD_NUMBER`| Build number to set. If `$AC_BUILD_NUMBER_SOURCE` is set to xcode, this variable will be read from the project|
|`$AC_BUILD_OFFSET` | The number to be added or subtracted from the `$AC_IOS_BUILD_NUMBER`|
|`$AC_VERSION_NUMBER_SOURCE` | Version number source type(env,xcode,appstore)|
|`$AC_IOS_VERSION_NUMBER` | Version number to set. If `$AC_VERSION_NUMBER_SOURCE` is set to xcode, this variable will be read from the project|
|`$AC_VERSION_STRATEGY` | Version Increment Strategy|
|`$AC_VERSION_OFFSET` | The number to be added or subtracted from the `$AC_IOS_VERSION_NUMBER`|
|`$AC_IOS_CONFIGURATION_NAME` | Xcode Configuration to extract build number and version number|
|`$AC_TARGETS` | Name of the targets to update|
|`$AC_OMIT_ZERO_PATCH_VERSION` | If true omits zero in patch version|
|`$AC_BUNDLE_ID` | If the build number source is appstore, this variable should have the bundle id of your application.|
|`$AC_APPSTORE_COUNTRY` | If the build Number source is appstore and the app is only available in some countries, set the country code. Ex. us|


Since you can use any environment variables for the build and version numbers, you can consume Appcircle's various environment variables during the build. Appcircle gives plenty of information related to your repo and project. 

Let's see a couple of ways to utilize those values.

**Using Commit Messages**

We can extract the commit message and set the version number from the message. Commit message is stored inside `$AC_COMMIT_MESSAGE`. Let's say we want to use the version number from the commit message. Let's assume that the commit message is `[VERSION] 1.2.3` Since we will use a calculated value, we have to change our `$AC_VERSION_NUMBER_SOURCE` as well. We also set the offset value as 0 so that the calculated value can be applied directly. We can use the following custom script to extract this information.

```ruby
commit_message = ENV['AC_COMMIT_MESSAGE']
# extract commit message with regex
version = commit_message.match(/\[VERSION\] (.*)/)
if version
  version = version[1]
  open(ENV['AC_ENV_FILE_PATH'], 'a') { |f|
    f.puts "AC_VERSION_NUMBER_SOURCE=env"
    f.puts "AC_VERSION_OFFSET=0"
    f.puts "AC_IOS_VERSION_NUMBER=#{version}"
}
end
```

Just add this script as a custom script above the Increment iOS Version Component. The type of the script must be set as ruby.

**Using Tags**

It is also possible to extract the version number from the Git tags. The following example assumes that the commit has a single tag. If you tag your version with `release-1.2.3`, the following script will extract the version number from the tag. 

```ruby
commit_message = ENV['AC_COMMIT_TAGS']
version = commit_message.match(/release-(.*)/)
if version
  version = version[1]
  open(ENV['AC_ENV_FILE_PATH'], 'a') { |f|
    f.puts "AC_VERSION_NUMBER_SOURCE=env"
    f.puts "AC_VERSION_OFFSET=0"
    f.puts "AC_IOS_VERSION_NUMBER=#{version}"
}
end
```

### Versioning Playground

You can use the below playground to test the effect of different options

