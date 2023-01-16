import React from 'react';
import clsx from 'clsx';

export default function NarrowImage({ src, ...rest }) {
  return <img src={src} {...rest} className="image-narrow" />;
}
