import React, { useEffect } from "react";

const HighlightFragment = () => {
  useEffect(() => {
    const applyHighlight = () => {
      setTimeout(() => {
        const url = window.location.href;
        const fragmentIndex = url.indexOf(":~:");

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
      }, 2000); // Adjust the delay as needed
    };

    applyHighlight();
  }, []);

  return null;
};

export default HighlightFragment;
