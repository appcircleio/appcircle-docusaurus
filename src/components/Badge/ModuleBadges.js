// Specific Badge Components for each menu item
import React from "react";
import Badge from "./Badge";
import BuildIcon from "../ModuleIcons/BuildIcon";
import BuildIntegrationsIcon from "../ModuleIcons/BuildIntegrationsIcon";
import ContinuousTestingIcon from "../ModuleIcons/ContinuousTestingIcon";
import EnvironmentVariablesIcon from "../ModuleIcons/EnvironmentVariablesIcon";
import VersioningIcon from "../ModuleIcons/VersioningIcon";
import IntegrationsIcon from "../ModuleIcons/IntegrationsIcon";
import AccountIcon from "../ModuleIcons/AccountIcon";
import ApiIcon from "../ModuleIcons/Api-Icon";
import BestPracticesIcon from "../ModuleIcons/BestPracticesIcon";
import DistributeIcon from "../ModuleIcons/DistributeIcon";
import EnterpriseStoreIcon from "../ModuleIcons/EnterpriseStoreIcon";
import FaqIcon from "../ModuleIcons/FaqIcon";
import InfrastructureIcon from "../ModuleIcons/InfrastructureIcon";
import PublishIcon from "../ModuleIcons/PublishIcon";
import ReportsIcon from "../ModuleIcons/ReportsIcon";
import SelfHostedIcon from "../ModuleIcons/SelfHostedIcon";
import SigningIdentitiesIcon from "../ModuleIcons/SigningIdentitiesIcon";

const AccountBadge = () => (
  <Badge icon={AccountIcon}>Account & Organization</Badge>
);

const APIBadge = () => <Badge icon={ApiIcon}>API & CLI</Badge>;

const BestPracticesBadge = () => (
  <Badge icon={BestPracticesIcon}>Best Practices</Badge>
);

const DistributionBadge = () => (
  <Badge icon={DistributeIcon}>Testing Distribution</Badge>
);
const EnterpriseStoreBadge = () => (
  <Badge icon={EnterpriseStoreIcon}>Enterprise App Store</Badge>
);
const FaqBadge = () => <Badge icon={FaqIcon}>Troubleshooting & FAQ</Badge>;

const InfrastructureBadge = () => (
  <Badge icon={InfrastructureIcon}>Build Infrastructure</Badge>
);

const IntegrationsBadge = () => (
  <Badge icon={IntegrationsIcon}>Integrations</Badge>
);
const PublishBadge = () => <Badge icon={PublishIcon}>Publish</Badge>;

const PublishIntegrationsBadge = () => (
  <Badge icon={PublishIcon}>Publish Integrations</Badge>
);

const ReportsBadge = () => <Badge icon={ReportsIcon}>Reports</Badge>;

const SelfHostedBadge = () => <Badge icon={SelfHostedIcon}>Self-Hosted</Badge>;

const SigningIdentitiesBadge = () => (
  <Badge icon={SigningIdentitiesIcon}>Signing Identities</Badge>
);

const BuildBadge = () => <Badge icon={BuildIcon}>Build</Badge>;

const BuildIntegrationsBadge = () => (
  <Badge icon={BuildIntegrationsIcon}>Build Integrations</Badge>
);
const ContinuousTestingBadge = () => (
  <Badge icon={ContinuousTestingIcon}>Continuous Testing</Badge>
);
const EnvironmentVariablesBadge = () => (
  <Badge icon={EnvironmentVariablesIcon}>Environment Variables</Badge>
);
const VersioningBadge = () => <Badge icon={VersioningIcon}>Versioning</Badge>;

const CloudBadge = () => <Badge icon={SelfHostedIcon}>Cloud</Badge>;

export {
  BuildBadge,
  BuildIntegrationsBadge,
  ContinuousTestingBadge,
  EnvironmentVariablesBadge,
  VersioningBadge,
  AccountBadge,
  APIBadge,
  BestPracticesBadge,
  DistributionBadge,
  EnterpriseStoreBadge,
  FaqBadge,
  InfrastructureBadge,
  IntegrationsBadge,
  PublishBadge,
  PublishIntegrationsBadge,
  ReportsBadge,
  SelfHostedBadge,
  SigningIdentitiesBadge,
  CloudBadge,
};
