---
title: React Native Specific Workflow Steps
description: Explore React Native specific workflow steps for building profiles. Visit our workflow marketplace for a complete list.
tags: [react native, mobile, workflow, step]
---

# React Native Specific Workflow Steps

The steps listed below are specific to the React Native build profiles.

You can find the full list of available workflow steps in our [workflow marketplace](https://github.com/appcircleio/appcircle-workflow-components) and under each workflow step in this document, you can find the related repository URL, which also includes the documentation for the related step.

## [App Center CodePush](/workflows/react-native-specific-workflow-steps/app-center-code-push)

Release a React Native update to [App Center](https://appcenter.ms/) CodePush. You need enter your token, owner, app name to distribute your updates.

## [Install Node](/workflows/react-native-specific-workflow-steps/node-install)

React Native applications commonly depend on certain Node modules. This workflow step makes sure that you have the required Node version installed in the build agent to build your React Native application.

## [npm/Yarn Commands](/workflows/react-native-specific-workflow-steps/npm-yarn-commands)

You may want to use npm or Yarn package manager to install specific dependencies for your React Native applications. The package manager commands you enter are executed in this workflow step.

## [React Native UI Test](/workflows/react-native-specific-workflow-steps/react-native-ui-test)

Run all the UI tests in your project written with [Detox](https://wix.github.io/Detox/docs/introduction/getting-started/) integration.

## [React Native Unit Test](/workflows/react-native-specific-workflow-steps/react-native-unit-test)

Run all the unit tests in your project written with [Jest](https://jestjs.io/docs/tutorial-react-native) integration.

## [Test Reports for React Native](/workflows/react-native-specific-workflow-steps/test-reports-react-native)

This component provides detailed reports and insights on the results of React Native app tests conducted.

For detailed information on the usage of **Test Reports for React Native**, please refer to the documentation:

[Appcircle React Native Testing](/continuous-testing/react-native-testing)