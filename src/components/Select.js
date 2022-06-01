import React, { useState } from 'react';

const Select = (props) => {
  return (
    <>
      <select
        style={{
          background: "#edf0f4",
          border: "1px solid #e1e6ef",
          borderRadius: 5,
          padding: 7,
          marginTop: 11
        }}
        value={props.value}
        onChange={(e) => props.onChange(e.target.value)}
      >
        {props.options.map((c) => (
            
          <option
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
