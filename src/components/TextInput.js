import React from 'react'
import  "./TextInput.scss";

export const TextInput = (props) => {
  return (
    <input
      className="TextInput"
      value={props.value}
      onChange={(e) => props.onChange(e)}
    />
  );
};

export default TextInput