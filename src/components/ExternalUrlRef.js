import React from 'react';
import LinkIcon from '@site/static/img/link.svg';

export default function ExternalUrlRef({ url, title }) {
  return (
    <a class="rlc-container" href={url}>
      <div class="rlc-info">
        <div class="rlc-title">
          {title}
        </div>
        <div class="rlc-url-container">
          <span class="rlc-url">{url}</span>
        </div>
      </div>
      <div class="rlc-image-container">
        <LinkIcon className='rlc-image'/>
      </div>
    </a>
  );
}