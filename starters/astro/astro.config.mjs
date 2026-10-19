import { defineConfig } from "astro/config";

// SITE and BASE come from the Pages workflow (a project site lives under
// /<repository>/); locally the site is at the root.
export default defineConfig({
  site: process.env.SITE,
  base: process.env.BASE ?? "/",
});
