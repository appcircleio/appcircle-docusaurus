# Documentation Guidelines

Welcome to the Docusaurus documentation repository. When contributing documentation, please adhere to the following standards to ensure consistency and clarity.

## Document Header

Each document should start with a header section that defines metadata used for SEO and navigation. Please follow the below structure:

```yaml
---
title: Title of the Document
description: A concise SEO-friendly description, limited to 160 characters.
tags: [tag1, tag2, tag3]
---
```

- **title**: The title of the document.
- **description**: his is critical for SEO. Keep it under 160 characters to ensure full visibility in search engine results.
- **tags**: Include relevant tags that describe the document's content. This helps in categorizing the documentation.

## Linking Strategy

When adding links to other documentation pages, use absolute path links starting from the root of the documentation directory.

### Correct Link Format

Use this format for linking within the documentation:

```markdown
'/category/subcategory/target-page'
```

### Incorrect Link Format

Do not use relative paths like the following:

```markdown
'../../category/subcategory/target-page' // This is incorrect
```

## Contribution Guidelines

1. Fork the repository and create a new branch for your document.
2. Write your documentation following the standards outlined above.
3. Submit a pull request with a clear description of the changes.

Thank you for contributing to our documentation. Your efforts help improve the experience for all our users.

# Website

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

### Installation

```
$ yarn
```

### Local Development

```
$ yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```
$ yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```
$ USE_SSH=true yarn deploy
```

Not using SSH:

```
$ GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.
