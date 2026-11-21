(() => {
  "use strict";
  if (window.location.hostname !== "braindecode.org") return;
  const [, version, ...rest] = window.location.pathname.split("/");
  if (!version || version === "stable" || !/^[\w.-]+$/.test(version)) return;

  const hasThemeBanner = () => {
    if (window.DOCUMENTATION_OPTIONS && window.DOCUMENTATION_OPTIONS.show_version_warning_banner) {
      return true;
    }
    const el = document.getElementById("bd-header-version-warning");
    return Boolean(el && (!el.classList.contains("d-none") || el.textContent.trim() !== ""));
  };
  if (hasThemeBanner()) return;

  const stableBase = "https://braindecode.org/stable/";
  const candidate = rest.length ? `${stableBase}${rest.join("/")}` : stableBase;
  const label =
    version === "dev"
      ? "the <strong>unstable development version</strong>"
      : `an <strong>old version (${version})</strong>`;

  fetch(candidate, { method: "HEAD" })
    .then((res) => (res.ok ? candidate : stableBase))
    .catch(() => stableBase)
    .then((target) => {
      const html = `<div class="alert alert-danger devbar d-print-none" role="region" aria-label="Version warning" style="margin:0;padding:0.6rem 1rem;text-align:center;background:#f8d7da;color:#842029;border-bottom:1px solid #f5c2c7;">This is documentation for ${label} of Braindecode. <a class="btn btn-danger btn-sm" style="margin-left:0.6rem;padding:0.2rem 0.65rem;background:#dc3545;color:#fff;border-radius:0.25rem;text-decoration:none;font-weight:600;" href="${target}">Switch to stable version</a></div>`;
      const insert = () => {
        if (!hasThemeBanner() && !document.querySelector(".devbar")) {
          document.body.insertAdjacentHTML("afterbegin", html);
        }
      };
      if (document.body) insert();
      else document.addEventListener("DOMContentLoaded", insert, { once: true });
    });
})();
