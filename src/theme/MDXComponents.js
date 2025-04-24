import React from "react";
import MDXComponents from "@theme-original/MDXComponents";

import Screenshot from "@site/src/components/Screenshot";
import NarrowImage from "@site/src/components/NarrowImage";
import ContentRef from "@site/src/components/ContentRef";
import ExternalUrlRef from "@site/src/components/ExternalUrlRef";
import * as ModuleBadges from "@site/src/components/Badge/ModuleBadges";

export default {
  ExternalUrlRef,
  Screenshot,
  NarrowImage,
  ContentRef,
  ...MDXComponents,
  ...ModuleBadges,
};
