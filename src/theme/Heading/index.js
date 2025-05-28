import React from 'react';
import Heading from '@theme-original/Heading';
import {useLocation} from '@docusaurus/router';

export default function HeadingWrapper(props) {
  const location = useLocation();
  const isReleaseNotesPage = location.pathname === '/release-notes';
  
  if (isReleaseNotesPage && props.as === 'h2') {
    const headingText = React.Children.toArray(props.children)
      .filter(child => typeof child === 'string')
      .join('');
    
    const versionMatch = headingText.match(/^(\d+\.\d+\.\d+)/);
    if (versionMatch) {
      const formattedVersion = versionMatch[1].replace(/\./g, '-');

      return <Heading {...props} id={formattedVersion} />;
    }
  }
  
  return <Heading {...props} />;
} 