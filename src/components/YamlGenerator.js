import React, { useState } from "react";
import forge from "node-forge"; // Importing node-forge for RSA key generation

// Helper function to convert camelCase or PascalCase to kebab-case
const toKebabCase = str => {
  return str
    .replace(/[A-Z]/g, match => `-${match.toLowerCase()}`)
    .replace(/^-/, ""); // Remove leading hyphen if any
};

const removeLastNewLine = key => {
  return key.replace(/\n$/, "");
};

// Helper function to generate RSA key pair
const generateRsaKeyPair = () => {
  const { privateKey, publicKey } = forge.rsa.generateKeyPair(2048); // Generate 2048-bit RSA key pair

  const privateKeyPem = forge.pki.privateKeyToPem(privateKey); // Convert private key to PEM format
  const publicKeyPem = forge.pki.publicKeyToPem(publicKey); // Convert public key to PEM format

  return {
    rsaPrivateKey: privateKeyPem,
    rsaPublicKey: publicKeyPem,
  };
};

// Helper function to format RSA keys with indentation
const formatKeyWithIndentation = (key, indent) => {
  return key
    .split("\n")
    .map(line => `${indent}${line}`)
    .join("\n");
};

const generateKeycloakClientsYaml = () => {
  const clients = [
    "appcircleWeb",
    "reportingServer",
    "licenseServer",
    "storeServer",
    "storeWeb",
    "storeAdminService",
    "distributionServer",
    "distributionAdminService",
    "distributionTesterWeb",
    "publishServer",
    "buildServer",
  ];
  let clientYaml = "";
  clients.forEach(client => {
    clientYaml += `
      ${toKebabCase(client)}:
        id: ${toKebabCase(client)}
        secret: ${crypto.randomUUID()}`;
  });
  return clientYaml;
};

function generateRandomPassword(length) {
  const chars =
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
  let password = "";
  for (let i = 0; i < length; i++) {
    password += chars.charAt(Math.floor(Math.random() * chars.length));
  }
  return password;
}

const YamlGenerator = () => {
  const [imageRegistryHost, setImageRegistryHost] = useState(
    "europe-west1-docker.pkg.dev"
  );
  const [imageRepositoryPath, setImageRepositoryPath] = useState(
    "appcircle/docker-registry"
  );
  const [imageTag, setImageTag] = useState("v3.22.1");
  const [appcircleMainDomain, setAppcircleMainDomain] = useState(
    "appcircle.spacetech.com"
  );
  const [initialUserEmail, setInitialUserEmail] = useState("admin@example.com");
  const [initialUserPassword, setInitialUserPassword] = useState(
    "superSecretAppcirclePassword1234"
  );
  const [requiresAuth, setRequiresAuth] = useState(true);
  const [registryUsername, setRegistryUsername] = useState("_json_key");
  const [registryPassword, setRegistryPassword] = useState("Content of the cred.json file");
  const [yamlContent, setYamlContent] = useState("");

  const handleGenerate = () => {
    const imageRegistry = `${imageRegistryHost}`;
    const imageRepositoryPathWithRegistry = `${imageRegistry}/${imageRepositoryPath}/`;

    const webeventredisPassword = generateRandomPassword(32);
    const keycloakAdminPassword = generateRandomPassword(12);
    const postgresPassword = generateRandomPassword(32);

    const indent = "      "; // Set the appropriate indentation
    var { rsaPrivateKey, rsaPublicKey } = generateRsaKeyPair(); // Generate RSA keys
    const formattedDistRsaPrivateKey = formatKeyWithIndentation(
      removeLastNewLine(rsaPrivateKey),
      indent
    );
    const formattedDistRsaPublicKey = formatKeyWithIndentation(
      removeLastNewLine(rsaPublicKey),
      indent
    );

    var { rsaPrivateKey, rsaPublicKey } = generateRsaKeyPair(); // Generate RSA keys
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

    // @TODO: all passwords are not included. Make a checklist.
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
auth:
  auth-keycloak:
    organizationName: spacetech
    image:
      repository: ${imageRepositoryPathWithRegistry}appcircle-keycloak
    admin:
      username: admin
      password: '${keycloakAdminPassword}'
    initialUsername: '${initialUserEmail}'
    initialPassword: '${initialUserPassword}'
  auth-postgresql:
    auth:
      password: '${postgresPassword}'
  server:
    image:
      repository: ${imageRepositoryPathWithRegistry}appcircle-vault
webeventredis:
  auth:
    password: '${webeventredisPassword}'
  master:
    preExecCmds: ''
  tls:
    enabled: false
  ingress:
    tls: false
    enabled: true
keycloak:
  clients:${generateKeycloakClientsYaml()}
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
          Image Registry Host:
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
          Image Repository Path:
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
          Image Tag:
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
          Image Registry Requires Auth:
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
              Registry Username:
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
              Registry Password:
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
