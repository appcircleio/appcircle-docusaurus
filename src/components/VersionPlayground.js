import React, { useState } from 'react';
import clsx from 'clsx';
import Switch from "./Switch";
import Select from './Select';

export default function VersionPlayground() {

    const [enableBuildNumber, setEnableBuildNumber] = useState(false);
    const [buildNumber, setBuildNumber] = useState('5');
    const [versionNumber, setVersionNumber] = useState('1.2.3');
    const [enableBuildVersioning, setEnableBuildVersioning] = useState(false);
    const [selectOmitZeroPatchVersion, setSelectOmitZeroPatchVersion] = useState(false);
    const [versionStrategy, setversionStrategy] = useState('keep');

    const buildSources = [
        { label: "Environment Variable", value: "env" },
        { label: "Xcode (Info.plist)", value: "xcode" }
    ];

    const envSources = [
        { label: "Environment Variable", value: "env" },
        { label: "App Store", value: "appstore" },
        { label: "Xcode (Info.plist)", value: "xcode" }
    ];

    const versionStrategies = [
        { label: "Keep", value: "keep" },
        { label: "Major", value: "major" },
        { label: "Minor", value: "minor" },
        { label: "Patch", value: "patch" }
    ];


    return (
        <div>
            <div>
                Build Number
            <input
                className="TextInput"
                value={buildNumber}
                onChange={(e) => setBuildNumber(e.target.value)}
            />
        </div>

        <div>
                Version Number
            <input
                className="TextInput"
                value={versionNumber}
                onChange={(e) => setVersionNumber(e.target.value)}
            />
        </div>
        <hr />


            UPDATE BUILD NUMBER WHILE BUILDING
            <Switch
                isOn={enableBuildNumber}
                onColor="#EF476F"
                handleToggle={() => setEnableBuildNumber(!enableBuildNumber)}
            />
            <Select options={versionStrategies} value={versionStrategy} onChange={setversionStrategy} />
        </div>
    );
}

//  value={enableBuildVersioning ? versionStrategy: versionStrategies[0]}