---
title: In-app Updates
description: Streamline app maintenance and enhance user experience by implementing in-app updates through your Enterprise App Store, ensuring seamless and automatic version upgrades.
tags:
  [
    enterprise app store,
    app distribution,
    app deployment,
    enterprise apps,
    app store setup,
    appcircle app store,
    In-app updates,
  ]
---

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';
import Screenshot from '@site/src/components/Screenshot';

In-app updates enable applications to deliver and install updates directly within the app, enhancing user experience by minimizing disruption.

## What are In-app Updates for Streamlined Update Experience

In-app updates offer a seamless method for delivering and installing new versions of an application directly within the app. This eliminates the need for users to manually check for updates, ensuring they receive the latest features and fixes efficiently. This streamlined approach enhances the overall user experience and keeps the app up-to-date.

## Benefits and Examples of In-app Updates

In-app updates offer several benefits, including a smoother user experience by enabling seamless updates without requiring users to manually download or install new versions. For example, critical bug fixes and feature enhancements can be automatically applied while the app is running, ensuring users always have access to the latest improvements and functionalities.

## Implementing In-App Updates

## Prerequisites for Integration

### Authentication Requirements

To integrate an in-app update experience, you will need the **Personal Access Token (PAT)**, the **enterprise store prefix**, and the **enterprise store profile ID**.

### How to Obtain Integrations Parameters

#### Personal Access Token (PAT)

