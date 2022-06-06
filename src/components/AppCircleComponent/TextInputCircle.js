import React from 'react'
import { TextInput } from "../TextInput";
import "./TextInputCircle.scss";
export const TextInputCircle = (props) => {
  return (
    <div className="TextInputCircle">
      <div className="TextInputCircle_Label">
        <label>{props.title}</label>
      </div>
      <TextInput {...props} />
      {props.bottomText && props.bottomTitle && (
        <p className="TextInputCircle_bottomText">
          {props.bottomTitle}
        </p>
      )}
    </div>
  );
};

export default TextInputCircle

