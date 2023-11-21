# Enterprise App Store

If you want to distribute your in-house applications to your users, you may use Appcircle's Enterprise Store. Appcircle's Enterprise store helps you to set up your own store and have full control over deployment and access management. 

### Prerequisites

In order for your users to download IPA or APK files, those files must be signed with proper certificates or Keystore files. 

Android apps can be signed with any Keystore if the user's device allows installing apps from other sources.

Although iOS apps can be signed with Ad-Hoc provisioning profiles for in-house distribution, this type of distribution is limited to 100 devices per year. Once you hit that limit, you need to wait a year to reset your device limit. You also need to add the UUID of your users' device to Apple's Developer website. Therefore, Ad-Hoc distribution is intended for internal developer team members. 

If you have more than 100 users and don't want to deal with device enrollment, you need to use sign your apps with Enterprise Certificate. Please check the Apple's Enterprise program for more information.

https://developer.apple.com/programs/enterprise/