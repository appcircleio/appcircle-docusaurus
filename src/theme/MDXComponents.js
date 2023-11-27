import React from 'react';
import MDXComponents from '@theme-original/MDXComponents';

import Screenshot from '@site/src/components/Screenshot';
import NarrowImage from '@site/src/components/NarrowImage';
import ContentRef from '@site/src/components/ContentRef';
import ExternalUrlRef from '@site/src/components/ExternalUrlRef';
import ExternalScreenshot from '@site/src/components/ExternalScreenshot';

/**
 * Note to contributor:
 * The components that are added here are are registered as Global Export on Docusaurus/MDX like Link, CodeBlock etc.
 * This means, these will be imported as overhead which can slow down first load or build time.
 * Therefore, here should ONLY contain components which will be used all across the documentation, frequently.
 * 
 * If your component is only used on a single documentation, DO NOT register them as global export; instead, stick to local import.
 * For example, there's SelfHostedBadge component which is only used on release notes. DO NOT add that or similar components here.
 */

export default {
  ...MDXComponents, // Re-use the default mapping
  Screenshot,
  NarrowImage,
  ContentRef,
  ExternalUrlRef,
  ExternalScreenshot
};