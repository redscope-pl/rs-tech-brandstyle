# GitBook: base customization

Hosted GitBook takes a brand through its site settings (Customization), not
through CSS. Enter the values below; upload the files from `brand/`.
rs-tech-brandstyle @@RS_VERSION@@.

Status: not yet entered on a GitBook site. The setting names follow GitBook's
Customization page as of 2026; if one is named differently there, match it by
meaning.

## Values

| Setting                  | Value                                                    |
| ------------------------ | -------------------------------------------------------- |
| Primary colour           | `@@RS_COLOR:light.accent@@` (red, the logo's)            |
| Primary colour, dark mode (if offered) | `@@RS_COLOR:dark.accent@@`               |
| Tint colour (if offered) | `@@RS_COLOR:dark.bg@@` (dark night)                      |
| Default theme            | follow the reader's system (light and dark both)         |
| Font                     | a monospace one if the list has it, else the default     |
| Corner style             | rounded                                                  |

## Files

| Setting           | File                                        |
| ----------------- | ------------------------------------------- |
| Logo, light mode  | `brand/images/logo/logo-light.svg`          |
| Logo, dark mode   | `brand/images/logo/logo-dark.svg`           |
| Icon / favicon    | `brand/icons/icon-512.png`                  |
| Social preview    | `brand/icons/icon-512.png`                  |

If an SVG is refused, take the PNG of the same name from `brand/icons/`
(`mark-512.png` for the eye alone).

The files are all rights reserved (`brand/NOTICE.md`); fine on our own
GitBook spaces.
