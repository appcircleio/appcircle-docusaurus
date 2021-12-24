---
title: "Build Profile Branch Management"
metaTitle: "Build Profile Branch Management"
metaDescription: "Build Profile Branch Management"
---
# Build Profile Branch Management

When you connect to a repository, all branches of that repository will be displayed with the last 100 commits. Appcircle provides a number of features for easy management of branches.



### Finding a Specific Branch

To find a specific branch, just start typing in the name in the branch search bar and the branches that include the phrase will be filtered as you type.

![](<../assets/image (138).png>)

####

### Pinning Branches to the Top for Faster Access

If you are using a branch frequently such as develop or master, you can pin it to the top. To pin a branch, open the context menu on the top right corner of the branch list item and press "Pin Item".

![](<../assets/image (139).png>)



The branch will be moved to the top with a pinned indicator. You can unpin the branch by pressing the "Remove Pin" button in the branch context menu.

![](<../assets/image (142).png>)



### Replicating the Build Configurations Across Branches

Once you [configure a branch](build-profile-configuration.md), you can easily replicate the same configuration in any other branch without the need to configure each branch separately.

After a branch is configured from the config screen, its status will change from "Configuration pending" to "Configured". In the configured branches, the "Copy Configuration" button will be active under the branch context menu.&#x20;

To copy a configuration, press the "Copy Configuration" button in the source branch context menu and then press the "Set Copied Configuration" in the destination branch context menu.

![Source branch](<../assets/image (143).png>)

![Destination branch](<../assets/image (144).png>)

Once you confirm the copy operation, the configuration in the destination will be set with the exact same options in the source branch and any current configuration will be overwritten

Please note that if the contents of the destination branch is not compatible with the selected options, you may get build errors.

![](<../assets/image (146).png>)

