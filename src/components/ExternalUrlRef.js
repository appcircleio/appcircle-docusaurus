import React from "react";
import PropTypes from "prop-types";
import "./ExternalUrlRef.css";

const ExternalUrlRef = ({ url, title, description, image }) => (
  <a
    href={url}
    target="_blank"
    rel="noopener noreferrer"
    className="erc-container"
  >
    <div className="erc-content">
      <div className="erc-title">{title}</div>
      {description && <div className="erc-description">{description}</div>}
      <div className="erc-url">{new URL(url).hostname}</div>
    </div>
    {image && (
      <div className="erc-image-container">
        <img
          src={image}
          alt={`Preview of ${title}`}
          className="erc-image"
          loading="lazy"
        />
      </div>
    )}
  </a>
);

ExternalUrlRef.propTypes = {
  url: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  description: PropTypes.string,
  image: PropTypes.string,
};

export default ExternalUrlRef;
