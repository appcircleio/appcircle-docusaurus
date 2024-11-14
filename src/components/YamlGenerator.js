import React, { useState } from "react";
import { v4 as uuidv4 } from "uuid"; // Importing uuidv4 from the uuid library
import forge from "node-forge"; // Importing node-forge for RSA key generation

// Helper function to convert camelCase or PascalCase to kebab-case
const toKebabCase = str => {
  return str
    .replace(/[A-Z]/g, match => `-${match.toLowerCase()}`)
    .replace(/^-/, ""); // Remove leading hyphen if any
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
        secret: ${uuidv4()}`;
  });
  return clientYaml;
};

function generateRandomPassword() {
  return (
    Math.random().toString(36).slice(2) +
    Math.random().toString(36).toUpperCase().slice(2)
  );
}

const YamlGenerator = () => {
  const [imageRegistryHost, setImageRegistryHost] = useState(
    "europe-west1-docker.pkg.dev"
  );
  const [imageRepositoryPath, setImageRepositoryPath] = useState(
    "appcircle/docker-registry"
  );
  const [imageTag, setImageTag] = useState("v3.22.1");
  const [yamlContent, setYamlContent] = useState("");

  const handleGenerate = () => {
    const imageRegistry = `${imageRegistryHost}`;
    const imageRepositoryPathWithRegistry = `${imageRegistry}/${imageRepositoryPath}/`;

    const webeventredisPassword = generateRandomPassword();

    const { rsaPrivateKey, rsaPublicKey } = generateRsaKeyPair(); // Generate RSA keys

    const yaml = `
global:
  imageRegistry: ${imageRegistry}
  imageRepositoryPath: ${imageRepositoryPath}
  imageTag: ${imageTag}

auth:
  auth-keycloak:
    image:
      repository: ${imageRepositoryPathWithRegistry}appcircle-keycloak:${imageTag}

minio:
  image:
    repository: ${imageRepositoryPathWithRegistry}minio/minio:${imageTag}

vault:
  server:
    image:
      repository: ${imageRepositoryPathWithRegistry}appcircle-vault:${imageTag}

webeventredis:
  auth:
    password: '${webeventredisPassword}'

keycloak:
  clients:${generateKeycloakClientsYaml()}

distribution:
  distribution-testerapi:
    rsaPrivateKey: |
      ${rsaPrivateKey}
    rsaPublicKey: |
      ${rsaPublicKey}`;

    setYamlContent(yaml);
  };

  return (
    <div className="container">
      <div className="form-group">
        <label>
          Image Registry Host:
          <input
            type="text"
            className="input-field"
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
            className="input-field"
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
            className="input-field"
            value={imageTag}
            onChange={e => setImageTag(e.target.value)}
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
