import React from "react";
import MDXComponents from "@theme-original/MDXComponents";

import Screenshot from "@site/src/components/Screenshot";
import NarrowImage from "@site/src/components/NarrowImage";
import ContentRef from "@site/src/components/ContentRef";
import ExternalUrlRef from "@site/src/components/ExternalUrlRef";
import * as ModuleBadges from "@site/src/components/Badge/ModuleBadges";
import HighlightFragment from "@site/src/components/HighlightFragment";

export default {
  ExternalUrlRef,
  Screenshot,
  NarrowImage,
  ContentRef,
  HighlightFragment,
  ...MDXComponents,
  ...ModuleBadges,
};
