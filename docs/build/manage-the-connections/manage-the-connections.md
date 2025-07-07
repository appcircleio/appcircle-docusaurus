---
title: Manage the Connections
description: The Connections page is a feature where we can check and edit the connections of the Git providers we are connected to.
tags: [build, connections, git providers, oauth, pat, personal access token]
sidebar_position: 1
---

import Screenshot from '@site/src/components/Screenshot';

# Connections

The Connections page is a feature where we can check and edit the connections of the Git providers we are connected to. You can access this page from the left bar in the Build module.

On this page, you can view **OAuth** and **PAT** (Personal Access Token) connections.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE6369-list.png' />

The tags next to the connections on your list display the connection type — whether it’s Cloud, Self-Hosted, and whether it uses an HTTP Token or a Personal Access Token.

:::info
If you have not previously connected to a Git provider on Appcircle, i.e., created a profile and not connected a repository, you will not see any connection on this page.
:::

## Connection Guides

You can connect GitHub through a GitHub app or Bitbucket and GitLab repositories to your build profile through OAuth apps. Alternatively, you can connect private repositories through SSH and public repositories directly on GitHub, Bitbucket, GitLab, and other compatible Git providers such as Azure DevOps and AWS CodeCommit.

## Connection Management

You can connect GitHub, GitLab, Bitbucket and Azure remote repositories. Different types of connections have different connection details in the connection settings.

## Accessing Internal Networks

In certain cases, the source codes of the apps may be stored in internal repositories instead of the cloud providers. If these internal repositories are accessible from the public internet, then you can use Appcircle without any additional configuration.