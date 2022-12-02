---
title: Using Environment Variables in Android Projects
metaTitle: Using Environment Variables in Android Projects
metaDescription: Using Environment Variables in Android Projects
sidebar_position: 5
---

import ContentRef from '@site/src/components/ContentRef';

# Using Environment Variables in Android Projects

Android developers can use environment variables using Gradle’s module-level build configuration. This module-level Gradle configuration file lets you specify build settings for that module of your application.

In the `android` block of your `build.gradle` file, specify a new `buildConfigField` method as shown below:

```groovy title="build.gradle"
android {
   defaultConfig {
       // Create a new variable here to be used in your code
       buildConfigField "String", "APPCIRCLE_API_URL", "\"${System.env.AC_API_URL}\""
   }
}
```

During the build process, Gradle will generate the `buildConfig` class and these variables will be accessible from your application in runtime.

You can now use this variable in your application. Here is an example showing how to use the variable in a view:

```java
public class SampleFragmentDetail extends Fragment {
   @Override
   public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
       // Use your BuildConfig variable in your view
       appVersionTextView.setText("Api URL: " + BuildConfig.APPCIRCLE_API_URL);
       return view;
   }
}

```

### Creating Environment Variables in Appcircle and using them in Android builds

Appcircle allows you to create groups of environment variables to be used during your builds. You can create environment variable groups for different branches of your project like development, staging, and production.

<ContentRef url="/environment-variables/managing-variables">Managing Variables</ContentRef>

Going forward on our sample above, you may want to use different API endpoints for development, staging, and production.

To create different values of the same variable, simply create an environment variable group for each branch:

![](<https://cdn.appcircle.io/docs/assets/image (76).png>)

Create an environment variable with the same name in each group and set the proper values for each branch.

![](<https://cdn.appcircle.io/docs/assets/image (80).png>)

Don’t forget to tell your build configuration to use the proper environment variable group during the build process:

![](<https://cdn.appcircle.io/docs/assets/image (172).png>)

Appcircle will use the values from the environment variables from the designated group for the branch you are building your application from.;

During the build process, `build.gradle` file in your module will use the values from the environment variables and your application will use these values during the runtime:
