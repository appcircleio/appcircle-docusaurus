import React, { useEffect } from "react";

const HighlightFragment = () => {
  useEffect(() => {
    const applyHighlight = () => {
      console.log("Applying highlight");
      const url = window.location.href;
      const fragmentIndex = url.indexOf(":~:");

      if (fragmentIndex > -1) {
        const fragment = url.substring(fragmentIndex + 3);
        const decodedFragment = decodeURIComponent(fragment);
        console.log("Decoded fragment:", decodedFragment);

        const textToHighlight = decodedFragment.split("=")[1];
        console.log("Text to highlight:", textToHighlight);
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
              console.log("Found text node:", nodeText);
              range.setStart(node, nodeIndex);
              range.setEnd(node, nodeIndex + textToHighlight.length);
              const highlight = document.createElement("span");
              highlight.style.backgroundColor = "yellow";
              range.surroundContents(highlight);
              console.log("Applied highlight");
              break;
            }
          }
        }
      }
    };

    const handleLoad = () => {
      console.log("Page loaded");
      setTimeout(() => {
        requestAnimationFrame(applyHighlight);
      }, 1000); // Ensure delay to account for all scripts
    };

    window.addEventListener("load", handleLoad);
    window.addEventListener("DOMContentLoaded", handleLoad);

    return () => {
      window.removeEventListener("load", handleLoad);
      window.removeEventListener("DOMContentLoaded", handleLoad);
    };
  }, []);

  return null;
};

export default HighlightFragment;
