---
title: Manage Pools
metaTitle: Manage Pools
metaDescription: Manage Pools
sidebar_position: 1
---

### Monitoring Self-hosted Pools

When you add a new self-hosted runner to your organization, it appears at "Self-hosted Runners" list with its pool.

![](https://cdn.appcircle.io/docs/assets/self-hosted-runner-runners-selected-runner-01.png)

Pool creation is managed automatically while registering a self-hosted runner from CLI.

If a pool doesn't exist in your organization, system creates that pool and adds runner into that pool. If you choose a pool name existing in organization, your runner will be added to that existing pool.

### Select Pool for Build Profile

Self-hosted pools are visible as a list in "Build Profiles". Open your app's build profile, click on "Config" button and you will find pools at "Config" tab in build profile settings.

![](https://cdn.appcircle.io/docs/assets/self-hosted-runner-config-pool-list-01.png)

If you don't have any self-hosted pool yet, list will have only "Default" pool which is Appcircle cloud.

You can choose your self-hosted pools or Appcircle cloud anytime you want and switch between them according to your needs.

:::warning

Keep in mind that, pool selection is important for build pipeline success. Your self-hosted runners in that pool should have required capabilities for the selected build profile.

For example, if your pool has only android tools configured in its runners, you can't build an iOS app in that pool. Or if you have runners with only Xcode 13.3 in your pool, your Xcode 13.4 selected build profile won't be executed in that pool.

:::

:::info

You can not define or select specific self-hosted runner in a pool. When a build job enters queue, it will be selected by any of the runner in that pool. So, as a best practice, try to organize your pool homogeneously.

Pools should have runners which have similar tools and capabilities. Machine architecture (arm64, x86_64) can also be taken into account when organizing self-hosted pools.

:::

:::info

Changing runner pool doesn't affect current running builds on pool. It will affect next build job after change.

:::

#### Pool-Based Xcode Version Selection

When self-hosted agents connect, they provide the build platform information they can receive builds for, along with any available Xcode versions. In the self-hosted collection, this information is updated and maintained. The goal is to allow the selection of an Xcode version specific to the agent during the build process instead of using the default Xcode.

If we are working with multiple machines on the iOS side, we can now define Xcode versions specific to the agent pool.

Accordingly, you can make specific pool selections and set your configurations.

<b>Example Macpool 1:</b>

![](<https://cdn.appcircle.io/docs/assets/macpool1.png>)

<b> Example Macpool 2:</b>

![](<https://cdn.appcircle.io/docs/assets/macpool2.png>)

### Delete Self-hosted Pool

Pool removal is managed automatically while removing or moving runner. If you remove a self-hosted runner and its pool doesn't have any other runners in that pool, then empty pool is deleted automatically and you won't see it in self-hosted runners list or build profile config tab. Same behavior happens when you move a self-hosted runner from one pool to another.

If you want to remove pool manually or remove group of runners with pool removal, click on pool name at "Self-hosted Runners" list and use "Delete" button at the bottom of pool details.

![](https://cdn.appcircle.io/docs/assets/self-hosted-runner-pool-detail-01.png)

A confirmation dialog will be visible for your approval. Type pool name into textbox and click on delete.

This action removes pool and its runners all together. Previously assigned build profiles will be mapped to "Default" pool and until you assign them to another self-hosted pool, their build jobs will be sent to Appcircle cloud.

:::info

Removing or deleting self-hosted pools doesn't affect running build jobs on that pool. On-going build jobs will be completed but that self-hosted pool won't get any new build job from queue.

:::
