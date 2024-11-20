import React, { useState, useCallback } from "react";
import forge from "node-forge";

// Existing helper functions remain the same...
const toKebabCase = str => {
  return str
    .replace(/[A-Z]/g, match => `-${match.toLowerCase()}`)
    .replace(/^-/, "");
};

const removeLastNewLine = key => {
  return key.replace(/\n$/, "");
};

const generateRsaKeyPair = () => {
  const { privateKey, publicKey } = forge.rsa.generateKeyPair(2048);
  const privateKeyPem = forge.pki.privateKeyToPem(privateKey);
  const publicKeyPem = forge.pki.publicKeyToPem(publicKey);
  return {
    rsaPrivateKey: privateKeyPem,
    rsaPublicKey: publicKeyPem,
  };
};

const formatKeyWithIndentation = (key, indent) => {
  return key
    .split("\n")
    .map(line => `${indent}${line}`)
    .join("\n");
};

const generateRandomPassword = (
  length,
  minNumbers = 1,
  minUppercase = 1,
  minLowercase = 1
) => {
  const totalMinRequired = minNumbers + minUppercase + minLowercase;
  if (length < totalMinRequired) {
    throw new Error(
      "Password length must be greater than or equal to the sum of minimum requirements"
    );
  }

  const lowercase = "abcdefghijklmnopqrstuvwxyz";
  const uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const numbers = "0123456789";

  let password = [];

  for (let i = 0; i < minNumbers; i++) {
    password.push(numbers.charAt(Math.floor(Math.random() * numbers.length)));
  }

  for (let i = 0; i < minUppercase; i++) {
    password.push(
      uppercase.charAt(Math.floor(Math.random() * uppercase.length))
    );
  }

  for (let i = 0; i < minLowercase; i++) {
    password.push(
      lowercase.charAt(Math.floor(Math.random() * lowercase.length))
    );
  }

  const allChars = lowercase + uppercase + numbers;
  const remainingLength = length - password.length;

  for (let i = 0; i < remainingLength; i++) {
    password.push(allChars.charAt(Math.floor(Math.random() * allChars.length)));
  }

  for (let i = password.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [password[i], password[j]] = [password[j], password[i]];
  }

  return password.join("");
};

