import React, { useState } from 'react';
import clsx from 'clsx';
import Switch from "./Switch";

export default function VersionPlayground() {

    const [enableBuildNumber, setEnableBuildNumber] = useState(false);
    const [enableBuildVersioning, setEnableBuildVersioning] = useState(false);
    const [selectOmitZeroPatchVersion, setSelectOmitZeroPatchVersion] = useState(false);

    const buildSources = [
        { label: "Environment Variable", value: "env" },
        { label: "Xcode (Info.plist)", value: "xcode" }
    ];

    const envSources = [
        { label: "Environment Variable", value: "env" },
        { label: "App Store", value: "appstore" },
        { label: "Xcode (Info.plist)", value: "xcode" }
    ];

    return (
        <div>
            UPDATE BUILD NUMBER WHILE BUILDING
            <Switch
                isOn={enableBuildNumber}
                onColor="#EF476F"
                handleToggle={() => setEnableBuildNumber(!enableBuildNumber)}
            />
        </div>
    );
}
