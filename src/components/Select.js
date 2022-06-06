import React, { useState } from "react";
import "./Select.scss";
const Select = (props) => {
  return (
    <>
      <select
        className="Select"
        value={props.value}
        onChange={(e) => props.onChange(e.target.value)}
      >
        {props.options.map((c) => (
          <option
            className="Option"
            style={{ color: "#445b77", fontSize: 15 }}
            key={c.label}
            value={c.value}
          >
            {c.label}
          </option>
        ))}
      </select>
    </>
  );
};

export default Select;
