import { useEffect } from "react";

export function CookieSeal() {
  useEffect(() => {
    // Load CookieSeal styles
  const style = document.createElement("link");
  style.rel = "stylesheet";
  style.href = "https://assets.cookieseal.com/cookie-seal.css";
  style.type = "text/css";

    // Load CookieSeal script
  const script = document.createElement("script");
  script.src = "https://assets.cookieseal.com/cookie-seal.js";
  script.async = true;

  document.head.appendChild(style);

    script.onload = () => {
      const interval = setInterval(() => {
        const banner = document.getElementById("cookieseal-banner");

        if (banner) {
          clearInterval(interval);

          // 1. Customize Settings butonunu kaldır
          const customizeBtn = document.getElementById("cookieseal-banner-reject");
          if (customizeBtn?.parentElement) {
            customizeBtn.parentElement.removeChild(customizeBtn);
          }

          // 2. Butonlara border-radius ver
          const buttons = document.querySelectorAll<HTMLButtonElement>(
            ".cookieseal-banner-button"
          );
          buttons.forEach((btn) => {
            btn.style.borderRadius = "0.375rem";
          });

          // 3. Yazıdaki “Cookie Settings” ifadesini değiştir
          const bannerText = document.getElementById("cookieseal-banner-text");
          if (bannerText) {
            bannerText.innerHTML = bannerText.innerHTML
              .replace(/Cookie Settings/gi, "Customize Settings")
              .replace(
                /and analyze our traffic./gi,
                'and analyze our traffic as specified in our<a href="/cookie-policy" target="_blank" rel="noopener noreferrer" style="text-decoration: underline; color: inherit;">Cookie Policy.</a>'
              )
              .replace(/ You can/gi, "You can")
              .replace(/orYou can/gi, "or you can");
          }
        }
      }, 100);
    };

      document.head.appendChild(script);

      return () => {
          document.head.removeChild(style);
          document.head.removeChild(script);
      };
  }, []);

  return null;
}
