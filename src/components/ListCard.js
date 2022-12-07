import React from 'react';

export default function ListCard({ title, description, href, customClass, children }) {
  return (
    <div class={`navigation-card ${customClass}`}>
      <a href={href}>
        <div class="navigation-card-image-container">{children}</div>
        <h3>{title}</h3>
        <p>{description}</p>
      </a>
    </div>
  );
}
