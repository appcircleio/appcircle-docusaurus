// BuildIcon.jsx
import React from "react";

const PublishIcon = ({ width = "35", height = "35", fill = "#5B799E" }) => (
  <svg
    xmlns="http://www.w3.org/2000/svg"
    width={width}
    height={height}
    viewBox="-4 0 44.2 35.7"
  >
    <path
      d="M33.5 16.255h-18v18h18v-18ZM18 0v13h13V0H18Z"
      fill={fill}
      strokeWidth="0"
    ></path>
    <path
      d="m12.4 26.555-2.7-3c-.1-.1-.2-.2-.4-.2-.1 0-.3.1-.4.2l-.7.8c0 .1-.1.1-.1.2v.4c0 .1.1.1.1.2l1 1.1H4.1c-1.1 0-2.1-1-2.1-2.3v-13.8c0-.3.1-.6.2-.9.1-.2.2-.5.4-.7s.4-.4.7-.5.6-.1.8-.2h9.7c.7 0 1.2-.5 1.3-1 .1-.6-.5-1.3-1.3-1.2H4.1c-.3 0-.9 0-1.6.4-.5.2-1 .6-1.3 1-.4.3-.7.8-.9 1.4-.2.5-.3 1.1-.3 1.7v13.7c0 .6.1 1.2.3 1.8.2.6.5 1.1.9 1.5s.8.8 1.3 1c.5.2 1 .3 1.6.3h5.2l-1 1.1c0 .1-.1.1-.1.2v.4c0 .1.1.1.1.2l.7.8c.2.2.5.2.7 0l2.7-3c.1-.1.2-.2.2-.4.1-.1.1-.3.1-.4v-.3c-.1-.2-.3-.4-.3-.5Z"
      fill={fill}
      strokeWidth="0"
    ></path>
  </svg>
);

export default PublishIcon;
