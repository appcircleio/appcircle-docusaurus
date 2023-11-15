import React from 'react';

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
        <img className='rlc-image' src='https://cdn.appcircle.io/docs/assets/appcircle-logo.png' />
      </div>
    </a>
  );
}