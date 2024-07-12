import { visit } from "unist-util-visit";
import ogs from "open-graph-scraper";
import isUrl from "is-url";

const remarkExternalUrlRef = () => {
  return async (tree) => {
    const textNodesToTransform = [];

    // Visit all text nodes in the tree
    visit(tree, "text", (node, index, parent) => {
      if (!parent || parent.type !== "paragraph") return; // Ensure parent is a paragraph

      // Check if the node value contains a URL
      const urls = node.value.split(/\s+/).filter((word) => isUrl(word));
      if (urls.length > 0) {
        textNodesToTransform.push({ parent, index, node, urls });
      }
    });

    for (let { parent, index, node, urls } of textNodesToTransform) {
      const newNodes = await transformNode(node.value, urls);
      parent.children.splice(index, 1, ...newNodes);
    }

    return tree;
  };
};

const transformNode = async (text, urls) => {
  const words = text.split(/\s+/);
  const nodes = [];

  for (const word of words) {
    if (isUrl(word) && urls.includes(word)) {
      const data = await fetchData(word);
      nodes.push({
        type: "mdxJsxFlowElement",
        name: "ExternalUrlRef",
        attributes: [
          { type: "mdxJsxAttribute", name: "url", value: word },
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
        children: [{ type: "text", value: word }],
        data: {
          _mdxExplicitJsx: true,
        },
      });
    } else {
      nodes.push({ type: "text", value: word + " " });
    }
  }

  return nodes;
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
      const description = result.ogDescription || "No description available";
      const image =
        result.ogImage?.url ||
        "https://cdn.appcircle.io/docs/assets/appcircle-logo.png";
      return { title, description, image };
    } else {
      throw new Error("OGS failed to fetch the title");
    }
  } catch (error) {
    return {
      title: new URL(url).hostname,
      description: "No description available",
      image: "https://cdn.appcircle.io/docs/assets/appcircle-logo.png",
    };
  }
};

module.exports = remarkExternalUrlRef;
