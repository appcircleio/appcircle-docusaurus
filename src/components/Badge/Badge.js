import React from "react";

// Generic Badge Component that accepts an icon
const Badge = ({ children, className, icon: Icon }) => (
  <span className={`module-badge ${className}`}>
    {Icon && <Icon />}
    {children}
  </span>
);

export default Badge;
