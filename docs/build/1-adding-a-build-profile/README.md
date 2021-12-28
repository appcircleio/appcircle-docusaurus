---
title: 'Adding a Build Profile & Connecting a Repository'
metaTitle: 'Adding a Build Profile & Connecting a Repository'
metaDescription: 'Adding a Build Profile & Connecting a Repository'
---

# Adding a Build Profile & Connecting a Repository

New to Appcircle Build module? Follow our quick start guide to build your iOS and Android apps in the cloud.

The Build Module allows you to streamline and automate your mobile app build flows.

:::info

The Build Module is the first step to automate your CI/CD processes via Appcircle.

:::

## Create a build profile (app)

A build profile is an app that you can build in a target OS and framework.&#x20;

To create your first build profile, click on the orange "Add New" button on the top left of the screen.

![](<https://cdn.appcircle.io/docs/assets/01-01-Adding-A-Build-Profile (2).jpg>)

Enter a name for your build profile and select the target operating system (iOS or Android) and target platform.

![](<https://cdn.appcircle.io/docs/assets/image (224).png>)

## Connect your repository

You can connect GitHub through a GitHub app or Bitbucket and GitLab repositories to your build profile through OAuth apps. Alternatively, You can connect private repositories through SSH and public repositories directly on GitHub, Bitbucket, GitLab, and other compatible git providers such as Azure DevOps and AWS CodeCommit. ([Please refer here for more information on AWS CodeCommit connections.](../../troubleshooting-faq/common-issues#how-to-connect-to-aws-codecommit-repositories-through-ssh))

You can also connect to your Self Hosted Bitbucket and GitLab account directly within Appcircle.

If you authorize Appcircle to connect to your Github, BitBucket, or GitLab account, you can auto-build your project with hooks, get build statuses and the full list of commits. If you connect to a repository through SSH or through a public URL, you need to [set up webhooks manually](../build-manually-or-with-triggers#setting-up-manual-webhooks-for-ssh-and-public-repositories).

To test drive Appcircle, you can find various sample projects in the [Appcircle GitHub page](https://github.com/appcircleio?q=sample) or you can just press on the **Quick start using the sample repository** button to populate the repository URL field with a compatible project based on the selected framework.

![](<https://cdn.appcircle.io/docs/assets/image (233).png>)

Refer to the relative documents under this page about the connections and differences between connection types:

- [Connect to GitHub](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-github)
- [Connect to Bitbucket](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-bitbucket)
- [Connect to GitLab](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-gitlab)
- [Connect to Private Repository via SSH Key](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-private-repository-via-ssh)
- [Connect to Public Repository](https://docs.appcircle.io/build/adding-a-build-profile/connecting-to-public-repository)

## View the newly created build profile

You will see your build profile once it has been created. Click on the build profile to connect a repository and fetch your code to Appcircle.

Appcircle will then pull your branches, commits, and other information from your repository.

![](<https://cdn.appcircle.io/docs/assets/image (244).png>)

![](<https://cdn.appcircle.io/docs/assets/image (168).png>)

### Delete a Build Profile

In order to delete a build, simply click on the Three Dot and click delete.

![](<https://cdn.appcircle.io/docs/assets/image (245).png>)

After the prompt, the profile will be deleted.

In order to free up storage in your organization, you should also remove the other references pointing to the artifact. In example, if you have the same artifact on the testing distribution, you should also delete those artifacts as well.&#x20;

Is your artifact storage full? Learn more about freeing up space [here](https://docs.appcircle.io/troubleshooting-faq/common-issues#artifact-storage-is-full).

:::info

[Have questions? Contact us here.](https://appcircle.io/support/)

:::