- For details on generating an Appcircle Personal Access Token, please visit the [Generating/Managing Personal API Tokens](/appcircle-api/api-authentication#generatingmanaging-the-personal-api-tokens).

#### Enterprise Store Prefix

Navigate to the Enterprise Store module and settings page to find the **STORE PREFIX** information. You can also modify it if needed.

<Screenshot url='https://cdn.appcircle.io/docs/assets/BE_4207-Enterprise-Store-Prefix-1.png' />

#### Enterprise Store Profile Id

You can obtain your Enterprise Store Profile ID from the URL or by using the @appcircle/cli.

##### How to Extract Your Enterprise Store Profile ID from the URL

1. Navigate to your Enterprise Store Profile.
2. Check the URL, which should be in this format: **/enterprise-store/profiles/PROFILE_ID**. The PROFILE_ID refers to your specific profile ID.

##### Retrieving Profile ID Using @appcircle/cli

The upcoming command retrieves the complete list of Enterprise Store Profiles.

```bash
appcircle enterprise-app-store profile list
```

### Authentication for Updates

#### Retrieving Access Token Using Personal API Token

To fetch app versions and download the binary, you first need to obtain an access token using a Personal API Token (PAT).

<Tabs defaultValue="swift" values={[
{ label: 'Swift', value: 'swift' },
{ label: 'Android', value: 'android' },
{ label: 'React Native', value: 'react-native' },
]}>

  <TabItem value="android">
    ```java
    import okhttp3.*;
    import com.google.gson.Gson;
    import java.io.IOException;
    import java.util.concurrent.TimeUnit;
    import com.google.gson.annotations.SerializedName;

    class AuthModel {
        @SerializedName("access_token")
        private String accessToken;

        public String getAccessToken() {
            return accessToken;
        }
        public void setAccessToken(String accessToken) {
            this.accessToken = accessToken;
        }
    }

    public class AuthService {
        private static final OkHttpClient client = new OkHttpClient.Builder()
                .connectTimeout(10, TimeUnit.SECONDS)
                .readTimeout(30, TimeUnit.SECONDS)
                .build();

        public static AuthModel getAccessToken(String pat) throws IOException {
            HttpUrl url = new HttpUrl.Builder()
                    .scheme("https")
                    .host("auth.appcircle.io")
                    .addPathSegment("auth")
                    .addPathSegment("v2")
                    .addPathSegment("token")
                    .build();

            RequestBody formBody = new FormBody.Builder()
                    .add("pat", pat)
                    .add("scope", "openid email profile")
                    .build();

            Request request = new Request.Builder()
                    .url(url)
                    .post(formBody)
                    .addHeader("accept", "application/json")
                    .addHeader("Content-Type", "application/x-www-form-urlencoded")
                    .build();

            try (Response response = client.newCall(request).execute()) {
                if (!response.isSuccessful()) throw new IOException("Unexpected code " + response);

                String responseBody = response.body().string();

                Gson gson = new Gson();
                return gson.fromJson(responseBody, AuthModel.class);
            }
        }
    }

    ```

  </TabItem>

  <TabItem value="swift">
    ```swift
    extension API {
        func getAccessToken(pat: String) async throws -> AuthModel {
            var components = URLComponents()
            components.scheme = apiConfig.scheme
            components.host = apiConfig.host
            components.path = "/auth/v2/token"
            guard let url = components.url else {
                throw HTTPError.invalidUrl
            }
            var request = URLRequest(url: url)

            request.httpMethod = HTTPMethod.POST.rawValue
            request.setValue("application/json", forHTTPHeaderField: "accept")
            request.setValue("application/x-www-form-urlencoded", forHTTPHeaderField: "Content-Type")

            let parameters = "pat=\(pat)&scope=openid email profile"
            request.httpBody = parameters.data(using: .utf8)

            return try await apiFetcher.request(request: request)
        }
    }
    ```

  </TabItem>

  <TabItem value="react-native">
    ```js
    import axios from 'axios';

    const AC_AUTH_HOSTNAME = 'https://auth.appcircle.io';

    export const getACToken = async (options: {pat: string}) => {
      const endpointURL = `${AC_AUTH_HOSTNAME}/auth/v2/token`;
      console.log(options.pat);
      const response = await axios.post(
        endpointURL,
        `pat=${encodeURIComponent(options.pat)}&scope=openid email profile`,
        {
          headers: {
            accept: 'application/json',
            'content-type': 'application/x-www-form-urlencoded',
          },
        },
      );

      return response.data;
    };
    ```

  </TabItem>
</Tabs>

###  Initiating Updates

#### Retrieving Available App Versions from Your Enterprise Store

Fetch all available versions and compare them with the current version to determine if an update is required.

<Tabs defaultValue="swift" values={[
{ label: 'Swift', value: 'swift' },
{ label: 'Android', value: 'android' },
{ label: 'React Native', value: 'react-native' },
]}>

  <TabItem value="android">
    ```java
    import okhttp3.Request;
    import okhttp3.OkHttpClient;
    import okhttp3.Response;
    import okhttp3.HttpUrl;
    import com.google.gson.Gson;
    import com.google.gson.reflect.TypeToken;
    import java.io.IOException;
    import java.lang.reflect.Type;
    import java.util.List;

    class AppVersion {
        private String id;
        private String version;
        private Integer publishType;

        public String getId() {
            return id;
        }

        public void setId(String id) {
            this.id = id;
        }

        public String getVersion() {
            return version;
        }

        public void setVersion(String version) {
            this.version = version;
        }

        public Integer getPublishType() {
            return publishType;
        }

        public void setPublishType(Integer publishType) {
            this.publishType = publishType;
        }
    }

    public class AppService {
        private static final String BASE_URL = "https://api.appcircle.io";
        private final OkHttpClient client = new OkHttpClient();
        private final Gson gson = new Gson();

        public List<AppVersion> getAppVersions(String accessToken, String profileId) throws IOException {
            HttpUrl url = HttpUrl.parse(BASE_URL + "/store/v2/profiles/" + profileId + "/app-versions");

            if (url == null) {
                throw new IOException("Invalid URL");
            }
            Request request = new Request.Builder()
                    .url(url)
                    .get()
                    .addHeader("Accept", "*/*")
                    .addHeader("Authorization", "Bearer " + accessToken)
                    .build();

            try (Response response = client.newCall(request).execute()) {
                if (!response.isSuccessful()) {
                    throw new IOException("Unexpected code " + response);
                }
                String responseBody = response.body().string();
                Type listType = new TypeToken<List<AppVersion>>() {}.getType();
                return gson.fromJson(responseBody, listType);
            }
        }
    }
    ```

  </TabItem>

  <TabItem value="swift">
    ```swift
    extension API {
        func getAppVersions(accessToken: String, profileId: String) async throws -> [AppVersion] {
            var components = URLComponents()
            components.scheme = apiConfig.scheme
            components.host = apiConfig.host
            components.path = "/store/v2/profiles/\(profileId)/app-versions"
            guard let url = components.url else {
                throw HTTPError.invalidUrl
            }
            var request = URLRequest(url: url)
            request.httpMethod = HTTPMethod.GET.rawValue
            request.setValue("*/*", forHTTPHeaderField: "Accept")
            request.setValue("Bearer \(accessToken)", forHTTPHeaderField: "Authorization")

            return try await apiFetcher.request(request: request)
        }
    }
    ```

  </TabItem>

  <TabItem value="react-native">
    ```js
    export const getAppVersions = async (
      accessToken: string,
      profileId: string,
    ) => {
      const url = `https://api.appcircle.io/store/v2/profiles/${profileId}/app-versions`;

      try {
        const response = await axios.get(url, {
          headers: {
            Accept: '*/*',
            Authorization: `Bearer ${accessToken}`,
          },
        });

        return response.data;
      } catch (error) {
        console.error('Failed to get app versions:', error);
      }
    };
    ```

  </TabItem>
</Tabs>

#### Compare Current Version with Fetched App Versions to Identify Updates

Compare the current version with the fetched versions to identify the latest release. Configuration options can be adjusted to determine which version is considered the latest.

<Tabs defaultValue="swift" values={[
{ label: 'Swift', value: 'swift' },
{ label: 'Android', value: 'android' },
{ label: 'React Native', value: 'react-native' },
]}>

  <TabItem value="android">
    ```java
    import androidx.annotation.Nullable;
    import java.util.List;
    import java.util.ArrayList;

    /*
        You can implement your custom update check mechanism within this function.
        Currently, we convert the version to an integer and compare it with the 'CFBundleShortVersionString'.
        You may want to check other datas about the app version to write the update control mechanism please check
        /v2/profiles/{profileId}/app-versions at https://api.appcircle.io/openapi/index.html?urls.primaryName=store
    */
    public class VersionUtils {
        private List<Integer> versionComponents(String version) {
            List<Integer> components = new ArrayList<>();
            String[] parts = version.split("\\.");
            for (String part : parts) {
                try {
                    components.add(Integer.parseInt(part));
                } catch (NumberFormatException e) {
                    e.printStackTrace();
                }
            }
            return components;
        }

        public @Nullable AppVersion getLatestVersion(String currentVersion, List<AppVersion> appVersions) {
            AppVersion latestAppVersion = null;
            List<Integer> currentComponents = versionComponents(currentVersion);

            for (AppVersion app : appVersions) {
                List<Integer> latestComponents = versionComponents(app.getVersion());
                boolean isNewerVersion = false;

                for (int i = 0; i < Math.min(currentComponents.size(), latestComponents.size()); i++) {
                    int current = currentComponents.get(i);
                    int latest = latestComponents.get(i);
                    if (latest > current && app.getPublishType() != 0) {
                        isNewerVersion = true;
                        break;
                    } else if (latest < current) {
                        break;
                    }
                }

                if (isNewerVersion) {
                    latestAppVersion = app;
                }
            }

            return latestAppVersion;
        }
    }

    ```

  </TabItem>

  <TabItem value="swift">
    ```swift
    /*
        You can implement your custom update check mechanism within this function.
        Currently, we convert the version to an integer and compare it with the 'CFBundleShortVersionString'.
        You may want to check other datas about the app version to write the update control mechanism please check
        /v2/profiles/{profileId}/app-versions at https://api.appcircle.io/openapi/index.html?urls.primaryName=store
    */
    private func getLatestVersion(currentVersion: String, appVersions: [AppVersion]) -> AppVersion? {
        var latestAppVersion: AppVersion?
        let currentComponents = versionComponents(from: currentVersion)
        
        // Helper function to convert version string into an array of integers
        func versionComponents(from version: String) -> [Int] {
            return version.split(separator: ".").compactMap { Int($0) }
        }
        
        
        appVersions.forEach { app in
            // Convert versions to arrays of integers
            let latestComponents = versionComponents(from: app.version)
            
            // Compare versions component by component
            for (current, latest) in zip(currentComponents, latestComponents) {
                // You can control to update None, Beta or Live publish types you have selected on Appcircle Enterprise Store
                if (latest > current && app.publishType != 0) {
                    latestAppVersion = app
                }
                
            }
        }
        
        return latestAppVersion
    }
    ```

  </TabItem>

  <TabItem value="react-native">
    ```js
    import {Platform} from 'react-native';
    
    interface AppVersion {
      id: string;
      version: string;
      publishType: number;
    }
    
    /*
        You can implement your custom update check mechanism within this function.
        Currently, we convert the version to an integer and compare it with the 'CFBundleShortVersionString'.
        You may want to check other datas about the app version to write the update control mechanism please check
        /v2/profiles/{profileId}/app-versions at https://api.appcircle.io/openapi/index.html?urls.primaryName=store
    */
    const getLatestVersion = (
      currentVersion: string,
      appVersions: AppVersion[],
    ): AppVersion | undefined => {
      let latestAppVersion: AppVersion | undefined;
      // Helper function to convert version string into an array of integers
      const versionComponents = (version: string): number[] => {
        return version
          .split('.')
          .map(Number)
          .filter(num => !isNaN(num));
      };

      const currentComponents = versionComponents(currentVersion);

      appVersions.forEach(app => {
        // Convert versions to arrays of integers
        const latestComponents = versionComponents(app.version);

        // Compare versions component by component
        for (
          let i = 0;
          i < Math.min(currentComponents.length, latestComponents.length);
          i++
        ) {
          const current = currentComponents[i];
          const latest = latestComponents[i];

          // You can control to update None, Beta or Live publish types you have selected on Appcircle Enterprise Store
          if (latest > current && app.publishType !== 0) {
            latestAppVersion = app;
          }
        }
      });

      return latestAppVersion;
    };
    ```

  </TabItem>
</Tabs>

#### Updating the App

If a newer version is available, generate the platform-specific download URL and return it for background opening later.

<Tabs defaultValue="swift" values={[
{ label: 'Swift', value: 'swift' },
{ label: 'Android', value: 'android' },
{ label: 'React Native', value: 'react-native' },
]}>

  <TabItem value="android">
    ```java
    public String getAppVersionName() {
        try {
            PackageInfo pInfo = this.getPackageManager().getPackageInfo(getPackageName(), 0);
            return  pInfo.versionName;
        } catch (PackageManager.NameNotFoundException e) {
            e.printStackTrace();
        }
        return "NOT_FOUND";
    }

    private class GetAccessTokenTask extends AsyncTask<String, Void, AuthModel> {
        @Override
        protected AuthModel doInBackground(String... params) {
            try {
                AuthModel response = AuthService.getAccessToken(params[0]);
                fetchAppVersions(response.getAccessToken(), Environment.PROFILE_ID);

                return response;
            } catch (IOException e) {
                e.printStackTrace();
                return null;
            }
        }
    }

    private void fetchAppVersions(final String accessToken, final String profileId) {
        new Thread(new Runnable() {
            @Override
            public void run() {
                try {
                    final List<AppVersion> appVersions = appService.getAppVersions(accessToken, profileId);
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            String versionName = getAppVersionName();

                            if (versionName != null) {
                                VersionUtils versionUtils = new VersionUtils();

                                @Nullable  AppVersion latestVersion = versionUtils.getLatestVersion(versionName, appVersions);
                                if (latestVersion != null) {
                                    showUpdateDialog(Environment.STORE_PREFIX, profileId, latestVersion, accessToken, "USER_EMAIL");
                                }
                            } else {
                                Log.d("MainActivity", "Current Version Not Found");
                            }
                        }
                    });
                } catch (final IOException e) {
                    e.printStackTrace();
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {
                            Log.e("APIError", "Error fetching app versions", e);
                        }
                    });
                }
            }
        }).start();
    }
    ```

  </TabItem>

  <TabItem value="swift">
    ```swift
    func checkForUpdate(pat: String, profileId: String, storeId: String, userEmail: String) async throws -> URL? {
        do {
            let authResponse = try await self.authApi.getAccessToken(pat: pat)
            let appVersions = try await self.api.getAppVersions(accessToken: authResponse.accessToken, profileId: profileId)
            let bundle = Bundle.main
            let currentVersion = bundle.infoDictionary?["CFBundleShortVersionString"] as? String
            guard let currentVersion = currentVersion else {
                print("'CFBundleShortVersionString' Version Could Not found")
                return nil
            }
            
            guard let availableVersion = getLatestVersion(currentVersion: currentVersion, appVersions: appVersions) else {
                print("App is up to date!")
                return nil
            }
            
            guard let downloadURL  = URL(string: "itms-services://?action=download-manifest&url=https://\(storeId).store.appcircle.io/api/profile/\(profileId)/appVersions/\(availableVersion.id)/download-update/\(authResponse.accessToken)/user/\(userEmail)") else {
                print("Latest Version URL could not created")
                return nil
            }
            
            return downloadURL
        } catch {
            print(error)
            return nil
        }
    }    
    ```

  </TabItem>

  <TabItem value="react-native">
    ```js
    export const checkForUpdate = async (params: {
      pat: string;
      storePrefix: string;
      iOSProfileId: string;
      androidProfileId: string;
      currentVersion: string;
      userEmail: string;
    }): Promise<{updateURL: string; version: string} | undefined> => {
      try {
        const {access_token} = await getACToken({pat: params.pat});
    
        const appVersions = await getAppVersions(
          access_token,
          Platform.OS === 'ios' ? params.iOSProfileId : params.androidProfileId,
        );
    
        const latestVersion = getLatestVersion(params.currentVersion, appVersions);
        if (latestVersion) {
          const downloadUrl = createDownloadUrl(
            params.storePrefix,
            Platform.OS === 'ios' ? params.iOSProfileId : params.androidProfileId,
            latestVersion.id,
            access_token,
            params.userEmail,
          );
    
          if (!downloadUrl) {
            console.error('Failed to create download URL');
            return undefined;
          }
    
          return {
            updateURL: downloadUrl,
            version: latestVersion.version,
          };
        }
      } catch (error) {
        console.error('Failed to determine if an update is available', error);
      }
    };

    const createDownloadUrl = (
      storeId: string,
      profileId: string,
      availableVersionId: string,
      accessToken: string,
      email: string,
    ): string | null => {
      const baseUrl = `https://${storeId}.store.appcircle.io/api/profile/${profileId}/appVersions/${availableVersionId}/download-update/${accessToken}/user/${email}`;
      const downloadUrl = `itms-services://?action=download-manifest&url=${baseUrl}`;

      try {
        return Platform.OS === 'ios' ? downloadUrl : baseUrl;
      } catch {
        console.error('Latest Version URL could not be created');
        return null;
      }
    };
    ```

  </TabItem>
</Tabs>

### How to Prompt an Alert and Install the Latest Release

After obtaining the download URL for a newer version, display an alert with options to update or cancel. Customize the alert based on your requirements, such as omitting the cancel button for mandatory updates.

<Tabs defaultValue="swift" values={[
{ label: 'Swift', value: 'swift' },
{ label: 'Android', value: 'android' },
{ label: 'React Native', value: 'react-native' },
]}>

  <TabItem value="android">
    ```java

    private AppService appService = new AppService();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        new GetAccessTokenTask().execute(Environment.PAT);
    }

    private void showUpdateDialog(final String storePrefix, final String profileId, final AppVersion appVersion, final String accessToken, final String userEmail) {
            new AlertDialog.Builder(this)
                    .setTitle("Update Available")
                    .setMessage(appVersion.getVersion() + " version is available. Do you want to update?")
                    .setPositiveButton("Update", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            String baseDownloadURL = "https://%s.store.appcircle.io/api/profile/%s/appVersions/%s/download-update/%s/user/%s";
                            Uri downloadURL =  Uri.parse(String.format(baseDownloadURL, storePrefix, profileId, appVersion.getId(), accessToken, userEmail));
                            Intent intent = new Intent(Intent.ACTION_VIEW, downloadURL);
                            startActivity(intent);
                        }
                    })
                    .setNegativeButton("Cancel", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            // Code to run when "Cancel" is pressed
                            dialog.dismiss();
                        }
                    })
                    .show();
        }
    ```

  </TabItem>

  <TabItem value="swift">
    ```swift
    import SwiftUI

    @main
    struct AppcircleApp: App {
        @State private var updateURL: URL?
        @State private var showAlert: Bool = false


        var body: some Scene {
            WindowGroup {
                ContentView()
                    .onAppear {
                        let updateChecker = UpdateChecker()
                        Task {
                            if let updateURL = try await updateChecker.checkForUpdate(pat: Configs.pat, profileId: Configs.profileId, storePrefix: Configs.storeId, userEmail: "USER_EMAIL") {
                                self.updateURL = updateURL
                                self.showAlert.toggle()
                            }
                        }
                    }
                    .alert(isPresented: $showAlert) {
                        Alert(
                            title: Text("Update Available"),
                            message: Text("A new version is available Would you like to update?"),
                            primaryButton: .default(Text("Update"), action: {
                                UIApplication.shared.open(self.updateURL!) { isOpened in
                                    print("Application Opened")
                                }
                            }),
                            secondaryButton: .cancel(Text("Cancel"), action: {
                                // Handle the cancel action
                                print("User canceled the update")
                            })
                        )
                    }
            }
        }
    }
    ```

  </TabItem>

  <TabItem value="react-native">
    ```js
    import DeviceInfo from 'react-native-device-info';

    useEffect(() => {
      const updateControl = async (currentVersion: string) => {
        const updateInfo = await checkForUpdate({
          pat: Configs.PAT,
          storePrefix: Configs.storePrefix,
          iOSProfileId: Configs.PROFILE_ID,
          androidProfileId: Configs.ANDROID_PROFILE_ID,
          currentVersion,
          userEmail: 'USER_EMAIL',
        });
        if (updateInfo && updateInfo.updateURL && updateInfo.version) {
          Alert.alert(
            'Update Available',
            `${updateInfo.version} version is available.`,
            [
              {
                text: 'Update',
                onPress: () => {
                  Linking.openURL(updateInfo.updateURL);
                },
              },
              {
                text: 'Cancel',
              },
            ],
          );
        }
      };

      const getCurrentAppVersion = async () => {
        try {
          const currentVersion = await DeviceInfo.getVersion();
          const buildNumber = await DeviceInfo.getBuildNumber();
          updateControl(currentVersion);
        } catch (error) {
          console.error('Failed to get app version:', error);
        }
      };

      getCurrentAppVersion();
    }, []);
    ```

  </TabItem>
</Tabs>

:::caution
With API Level 29 and above, the in-app update experience must be managed by allowing users to download and manually install the update due to increased security restrictions.