const YamlGenerator = () => {
  const [imageRegistryHost, setImageRegistryHost] = useState(
    "europe-west1-docker.pkg.dev"
  );
  const [imageRepositoryPath, setImageRepositoryPath] = useState(
    "appcircle/docker-registry"
  );
  const [imageTag, setImageTag] = useState("alpha-latest");
  const [appcircleMainDomain, setAppcircleMainDomain] = useState(
    "appcircle.spacetech.com"
  );
  const [organizationName, setOrganizationName] = useState("spacetech");
  const [initialUserEmail, setInitialUserEmail] = useState("admin@example.com");
  const [initialUserPassword, setInitialUserPassword] = useState(
    "superSecretAppcirclePassword1234"
  );
  const [requiresAuth, setRequiresAuth] = useState(true);
  const [registryUsername, setRegistryUsername] = useState("_json_key");
  const [registryPassword, setRegistryPassword] = useState(
    "Content of the cred.json file"
  );
  const [yamlContent, setYamlContent] = useState("");

  // New state for SSL/TLS certificates
  const [sslCert, setSslCert] = useState("");
  const [sslKey, setSslKey] = useState("");
  const [caCert, setCaCert] = useState("");

  const handleFileRead = useCallback((file, setter) => {
    const reader = new FileReader();
    reader.onload = e => {
      setter(e.target.result);
    };
    reader.readAsText(file);
  }, []);

  const handleCertFileChange = useCallback(
    event => {
      const file = event.target.files[0];
      if (file) {
        handleFileRead(file, setSslCert);
      }
    },
    [handleFileRead]
  );

  const handleKeyFileChange = useCallback(
    event => {
      const file = event.target.files[0];
      if (file) {
        handleFileRead(file, setSslKey);
      }
    },
    [handleFileRead]
  );
  const handleCaFileChange = useCallback(
    event => {
      const file = event.target.files[0];
      if (file) {
        handleFileRead(file, setCaCert);
      }
    },
    [handleFileRead]
  );

  const handleGenerate = () => {
    const imageRegistry = `${imageRegistryHost}`;
    const imageRepositoryPathWithRegistry = `${imageRegistry}/${imageRepositoryPath}/`;

    const initialOrganizationId = crypto.randomUUID();
    const keycloakAdminPassword = generateRandomPassword(18);
    const postgresPassword = generateRandomPassword(32);

    const indent = "      ";
    var { rsaPrivateKey, rsaPublicKey } = generateRsaKeyPair();
    const formattedDistRsaPrivateKey = formatKeyWithIndentation(
      removeLastNewLine(rsaPrivateKey),
      indent
    );
    const formattedDistRsaPublicKey = formatKeyWithIndentation(
      removeLastNewLine(rsaPublicKey),
      indent
    );

    var { rsaPrivateKey, rsaPublicKey } = generateRsaKeyPair();
    const formattedStoreRsaPrivateKey = formatKeyWithIndentation(
      removeLastNewLine(rsaPrivateKey),
      indent
    );
    const formattedStoreRsaPublicKey = formatKeyWithIndentation(
      removeLastNewLine(rsaPublicKey),
      indent
    );

    let dockerRegistrySecret = "";
    if (requiresAuth) {
      const authString = `${registryUsername}:${registryPassword}`;
      const base64EncodedAuthString = btoa(authString);
      dockerRegistrySecret = `{\"auths\":{\"${imageRegistry}\":{\"auth\": \"${base64EncodedAuthString}\"}}}`;
    }

    // Format SSL/TLS certificates with proper indentation
    const formattedSslCert = sslCert
      ? formatKeyWithIndentation(sslCert, indent)
      : "";
    const formattedSslKey = sslKey
      ? formatKeyWithIndentation(sslKey, indent)
      : "";
    const formattedCaCert = caCert
      ? formatKeyWithIndentation(caCert, indent)
      : "";

    const yaml = `global:
  appEnvironment: 'Production'
  urls:
    domainName: .${appcircleMainDomain}
    scheme: https
  mail:
    smtp:
      domain: 'smtp.example.com'
      host: 'smtp.example.com'
      port: '587'
      from: 'appcircle@example.com'
      ssl: 'false'
      tls: 'true'
      auth: 'true'
      username: 'smtpUsername'
      password: 'superSecretSMTPPassword'
  imageRegistry: ${imageRegistry}
  imageRepositoryPath: ${imageRepositoryPath}
  imageTag: ${imageTag}
  ingressClassName: "nginx"
  ${requiresAuth ? `containerRegistrySecret: '${dockerRegistrySecret}'` : ""}
  tlsWildcard:
    cert: |
${formattedSslCert}
    key: |
${formattedSslKey}
    ca: |
${formattedCaCert}
auth:
  auth-keycloak:
    organizationName: ${organizationName}
    initialUsername: '${initialUserEmail}'
    initialPassword: '${initialUserPassword}'
    image:
      repository: ${imageRepositoryPathWithRegistry}appcircle-keycloak
  server:
    image:
      repository: ${imageRepositoryPathWithRegistry}appcircle-vault
webeventredis:
  tls:
    enabled: true
  ingress:
    tls: true
    enabled: true
distribution:
  distribution-testerapi:
    rsaPrivateKey: |
${formattedDistRsaPrivateKey}
    rsaPublicKey: |
${formattedDistRsaPublicKey}
store:
  store-api:
    rsaPrivateKey: |
${formattedStoreRsaPrivateKey}
    rsaPublicKey: |
${formattedStoreRsaPublicKey}`;

    setYamlContent(yaml);
  };

  return (
    <div className="container">
      <div className="form-group">
        <label>
          The Organization Name:
          <input
            type="text"
            className="input-field input-field-long"
            value={organizationName}
            onChange={e => setOrganizationName(e.target.value)}
          />
        </label>
      </div>
      <div className="form-group">
        <label>
          Appcircle Main Domain:
          <input
            type="text"
            className="input-field input-field-long"
            value={appcircleMainDomain}
            onChange={e => setAppcircleMainDomain(e.target.value)}
          />
        </label>
      </div>
      <div className="form-group">
        <label>
          Appcircle Initial User Email:
          <input
            type="text"
            className="input-field input-field-long"
            value={initialUserEmail}
            onChange={e => setInitialUserEmail(e.target.value)}
          />
        </label>
      </div>
      <div className="form-group">
        <label>
          Appcircle Initial User Password:
          <input
            type="text"
            className="input-field input-field-long"
            value={initialUserPassword}
            onChange={e => setInitialUserPassword(e.target.value)}
          />
        </label>
      </div>
      <div className="form-group">
        <label>
          Container Image Registry Host:
          <input
            type="text"
            className="input-field input-field-long"
            value={imageRegistryHost}
            onChange={e => setImageRegistryHost(e.target.value)}
          />
        </label>
      </div>
      <div className="form-group">
        <label>
          Container Image Repository Path:
          <input
            type="text"
            className="input-field input-field-long"
            value={imageRepositoryPath}
            onChange={e => setImageRepositoryPath(e.target.value)}
          />
        </label>
      </div>
      <div className="form-group">
        <label>
          Container Image Tag:
          <input
            type="text"
            className="input-field input-field-long"
            value={imageTag}
            onChange={e => setImageTag(e.target.value)}
          />
        </label>
      </div>
      <div className="form-group">
        <label>
          Container Image Registry Requires Auth:
          <input
            type="checkbox"
            className="input-checkbox"
            checked={requiresAuth}
            onChange={e => setRequiresAuth(e.target.checked)}
          />
        </label>
      </div>
      {requiresAuth && (
        <>
          <div className="form-group">
            <label>
              Container Image Registry Username:
              <input
                type="text"
                className="input-field input-field-long"
                value={registryUsername}
                onChange={e => setRegistryUsername(e.target.value)}
              />
            </label>
          </div>
          <div className="form-group">
            <label>
              Container Image Registry Password:
              <input
                type="text"
                className="input-field input-field-long"
                value={registryPassword}
                onChange={e => setRegistryPassword(e.target.value)}
              />
            </label>
          </div>
        </>
      )}
      <div className="form-group">
        <label>
          SSL/TLS Certificate File:
          <input
            type="file"
            className="input-field"
            onChange={handleCertFileChange}
            accept=".crt,.pem"
          />
        </label>
      </div>
      <div className="form-group">
        <label>
          SSL/TLS Private Key File:
          <input
            type="file"
            className="input-field"
            onChange={handleKeyFileChange}
            accept=".key,.pem"
          />
        </label>
      </div>
      <div className="form-group">
        <label>
          CA Certificate File:
          <input
            type="file"
            className="input-field"
            onChange={handleCaFileChange}
            accept=".crt,.pem"
          />
        </label>
      </div>
      <div className="form-group">
        <button className="generate-btn" onClick={handleGenerate}>
          Generate YAML
        </button>
      </div>
      {yamlContent && (
        <div className="yaml-output">
          <pre>{yamlContent}</pre>
        </div>
      )}
    </div>
  );
};

export default YamlGenerator;
