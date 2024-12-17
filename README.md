# Documentation Guidelines

Welcome to the Docusaurus documentation repository. When contributing documentation, please adhere to the following standards to ensure consistency and clarity.

## Document Header

Each document should start with a header section that defines metadata used for SEO and navigation. Please follow the structure below:

```yaml
---
title: Title of the Document
description: A concise SEO-friendly description, limited to 160 characters.
tags: [tag1, tag2, tag3]
---
```

- **title**: The title of the document.
- **description**: This is critical for SEO. Keep it under 160 characters to ensure full visibility in search engine results.
- **tags**: Include relevant tags that describe the document's content. This helps in categorizing the documentation.

**Warning:** When setting up **titles** and **descriptions**, it is important to avoid duplicating values from other areas within the documentation. **Titles** and **descriptions** must be unique.
Otherwise, it will cause SEO-related issues.

## Linking Strategy

When adding links to other documentation pages, use absolute path links starting from the root of the documentation directory.

### Correct Link Format

Use this format for linking within the documentation:

```markdown
'/category/subcategory/target-page'
```

For example:

```markdown
'/build/build-process-management/build-profile-branch-operations'
```

### Incorrect Link Format

Do not use relative paths like the following:

```markdown
'../../category/subcategory/target-page' // This is incorrect
```

```markdown
'./target-page' // This is incorrect
```

```markdown
'./docs/build/build-process-management/build-profile-branch-operations.md' // This is incorrect
```

## Screenshot Strategy

There are specific guidelines for adding screenshots to our documentation, such as image size, Appcircle theme, and pointer colors.

### Correct Screenshot Format

- The dimensions of the image must be 1440x900 pixels.
- The image file name must be unique. Use a descriptive name to ensure uniqueness. Example: 'BE-4000-example.png'.
- Please ensure that screenshots are full-size. Avoid cropping specific areas, and instead, use pointers and shapes to highlight the necessary areas.
- Appcircle theme must be **Light Theme** on the screenshot.
- Active Organization must be **Appcircle Team** organization, please avoid using personal names.
- Profiles that are displayed, such as a Build Profile or a Publish Profile, should adhere to the following naming format: '**Example Publish Profile**'.
- The images should use pointers and shapes that have specific colors and formats as follows:

![Example](https://cdn.appcircle.io/docs/assets/BE-4019-example.png)

- Color code: #f69c21

### Screenshot Alt Text

When adding screenshots, please include alt text that describes the image content. This is important for accessibility and SEO purposes.

```jsx
<Screenshot
  url="https://cdn.appcircle.io/docs/assets/enable-sso_v3.png"
  alt="Enable SSO for Organizations"
/>
```

### Incorrect Screenshot Format

Do not use the following items when taking screenshots:

- Dark theme Appcircle UI.
- Organization or profile names that uses personal names.
- A snipped screenshot from a full size browser window.
- Shapes and pointers with different colors and format than the shared example image above.

## Tag Strategy

Tags are used to categorize and group documentation pages. When adding tags to a document, please follow these guidelines:

- Tags should be lowercase.
- Tags should be relevant to the content of the document.
- Before adding a new tag, check `tags.yml` to see if a similar tag already exists.
- If a similar tag exists, use the existing tag instead of creating a new one.
- If a similar tag does not exist, create a new tag in `tags.yml` and use it in the document.

### Creating a New Tag

When creating a new tag, add it to the `tags.yml` file in the following format:

```yaml
tag:
  label: Tag Name
  description: Description of the tag.
  permalink: /tag

"access-management":
  label: Access Management
  description: Manage access to your projects and organizations.
  permalink: /access-management
```

Please note that tags are case-sensitive. For example, 'Build' and 'build' are considered different tags.

## Contribution Guidelines

1. Fork the repository and create a new branch for your document.
2. Write your documentation following the standards outlined above.
3. Submit a pull request with a clear description of the changes.

Thank you for contributing to our documentation. Your efforts help improve the experience for all Appcircle users.

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
