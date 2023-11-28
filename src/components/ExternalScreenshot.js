import React from 'react';

/**
 * The URLs are for remote content. For local content, please do not use this component.
 * @param {width} | Width in pixels.
 * @param {height} | Width in pixels.
 * @returns 
 */
export default function ExternalScreenshot({ url, width = 0, height = 0, maxHeight }) {
  const widthNumber = parseInt(width);
  const heightNumber = parseInt(height);
  const aspectRatio = widthNumber / heightNumber;
  const calculatedMaxHeight = 898 / (aspectRatio); 
  /**
   * Here's what's going on here:
   * Since we provide the width height as pixels, we first extract the 'px' part. E.g. '3090px' becomes 3090.
   * Then, we calculate the aspect ratio by dividing width to height.
   * Then, We calculate the necessary maxHeight to the maxWidth which is given by docusaurus.
   * 898 is the maxWidth of the parent. 930 is the maximum width and 32 is with margins of 16px from each side. 
   */
  return (
    <img className="external-screenshot" src={url} width={width} height={height} style={{ maxHeight: maxHeight || calculatedMaxHeight }}></img>
  );
}