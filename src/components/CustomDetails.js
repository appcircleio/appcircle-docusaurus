import React from 'react';

/**
 *  This component is a custom implementation of the Details component, 
 *  created to resolve the issue where image zoom is not functioning in the default Details component.
 * 
 *  The issue occurs in a third-party plugin. You can find more details about it here:
 *  https://github.com/flexanalytics/plugin-image-zoom/issues/9
 * 
 * @param {*} props 
 * @returns 
 */
export default function CustomDetails( props ) {
  const items = React.Children.toArray(props.children);
  // Split summary item from the rest to pass it as a separate prop to the
  // Details theme component
  const summary = items.find(
    (item) =>
      React.isValidElement(item) && item.type === 'summary',
  );
  const children = <>{items.filter((item) => item !== summary)}</>;

  return (
    <details class="custom-details alert alert--info" data-collapsed="false">
    {summary}
    <div style={{
      display: 'block', overflow: 'visible', height: 'auto', willChange: 'height', transition: 'height 266ms ease-in-out'
    }}>
      <div class="custom-details-inner-container">
        {children}
      </div>
    </div>
  </details>
  );
}