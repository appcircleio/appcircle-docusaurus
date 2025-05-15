import TOCItems from '@theme-original/TOCItems';
import {useLocation} from '@docusaurus/router';

export default function TOCItemsWrapper(props) {
  const location = useLocation();
  const isReleaseNotesPage = location.pathname === '/release-notes';
  
  if (isReleaseNotesPage && props.toc) {
    const modifiedToc = props.toc.map(tocItem => {
      const versionMatch = tocItem.value.match(/^(\d+\.\d+\.\d+)/);
      if (versionMatch) {
        const formattedVersion = versionMatch[1].replace(/\./g, '-');
        
        return {
          ...tocItem,
          id: formattedVersion,
          children: tocItem.children?.map(child => {
            const childVersionMatch = child.value.match(/^(\d+\.\d+\.\d+)/);
            if (childVersionMatch) {
              const childFormattedVersion = childVersionMatch[1].replace(/\./g, '-');
              return {
                ...child,
                id: childFormattedVersion
              };
            }
            return child;
          })
        };
      }
      return tocItem;
    });
    
    return <TOCItems {...props} toc={modifiedToc} />;
  }
  
  return <TOCItems {...props} />;
} 