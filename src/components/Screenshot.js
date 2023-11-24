import React from 'react';

/**
 * The urls are for remote content. For local content, please do not use this component.
 * If you really want to use it, you might use it like `require('../path/to/screenshot')`
 * @param param0 
 * @returns 
 */
export default function Screenshot({ url }) {
  return (
    <img className="screenshot" src={url}></img>
  );
}