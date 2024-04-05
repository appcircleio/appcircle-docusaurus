---
title: iOS Builds
metaTitle: Using Environment Variables in iOS Projects
metaDescription: Using Environment Variables in iOS Projects
sidebar_position: 4
---

import ContentRef from '@site/src/components/ContentRef';
import Screenshot from '@site/src/components/Screenshot';

# Using Environment Variables in iOS Projects

We strongly recommend using environment variables if you need to use sensitive or variable data in your projects. Using sensitive data such as API keys and passwords may cause security flaws or keeping frequently changing variables may increase your development time.

### Xcode configuration files

Xcode allows you to create build configuration files commonly known as `xcconfig` files. These files can hold key/value pairs for your project-wide variables. Once you create these configuration variables, you can then use Appcircle's custom script workflow steps to replace them with the environment variables you create in Appcircle.

### Creating Xcode build configuration files

Simply create a new file by selecting **File > New** from Xcode menu and choose **Configuration Settings File** under **Other** section in the Xcode window.

<Screenshot url='https://cdn.appcircle.io/docs/assets/env-var-ios-02.jpg' />

Once you create your `.xcconfig` file, you can now assign it to your targets in Configurations window:

<Screenshot url='https://cdn.appcircle.io/docs/assets/env-var-ios-03.jpg' />

### Adding variables into build configuration file

You can now add your project-wide variables into the `.xcconfig` file:

```swift
// Application name
APPLICATION_NAME = Appcircle
// API endpoint
API_URL = api.appcircle.io
```

:::info

Please note that Xcode will treat double slashes // as comment delimiters even if it’s a URL. That’s why you may exclude the `https://` portion of your URLs or use different symbols to be replaced later in your code.

:::

### Using different values for different stages

You may want to use different values of the same environment variables for different stages of your application. For example, an API endpoint may need to be different for the development and production stages.

Xcode allows you to include and inherit build configuration files and use different configuration files for different targets of your project.;

Here's a sample code showing importing the main `config.xcconfig` file into a `development.xcconfig` file and alter the value of a variable:

```swift
// include the main xcconfig file
#include "path/to/Config.xcconfig"

// Development.xcconfig
APPLICATION_NAME = $(inherited) DEV

```

### Accessing build configuration values from your project

Now that we have our build configuration files ready, we need to tell our project to use the values from these files for certain variables.;

Xcode’s Info tab in the configuration window refers to the target’s `info.plist` file, which is compiled during the build process into the application bundle. Here, by simply adding a reference to the `$(API_URL)` variable, you can access its value from your bundle.

<Screenshot url='https://cdn.appcircle.io/docs/assets/env-var-ios-04.jpg' />

Final step in Xcode will be calling the variables from your code's view controller:

```swift
- (void)viewDidLoad {
    [super viewDidLoad];

    self.lblVersion.text =  [NSString stringWithFormat:@"v%@",[[NSBundle mainBundle] objectForInfoDictionaryKey:@"CFBundleShortVersionString"]];
    self.lblApi.text = [NSString stringWithFormat:@"Api URL: %@\nApi KEY: %@",[[NSBundle mainBundle] objectForInfoDictionaryKey:@"API_URL"],[[NSBundle mainBundle] objectForInfoDictionaryKey:@"API_KEY"]];
}

```

### Replacing configuration settings values with environment variables

You can create environment variable groups and key/value pairs in these groups. To learn more about creating environment variables in Appcircle please see the following page:

<ContentRef url="/environment-variables/managing-variables">Managing Variables</ContentRef>

Once you update your project with `.xcconfig` files, you can create environment variable groups and include different values of the same environment variable to be used in different stages of your application like development or production.

<Screenshot url='https://cdn.appcircle.io/docs/assets/env-var-multi-dev.png' />

To be able to use these variables in your project, we need to replace the values in our `.xcconfig` file using a custom script workflow step. To get more information about creating and using custom scripts, please check the following page:

<ContentRef url="/workflows/common-workflow-steps/build-and-test/custom-script">Working with Custom Scripts</ContentRef>

In our example here, we will use a Bash script to replace the values in our .xcconfig file.;

```bash
echo "API_URL : ${API_URL}"
echo "API_KEY : ${API_KEY}"
bash $AC_REPOSITORY_DIR/Appcircle/environment.sh $AC_REPOSITORY_DIR/Appcircle/development.xcconfig
```

During the build process, this Bash script will replace the values in the .xcconfig file with the environment variables created earlier.
