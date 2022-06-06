import React, { useState } from "react";
import styles from "./Switch.module.css";

const Switch = ({ isOn, handleToggle, onColor }) => {
    console.log(styles);
    return (
      <>
        <input
          checked={isOn}
          onChange={handleToggle}
          className={styles.switchcheckbox}
          id={`react-switch-new`}
          type="checkbox"
        />
        <label
          style={{ background: isOn && onColor }}
          className={styles.switchlabel}
          htmlFor={`react-switch-new`}
        >
          <span className={styles.switchbutton} />
        </label>
      </>
    );
  };
export default Switch;
