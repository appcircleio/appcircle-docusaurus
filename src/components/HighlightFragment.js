import React, { useEffect } from "react";

const HighlightFragment = () => {
  useEffect(() => {
    const applyHighlight = () => {
      const url = window.location.href;
      const fragmentIndex = url.indexOf(":~:");

      console.log("url", url);

      if (fragmentIndex > -1) {
        const fragment = url.substring(fragmentIndex + 3);
        const decodedFragment = decodeURIComponent(fragment);

        const textToHighlight = decodedFragment.split("=")[1];
        if (textToHighlight) {
          const range = document.createRange();
          const textNodes = document.createTreeWalker(
            document.body,
            NodeFilter.SHOW_TEXT,
            null,
            false
          );
          let node;
          while ((node = textNodes.nextNode())) {
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
    };

    const observer = new MutationObserver(() => {
      setTimeout(applyHighlight, 100); // Ensure all mutations are handled
    });

    observer.observe(document.body, { childList: true, subtree: true });

    window.addEventListener("load", applyHighlight);

    return () => {
      observer.disconnect();
      window.removeEventListener("load", applyHighlight);
    };
  }, []);

  return null;
};

export default HighlightFragment;
