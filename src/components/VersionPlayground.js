import React, { useState } from "react";
import Switch from "./Switch";
import Select from "./Select";
import TextInput from "./TextInput";
import Toggle from "./Toggle";
import ToggleCircle from "./AppCircleComponent/ToggleCircle";
import { TextInputCircle } from "./AppCircleComponent/TextInputCircle";
import SelectCircle from "./AppCircleComponent/SelectCircle";

export default function VersionPlayground() {
  const [enableBuildNumber, setEnableBuildNumber] = useState(false);
  const [buildNumber, setBuildNumber] = useState("5");
  const [versionNumber, setVersionNumber] = useState("1.2.3");
  const [enableBuildVersioning, setEnableBuildVersioning] = useState(false);
  const [selectOmitZeroPatchVersion, setSelectOmitZeroPatchVersion] =
    useState(false);
  const [versionStrategy, setversionStrategy] = useState("keep");

  const [toggleCheckedBuild, setToggleCheckedBuild] = useState(false);
  const [toggleCheckedVersion, setToggleCheckedVersion] = useState(false);

  const [value, setValue] = useState("");

  const buildSources = [
    { label: "Environment Variable", value: "env" },
    { label: "Xcode (Info.plist)", value: "xcode" },
  ];

  const envSources = [
    { label: "Environment Variable", value: "env" },
    { label: "App Store", value: "appstore" },
    { label: "Xcode (Info.plist)", value: "xcode" },
  ];

  const versionStrategies = [
    { label: "Keep", value: "keep" },
    { label: "Major", value: "major" },
    { label: "Minor", value: "minor" },
    { label: "Patch", value: "patch" },
  ];

  const handleInput = (e) => {
    setValue(e.target.value);
  };
  const handleChange = (e) => {
    setToggleCheckedBuild(e.target.checked);
  };
  const handleChangeVersion = (e) => {
    setToggleCheckedVersion(e.target.checked);
  };

  return (
    <div>
      <TextInputCircle
        // bottom text is not visible if bottomText is false
        title="Build Number"
        bottomText={false}
        value={value}
        onChange={handleInput}
      />
      <TextInputCircle
        // bottom text is not visible if bottomText is false
        title="Version Number"
        bottomText={false}
        value={value}
        onChange={handleInput}
      />
      <ToggleCircle
        toggleTitle="UPDATE BUILD NUMBER WHILE BUILDING"
        toggleDesc="Appcircle will apply the build number while building based on your settings below. Code in your repository won't change.
        Code in your repository won’t change"
        checked={toggleCheckedBuild}
        disabled={false}
        onChange={handleChange}
        offstyle="#a5b5c9"
        onstyle="var(--ifm-color-primary)"
      />
      {toggleCheckedBuild && (
        <TextInputCircle
          title="Build Offset"
          // bottom text is not visible if bottomText is false
          bottomText={false}
          value={value}
          onChange={handleInput}
        />
      )}
      <ToggleCircle
        toggleTitle="UPDATE VERSION NUMBER WHILE BUILDING"
        toggleDesc="Appcircle will apply the version number stated below while building.
        Code in your repository won’t change"
        checked={toggleCheckedVersion}
        disabled={false}
        onChange={handleChangeVersion}
        offstyle="#a5b5c9"
        onstyle="var(--ifm-color-primary)"
      />
      {toggleCheckedVersion && (
        <>
          <TextInputCircle
            // bottom text is not visible if bottomText is false
            title="Version Offset"
            bottomText={false}
            value={value}
            onChange={handleInput}
          />
          <SelectCircle
            // bottom text is not visible if bottomText is false
            title="Version Strategy"
            options={versionStrategies}
            value={versionStrategy}
            onChange={setversionStrategy}
          />
        </>
      )}
    </div>
  );
}

//  value={enableBuildVersioning ? versionStrategy: versionStrategies[0]}
