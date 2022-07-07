import React, { useState, useEffect } from "react";
import ToggleCircle from "./AppCircleComponent/ToggleCircle";
import TextInputCircle from "./AppCircleComponent/TextInputCircle";
import SelectCircle from "./AppCircleComponent/SelectCircle";
import "./Calculated.scss";

export default function VersionPlayground(props) {
  const [buildNumber, setBuildNumber] = useState("5");
  const [versionNumber, setVersionNumber] = useState("1.2.3");
  const [buildOffset, setBuildOffset] = useState("1");
  const [versionOffset, setVersionOffset] = useState("0");
  const [newBuildNumber, setNewBuildNumber] = useState("5");
  const [newVersionNumber, setNewVersionNumber] = useState("1.2.3");

  const [omitZero, setOmitZero] = useState(false);
  const [versionStrategy, setVersionStrategy] = useState("keep");

  const [toggleCheckedBuild, setToggleCheckedBuild] = useState(false);
  const [toggleCheckedVersion, setToggleCheckedVersion] = useState(false);
  const {title, subtitle} = props;

  const versionStrategies = [
    { label: "Keep", value: "keep" },
    { label: "Major", value: "major" },
    { label: "Minor", value: "minor" },
    { label: "Patch", value: "patch" },
  ];

  const handleChange = (e) => {
    setToggleCheckedBuild(e.target.checked);
  };
  const handleChangeVersion = (e) => {
    setToggleCheckedVersion(e.target.checked);
  };

  const handleBuildNumber = (e) => {
    setBuildNumber(e.target.value);
  };

  const handleVersionNumber = (e) => {
    setVersionNumber(e.target.value);
  };

  const calculateBuildNumber = () => {
    const calculated =
      (parseInt(buildOffset) || 0) + (parseInt(buildNumber) || 0);
    setNewBuildNumber(calculated);
  };

  const calculateVersionNumber = () => {
    const version_array = versionNumber.split(".").map(Number);
    const offset = parseInt(versionOffset) || 0;
    switch (versionStrategy) {
      case "patch":
        version_array[2] = (version_array[2] || 0) + offset;
        break;
      case "minor":
        version_array[1] = (version_array[1] || 0) + offset;
        version_array[2] = version_array[2] = 0;
        break;
      case "major":
        version_array[0] = (version_array[0] || 0) + offset;
        version_array[1] = version_array[1] = 0;
        version_array[1] = version_array[2] = 0;
        break;
      default:
        break;
    }

    if (omitZero && version_array[2] == 0) {
      version_array.pop();
    }
    setNewVersionNumber(version_array.join("."));
  };

  useEffect(() => {
    calculateBuildNumber();
  }, [buildNumber, buildOffset]);

  useEffect(() => {
    calculateVersionNumber();
  }, [versionNumber, versionOffset, versionStrategy, omitZero]);

  return (
    <div>
      <TextInputCircle
        // bottom text is not visible if bottomText is false
        title={title}
        bottomText={false}
        value={buildNumber}
        name="buildNumber"
        onChange={handleBuildNumber}
      />
      <TextInputCircle
        // bottom text is not visible if bottomText is false
        title={subtitle}
        bottomText={false}
        value={versionNumber}
        name="versionNumber"
        onChange={handleVersionNumber}
      />

      <ToggleCircle
        toggleTitle={`UPDATE ${title.toUpperCase()} WHILE BUILDING`}
        toggleDesc={`Appcircle will apply the ${title.toLowerCase()} while building based on your settings below.`}
        checked={toggleCheckedBuild}
        disabled={false}
        onChange={handleChange}
        // offstyle="#a5b5c9"
        // onstyle="var(--ifm-color-primary)"
      />
      {toggleCheckedBuild && (
        <>
          <TextInputCircle
            title={title + " Offset"}
            // bottom text is not visible if bottomText is false
            bottomText={false}
            value={buildOffset}
            onChange={(e) => setBuildOffset(e.target.value)}
          />
          <div className="Calculated">
            <label>
              Calculated {title}: <span>{newBuildNumber}</span>
            </label>
          </div>
        </>
      )}
      <ToggleCircle
        toggleTitle={`UPDATE ${subtitle.toUpperCase()} WHILE BUILDING`}
        toggleDesc={`Appcircle will apply the ${subtitle.toLowerCase()} while building based on your settings below.`}
        checked={toggleCheckedVersion}
        disabled={false}
        onChange={handleChangeVersion}
        // offstyle="#a5b5c9"
        // onstyle="var(--ifm-color-primary)"
      />
      {toggleCheckedVersion && (
        <>
          <TextInputCircle
            // bottom text is not visible if bottomText is false
            title={subtitle + " Offset"}
            bottomText={false}
            value={versionOffset}
            onChange={(e) => setVersionOffset(e.target.value)}
          />
          <SelectCircle
            // bottom text is not visible if bottomText is false
            title="Version Strategy"
            options={versionStrategies}
            value={versionStrategy}
            onChange={setVersionStrategy}
          />

          <ToggleCircle
            toggleTitle="Omit Zero Patch Version"
            toggleDesc="If true omits zero in patch version(so 42.10.0 will become 42.10 and 42.10.1 will remain 42.10.1), default is false"
            checked={omitZero}
            disabled={false}
            onChange={(e) => setOmitZero(e.target.checked)}
            offstyle="#a5b5c9"
            onstyle="var(--ifm-color-primary)"
          />

          <div className="Calculated">
            <label>
              Calculated {subtitle}: <span>{newVersionNumber}</span>
            </label>
          </div>
        </>
      )}
    </div>
  );
}
