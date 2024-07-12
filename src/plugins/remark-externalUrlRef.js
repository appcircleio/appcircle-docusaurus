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

    // Inject a script to reapply highlight after the content has been processed
    const highlightScriptNode = {
      type: "mdxJsxFlowElement",
      name: "script",
      attributes: [
        { type: "mdxJsxAttribute", name: "type", value: "text/javascript" },
        {
          type: "mdxJsxAttribute",
          name: "dangerouslySetInnerHTML",
          value: {
            __html: `
              setTimeout(() => {
                const url = window.location.href;
                const fragmentIndex = url.indexOf(':~:');

                if (fragmentIndex > -1) {
                  const fragment = url.substring(fragmentIndex + 3);
                  const decodedFragment = decodeURIComponent(fragment);

                  const textToHighlight = decodedFragment.split('=')[1];
                  if (textToHighlight) {
                    const range = document.createRange();
                    const textNodes = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
                    let node;
                    while (node = textNodes.nextNode()) {
                      const nodeText = node.nodeValue;
                      const nodeIndex = nodeText.indexOf(textToHighlight);
                      if (nodeIndex !== -1) {
                        range.setStart(node, nodeIndex);
                        range.setEnd(node, nodeIndex + textToHighlight.length);
                        const highlight = document.createElement("span");
                        highlight.style.backgroundColor = "yellow";
                        range.surroundContents(highlight);
                        break;
                      }
                    }
                  }
                }
              }, 2000); // Adjust the delay as needed
            `,
          },
        },
      ],
      children: [],
      data: {
        _mdxExplicitJsx: true,
      },
    };

    tree.children.push(highlightScriptNode);

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
