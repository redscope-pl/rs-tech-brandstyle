import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

// Relative base: the built site works at any path (a GitHub Pages project
// site lives under /<repository>/).
export default defineConfig({
  base: "./",
  plugins: [vue()],
});
