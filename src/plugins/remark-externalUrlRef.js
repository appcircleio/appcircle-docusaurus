const visit = require("unist-util-visit");
const ogs = require("open-graph-scraper");
const u = require("unist-builder");
const isUrl = require("is-url");

const remarkExternalUrlRef = () => {
  return async (tree) => {
    const textNodesToTransform = [];

    visit(tree, "text", (node, index, parent) => {
      if (!parent) return; // Skip if no parent is found

      const urls = node.value.split(/\s+/).filter((word) => isUrl(word));
      if (urls.length > 0) {
        textNodesToTransform.push({ parent, index, urls });
      }
    });

    for (let { parent, index, urls } of textNodesToTransform) {
      const newNodes = await Promise.all(urls.map((url) => transformNode(url)));
      parent.children.splice(index, 1, ...newNodes);
    }

    return tree;
  };
};

const transformNode = async (url) => {
  try {
    const data = await fetchData(url);
    // Escape quotes inside the strings to prevent breaking JSX syntax
    const title = data.title.replace(/"/g, "&quot;");
    const description = data.description
      ? data.description.replace(/"/g, "&quot;")
      : "";
    const image =
      data.image || "https://cdn.appcircle.io/docs/assets/appcircle-logo.png";

    return u(
      "jsx",
      `<ExternalUrlRef url="${url}" title="${title}" description="${description}" image="${image}" />`
    );
  } catch (error) {
    console.error(`Error transforming node for URL ${url}: ${error}`);
    return u("text", url); // Return original URL as text if there's an error
  }
};

const fetchData = async (url) => {
  const options = {
    url,
    headers: {
      "User-Agent":
        "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
    },
  };
  try {
    const { result } = await ogs(options);
    if (result.success) {
      const title = result.ogTitle || new URL(url).hostname;
      const description = result.ogDescription || "No description available"; // Default description
      const image =
        result.ogImage && result.ogImage.url
          ? result.ogImage.url
          : "https://cdn.appcircle.io/docs/assets/appcircle-logo.png"; // Default image
      return { title, description, image };
    } else {
      throw new Error("OGS failed to fetch the title");
    }
  } catch (error) {
    // console.error(`Error fetching data for URL ${url}: ${error}`); // Commented out to prevent spamming the console
    return {
      title: new URL(url).hostname,
      description: "No description available", // Default description
      image: "https://cdn.appcircle.io/docs/assets/appcircle-logo.png", // Default image
    };
  }
};

module.exports = remarkExternalUrlRef;
