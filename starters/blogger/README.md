# Blogger theme

For `blog.redscope.online` (Blogger's own address
`redscopetech.blogspot.com`): articles and news in the nexus, the terminal
look of the author's "Technomantic Nexus" drafts (frame, status lines,
`[H] [S] [F] [Ω]` navigation, posts as fragments, an archive sidebar), made
of the pack's tokens and `nexus.css`; light and dark from the visitor's
scheme, the eye inline (nothing to host). Index pages show each post's
picture and a long snippet; a post's page shows it whole.

Install: Blogger → Theme → the arrow next to Customize → Backup (keep the
old one), then Edit HTML, replace everything with `theme.xml` of the built
pack, Save. The Blog widget brings its own markup; Header, Labels and
Blog Archive keep Blogger's default markup, styled by the theme.

Status: well-formed XML, no leftover placeholders; seen as a mock in
`docs/preview-nexus.html`. The first version was field-tested on the blog
(2026-10-19: "unoptimalized"); this one is not yet installed. Blogger can
refuse a theme on save: its message names the line. Comments are not shown
yet (the Blog widget's comment parts are Blogger's own includables).

Left out of the drafts on purpose: the Google Fonts link (the pack uses the
system's fonts) and three.js from a CDN (nothing from outside; BRAINSTORM).

The favicon is Blogger's own setting (Layout → Favicon): upload
`favicon-32.png` or `icon-192.png` of the pack.
