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

There are certain points to follow when adding screenshots to our documentation. Like the image size , Appcircle theme and pointer colors.

### Correct Screenshot Format

- Image size must be 1440x900.
- The image file name must be unique. It is good practice to use the Linear task ID within the file name to make it distinct. Example: 'BE-4000-example.png'.
- Screenshots must be full-size. Meaning, it is not recommended to cut out a certain area. We can use pointers and shapes to point out the necessary areas.
- Appcircle theme must be **Light Theme** on the screenshot.
- Active Organization must be **Appcircle Team** organization, please avoid using personal names.
- Displayed profiles such as a Build Profile or a Publish Profile should have the following name format: '**Example Publish Profile**'.
- The pointers and shapes used on the images should have the following color and format:

![Example](https://cdn.appcircle.io/docs/assets/be-4019-example.png)

- Color code: #f69c21

**Warning** : When uploading images through the GCloud CLI, it is important to ensure that the image name is not already present in the documentation within an uploaded image link. If an image with the same name already exists, it will be replaced by GCloud with the new one without a warning.

### Incorrect Screenshot Format

Do not use the following for a screenshot:

- Dark theme Appcircle UI.
- Organization or profile names that uses personal names.
- A snipped screenshot from a full size browser window.
- Shapes and pointers with different colors and format than the shared example image above.

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
