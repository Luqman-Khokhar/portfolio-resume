import { defineConfig, type Plugin } from "vite";
import react from "@vitejs/plugin-react-swc";
import path from "path";
import { renderSitemap, renderSnapshot, structuredData } from "./src/seo/snapshot.ts";

// Puts the portfolio's content and JSON-LD into index.html at build (and in dev), and emits sitemap.xml.
const seo = (): Plugin => ({
  name: "portfolio-seo",
  transformIndexHtml(html) {
    const jsonLd = JSON.stringify(structuredData()).replace(/</g, "\\u003c");
    return html
      .replace("<!--seo:json-ld-->", `<script type="application/ld+json">${jsonLd}</script>`)
      .replace('<div id="root"></div>', `<div id="root">${renderSnapshot()}</div>`);
  },
  configureServer(server) {
    server.middlewares.use("/sitemap.xml", (_req, res) => {
      res.setHeader("Content-Type", "application/xml");
      res.end(renderSitemap(new Date().toISOString().slice(0, 10)));
    });
  },
  generateBundle() {
    this.emitFile({ type: "asset", fileName: "sitemap.xml", source: renderSitemap(new Date().toISOString().slice(0, 10)) });
  },
});

// https://vitejs.dev/config/
export default defineConfig(() => ({
  server: {
    host: "::",
    port: 8080,
  },
  plugins: [react(), seo()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
}));
