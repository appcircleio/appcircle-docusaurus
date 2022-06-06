import React from 'react'
import Toggle from "../Toggle";
import "./ToggleCircle.scss";
export const ToggleCircle = (props) => {
  return (
    <div className="ToggleCircle">
      <div className="ToggleCircle_Label">
        <h1>{props.toggleTitle}</h1>
        <span>
          {props.toggleDesc}
        </span>
      </div>
      <Toggle {...props} />
    </div>
  );
};

export default ToggleCircle