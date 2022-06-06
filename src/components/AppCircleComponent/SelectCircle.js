import React from 'react'
import Select from '../Select';
import "./TextInputCircle.scss";
export const SelectCircle = (props) => {
  return (
    <div className="TextInputCircle">
      <div className="TextInputCircle_Label">
        <label>{props.title}</label>
      </div>
      <Select {...props} />
    </div>
  );
};

export default SelectCircle
