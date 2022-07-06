---
title: Manage Self-hosted Runners
metaTitle: Manage Self-hosted Runners
metaDescription: Manage Self-hosted Runners
sidebar_position: 3
---

# Monitoring Self-hosted Runners

When you add a new self-hosted runner to your organization, it appears at "Self-hosted Runners" list with `Offline` state. You can see your runner in list with given name and pool from CLI.

After configuring and starting runner service, it becomes `Online` on list.

Self-hosted runners list has also other quick details which give your overview for your runners.

- "Version" is your self-hosted runner's version, you got from CLI.

```bash
./ac-runner -v
```

- "Last Contact" shows when Appcircle cloud has last contact with your self-hosted runner.

- "State" shows your self-hosted runner's current build status. For example, it can be `waiting` when runner is idle and `running` when it's executing build job.

You can **disable** self-hosted runner from list, using toggle button on right-hand side. When runner is disabled, it won't accept build job anymore. Disabling runner, doesn't affect currently running build pipeline on runner. It will complete its executing job. When complete, it won't take any new build job from queue until you enable it again. Using same toggle button you can enable self-hosted runner.

With quick enable/disable feature, you can remove self-hosted runner from pool temporarily and make some maintenance or debugging. When ready, you can add the self-hosted runner to pool again without any CLI operation.

:::warning

Your pool should have at least one active (ready-to-build) runner for build pipeline continuity.

If your pool is assigned to an active build profile but doesn't have any active runners, started build jobs from that profile will wait in queue until timeout.

For this reason, you should think about your pool organization and build profile settings while removing or disabling self-hosted runners.

:::
