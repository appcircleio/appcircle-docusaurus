---
title: Custom Script FAQ
metaTitle: Custom Script FAQ
metaDescription: Custom Script FAQ
sidebar_position: 1
---
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

# Custom Script FAQ

### How to install a new package to the build machine?

You can use the compatible package managers to install packages.

For the macOS build machines for iOS builds, _brew _is a commonly used package manager with commands like `brew install maven`

For the Linux (Debian) build machines for Android builds, _apt-get_ can be used for 3rd party packages such as `apt-get -y install maven`



### How to change the package name/application ID dynamically?

With custom scripts, you can edit the Info.plist and the build.gradle files.

<Tabs>
  <TabItem value="ios" label="iOS" default>

   ```bash title="iOS sample for Info.plist"
cd $AC_REPOSITORY_DIR/Your-Target-Folder
/usr/libexec/PlistBuddy -c "Set :CFBundleIdentifier io.myapp" "./Info.plist"
```

  </TabItem>
  <TabItem value="android" label="Android">

```bash title="Android sample for build.gradle"
cd $AC_REPOSITORY_DIR/app
sed -i '' 's/old-value/new-value/g' build.gradle
```

  </TabItem>
</Tabs>

### How to access a file in the repository directory?

For each step in the workflow, you can view the input and output variables in the step configuration.

The repository directory is an output of the Git Clone step and its patch can be accessed with the `AC_REPOSITORY_PATH` environment variable by any step added after the Git Clone step. An example is as follows:


```bash
cd $AC_REPOSITORY_DIR
cat README
```



### How to a add a file as a downloadable build artifact?

You can add any file to the output directory that contain the build artifacts using the `AC_OUTPUT_DIR` environment variable. An example is as follows:


```bash
cd $AC_REPOSITORY_DIR/app/build/reports/
mv lint-results* $AC_OUTPUT_DIR/
```

