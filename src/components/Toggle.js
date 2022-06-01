import React from "react";
import './Toggle.scss'

function Toggle(props) {
  const {
    checked,
    disabled,
    onChange,
    offstyle = "btn-warning",
    onstyle = "btn-success"
  } = props;
  let displayStyle = checked ? onstyle : offstyle;

  return (
    <>
      <label style={{userSelect:'none'}}>
        <span className="switch-wrapper">
          <input
            type="checkbox"
            checked={checked}
            disabled={disabled}
            onChange={(e) => onChange && onChange(e)}
          />
          <span className="switch" style={{ background: displayStyle }}>
            <span className="switch-handle" />
          </span>
        </span>
      </label>
    </>
  );
}

export default Toggle;
