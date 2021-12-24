---
title: "Getting Started With Appcircle"
metaTitle: Getting Started With Appcircle"
metaDescription: "Getting Started With Appcircle"
sidebar_position: 2
---
# Getting Started With Appcircle

Appcircle is a mobile CI/CD platform which makes it easy for you to manage the lifecycle of your mobile applications.

:::tip

Appcircle supports mobile applications developed in Swift/Objective-C, Java/Kotlin, React Native, Flutter and Smartface for both iOS and Android.

:::

Before going through with the documentation, you can also view the following introductory video about Appcircle:

{% embed url="https://www.youtube.com/watch?v=OUoZFGqJFdM" %}
Appcircle Introduction: Build -> Sign -> Distribute -> Preview on the Emulator
{% endembed %}



A basic lifecycle of a mobile application can be broken down into 5 steps:



### Create or Add Signing Identities

Your mobile applications must be digitally signed to be able to distributed, tested and, submitted to app stores.

For iOS applications, you must have a signing certificate and provisioning profiles to be able to run your application on real devices and submit them to Apple Appstore.&#x20;

{% content-ref url="signing-identities/ios-certificates-and-provisioning-profiles.md" %}
[ios-certificates-and-provisioning-profiles.md](signing-identities/ios-certificates-and-provisioning-profiles.md)
{% endcontent-ref %}



For Android applications, you need to create a keystore file to sign your applications digitally.

{% content-ref url="signing-identities/android-keystores.md" %}
[android-keystores.md](signing-identities/android-keystores.md)
{% endcontent-ref %}

###

### Create Building Profiles

Building your mobile applications is very easy with Appcircle no matter what platform and language you are using. You can connect your repositories from GitHub, Bitbucket, or GitLab to Appcircle.

You can also connect to public repositories directly or use SSH for custom repository connections. If you want to try out Appcircle, you can find sample apps for different frameworks in [Appcircle GitHub](https://github.com/appcircleio?q=sample).&#x20;

Appcircle will fetch all your branches and commits in your repository and lets you build any commit you want to test your application.

{% content-ref url="build/adding-a-build-profile/" %}
[adding-a-build-profile](build/adding-a-build-profile/)
{% endcontent-ref %}



Configure your build profile and select project parameters, signing options, distribution profiles and environment variables. Your project will be built using these settings and options.

{% content-ref url="build/build-profile-configuration.md" %}
[build-profile-configuration.md](build/build-profile-configuration.md)
{% endcontent-ref %}



You can customize your build flow using our workflow editor. Workflow editor allows you to be in control of the build process. You can add or remove build steps, add your custom scripts for advanced build processes.

{% content-ref url="workflows/why-to-use-workflows.md" %}
[why-to-use-workflows.md](workflows/why-to-use-workflows.md)
{% endcontent-ref %}



You can also automate your build process by telling Appcircle to automatically build your code with every push to your repository. There are also options including tagged pushes for more advanced cases.

{% content-ref url="build/build-manually-or-with-triggers.md" %}
[build-manually-or-with-triggers.md](build/build-manually-or-with-triggers.md)
{% endcontent-ref %}

###

### Distribute Your Applications

Distribution is a very major and important step for testing and deploying a mobile application.&#x20;

You can use Preview On Device feature to simulate your app on a real device and see how everything works.&#x20;

{% content-ref url="distribute/preview-on-device.md" %}
[preview-on-device.md](distribute/preview-on-device.md)
{% endcontent-ref %}



Create testing groups, add testers to testing groups and assign these groups to distribution profiles to distribute your build to testers so that they can download and install applications on their devices.

{% content-ref url="distribute/testing-groups.md" %}
[testing-groups.md](distribute/testing-groups.md)
{% endcontent-ref %}



If you have a team of testers, you can create testing groups and distribute builds to your testers manually or automatically after each build and let them run the application on their mobile devices.

{% content-ref url="distribute/create-or-select-a-distribution-profile.md" %}
[create-or-select-a-distribution-profile.md](distribute/create-or-select-a-distribution-profile.md)
{% endcontent-ref %}

&#x20;

### Submit to the Public App Stores

:tools: This feature is coming soon!
