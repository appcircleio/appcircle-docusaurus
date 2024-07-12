import { visit } from "unist-util-visit";
import ogs from "open-graph-scraper";
import isUrl from "is-url";

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
  const data = await fetchData(url);
  return {
    type: "mdxJsxFlowElement",
    name: "ExternalUrlRef",
    attributes: [
      { type: "mdxJsxAttribute", name: "url", value: url },
      { type: "mdxJsxAttribute", name: "title", value: data.title },
      {
        type: "mdxJsxAttribute",
        name: "description",
        value: data.description || "No description available.",
      },
      {
        type: "mdxJsxAttribute",
        name: "image",
        value:
          data.image ||
          "https://cdn.appcircle.io/docs/assets/appcircle-logo.png",
      },
    ],
    children: [],
    data: {
      _mdxExplicitJsx: true,
    },
  };
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
