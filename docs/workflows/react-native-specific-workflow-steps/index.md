---
title: React Native Specific Workflow Steps
description: Explore React Native specific workflow steps for building profiles. Visit our workflow marketplace for a complete list.
tags: [react-native, mobile, workflow, step]
---

# React Native Specific Workflow Steps

The steps listed below are specific to the React Native build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## App Center CodePush

Release a React Native update to [App Center](https://appcenter.ms/) CodePush. You need enter your token, owner, app name to distribute your updates.

<ContentRef url="/workflows/react-native-specific-workflow-steps/app-center-code-push">
    App Center CodePush
</ContentRef>

## Install Node

React Native applications commonly depend on certain Node modules. This workflow step makes sure that you have the required Node version installed in the build agent to build your React Native application.

<ContentRef url="/workflows/react-native-specific-workflow-steps/node-install">
    Install Node
</ContentRef>

## npm/Yarn Commands

You may want to use npm or Yarn package manager to install specific dependencies for your React Native applications. The package manager commands you enter are executed in this workflow step.

<ContentRef url="/workflows/react-native-specific-workflow-steps/npm-yarn-commands">
    npm/Yarn Commands
</ContentRef>

## React Native UI Test

Run all the UI tests in your project written with [Detox](https://wix.github.io/Detox/docs/introduction/getting-started/) integration.

<ContentRef url="/workflows/react-native-specific-workflow-steps/react-native-ui-test">
    React Native UI Test
</ContentRef>

## React Native Unit Test

Run all the unit tests in your project written with [Jest](https://jestjs.io/docs/tutorial-react-native) integration.

<ContentRef url="/workflows/react-native-specific-workflow-steps/react-native-unit-test">
    React Native Unit Test
</ContentRef>

## Test Reports for React Native

This component provides detailed reports and insights on the results of React Native app tests conducted.

For detailed information on the usage of **Test Reports for React Native**, please refer to the documentation:

[https://docs.appcircle.io/continuous-testing/react-native-testing](https://docs.appcircle.io/continuous-testing/react-native-testing)

<ContentRef url="/workflows/react-native-specific-workflow-steps/test-reports-react-native">
    Test Reports for React Native
</ContentRef>
