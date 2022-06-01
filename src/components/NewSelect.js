import { useState } from "react";

const Select = (props) => {
  const strategy = {
    major: "Major",
    minor: "Minor",
    patch: "Patch",
    keep: "Keep"
  };

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
        onChange={(e) => props.onChange(e)}
      >
        {Object.entries(strategy).map((c) => (
          <option
            style={{ color: "#445b77", fontSize: 15 }}
            key={c}
            value={c[1]}
          >
            {c[0]}
          </option>
        ))}
      </select>
      <h2>{props.value}</h2>
    </>
  );
};

export default Select;
