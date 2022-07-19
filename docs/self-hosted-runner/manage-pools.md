---
title: Manage Self-hosted Pools
metaTitle: Manage Self-hosted Pools
metaDescription: Manage Self-hosted Pools
sidebar_position: 4
---

# Monitoring Self-hosted Pools

When you add a new self-hosted runner to your organization, it appears at "Self-hosted Runners" list with its pool.

Pool creation is managed automatically while registering a self-hosted runner from CLI. If a pool doesn't exist in your organization, system creates that pool and adds runner into that pool. If you choose a pool name existing in organization, your runner will be added to that existing pool.

# Select Pool for Build Profile

Self-hosted pools are visible as a list in "Build Profiles". Open your app's build profile, click on "Config" button and you will find pools at "Config" tab in build profile settings.

If you don't have any self-hosted pool yet, list will have only "Default" pool which is Appcircle Cloud.

You can choose your self-hosted pools or Appcircle Cloud anytime you want and switch between them according to your needs.

:::warning

Keep in mind that, pool selection is important for build pipeline success. Your self-hosted runners in that pool should have required capabilities for the selected build proile. For example, if your pool has only android tools configured in its runners you can't build an iOS app in that pool.

:::

:::info

You can not define or select specific self-hosted runner in a pool. When a build job enters queue, it will be selected by any of the runner in that pool. So, as a best practice, organize your poold homogeneously. Pools should have runners which have similar tools and capabilities. Machine architecture (arm64, x86_64) can also be taken into account when orgnizing self-hosted pools.

:::

:::info

Changing runner pool doesn't affect current running builds on pool. It will affect next build job after change.

:::

# Delete Self-hosted Pool

Pool removal is managed automatically while removing or moving runner. If you remove a self-hosted runner and its pool doesn't have any other runners in that pool, then empty pool is deleted automatically and you won't see it in self-hosted runners list or build profile config. Same behaviour happens when you move a self-hosted runner from one pool to another.

If you want to remove pool manually or remove group of runners with pool removal, click on pool name at "Self-hosted Runners" list and use "Delete" button at the bottom of pool details. A confirmation dialog will be visible for your approval. Type pool name into textbox and click on delete.

This action removes pool and its runners all together. Previously assigned build profiles will be mapped to "Default" pool and until you assign them to another self-hosted pool, their build jobs will be sent to Appcircle Cloud.

:::info

Removing or deleting self-hosted pools doesn't affect running build jobs on that pool. On-going build jobs will be completed but that self-hosted pool won't get any new build job from queue.

:::

:::warning

When a self-hosted pool is deleted from organization for any reason, its related build profiles will return to `default` pool automatically which is Appcircle cloud. So build jobs will go on with Appcircle cloud automatically.

:::
