import Link from '@theme-original/Link';

export default function LinkWrapper(props) {
  if (props.href && props.href.startsWith('#') && props.href.match(/^#\d+\.\d+\.\d+/)) {
    const versionMatch = props.href.match(/^#(\d+\.\d+\.\d+)/);
    if (versionMatch) {
      const formattedVersion = versionMatch[1].replace(/\./g, '-');
      const newHref = `#${formattedVersion}`;
      
      return <Link {...props} href={newHref} />;
    }
  }
  
  return <Link {...props} />;
} 