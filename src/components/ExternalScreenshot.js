import React from 'react';

/**
 * The URLs are for remote content. For local content, please do not use this component.
 *
 * @returns 
 */
export default function Screenshot({ url, width = 0, height = 0 }) {
  return (
    <img className="external-screenshot" src={url} width={width} height={height}></img>
  );
}