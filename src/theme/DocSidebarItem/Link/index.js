import DocSidebarItemLink from '@theme-original/DocSidebarItem/Link';

export default function DocSidebarItemLinkWrapper(props) {
  if (props.href && props.href.includes('/release-notes#') && props.href.match(/#\d+\.\d+\.\d+/)) {
    const versionMatch = props.href.match(/#(\d+\.\d+\.\d+)/);
    if (versionMatch) {
      const formattedVersion = versionMatch[1].replace(/\./g, '-');
      const newHref = props.href.replace(versionMatch[0], `#${formattedVersion}`);

      return <DocSidebarItemLink {...props} href={newHref} />;
    }
  }
  
  return <DocSidebarItemLink {...props} />;
} 