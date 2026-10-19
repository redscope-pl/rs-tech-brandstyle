import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

// Relative base: the built site works at any path (a GitHub Pages project
// site lives under /<repository>/).
export default defineConfig({
  base: "./",
  plugins: [react()],
});
