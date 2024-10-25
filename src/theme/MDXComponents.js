import React from "react";
import MDXComponents from "@theme-original/MDXComponents";

import Screenshot from "@site/src/components/Screenshot";
import CustomDetails from "@site/src/components/CustomDetails";
import NarrowImage from "@site/src/components/NarrowImage";
import ContentRef from "@site/src/components/ContentRef";
import ExternalUrlRef from "@site/src/components/ExternalUrlRef";
import * as ModuleBadges from "@site/src/components/Badge/ModuleBadges";

export default {
  ExternalUrlRef,
  Screenshot,
  CustomDetails,
  NarrowImage,
  ContentRef,
  ...MDXComponents,
  ...ModuleBadges,
};
