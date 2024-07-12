import { visit } from "unist-util-visit";
import ogs from "open-graph-scraper";
import isUrl from "is-url";

const remarkExternalUrlRef = () => {
  return async (tree) => {
    const nodesToTransform = [];

    visit(tree, "text", (node, index, parent) => {
      if (!parent || parent.type !== "paragraph") return; // Ensure parent is a paragraph

      const words = node.value.split(/(\s+)/).filter(Boolean); // Preserve spaces as separate nodes
      words.forEach((word, wordIndex) => {
        if (isUrl(word)) {
          nodesToTransform.push({ parent, node, index, word, wordIndex });
        }
      });
    });

    for (let { parent, node, index, word, wordIndex } of nodesToTransform) {
      const newNodes = await transformNode(word);
      const surroundingText = node.value.split(word);
      parent.children.splice(
        index,
        1,
        {
          type: "text",
          value: surroundingText[0],
        },
        ...newNodes,
        {
          type: "text",
          value: surroundingText[1],
        }
      );
    }

    return tree;
  };
};

const transformNode = async (url) => {
  const data = await fetchData(url);
  return [
    {
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
      children: [{ type: "text", value: url }],
      data: {
        _mdxExplicitJsx: true,
      },
    },
  ];
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
