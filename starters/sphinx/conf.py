# Sphinx configuration in the RedScope style (rs-tech-brandstyle @@RS_VERSION@@).
# Theme: Furo; colours come from brand/css/tokens.css, never written here.

project = "RedScope Technologies"
author = "RedScope Technologies"
copyright = "RedScope Technologies"

extensions = []
exclude_patterns = ["_build"]

html_theme = "furo"
html_title = project
html_static_path = ["_static"]
html_css_files = ["brand/css/tokens.css"]
html_favicon = "_static/brand/icons/favicon.ico"


def _furo(scheme: str) -> dict:
    """Furo's variables, from the pack's fixed scheme variables."""
    return {
        "color-brand-primary": f"var(--rs-{scheme}-accent)",
        "color-brand-content": f"var(--rs-{scheme}-accent)",
        "color-brand-visited": f"var(--rs-{scheme}-highlight)",
        "color-foreground-primary": f"var(--rs-{scheme}-fg)",
        "color-foreground-secondary": f"var(--rs-{scheme}-muted)",
        "color-background-primary": f"var(--rs-{scheme}-bg)",
        "color-background-secondary": f"var(--rs-{scheme}-surface)",
        "color-background-border": f"var(--rs-{scheme}-line)",
        "color-highlighted-background": f"var(--rs-{scheme}-accent-soft)",
        "color-admonition-title--note": f"var(--rs-{scheme}-highlight)",
        "color-admonition-title-background--note": f"var(--rs-{scheme}-highlight-soft)",
        "color-admonition-title--tip": f"var(--rs-{scheme}-accent)",
        "color-admonition-title-background--tip": f"var(--rs-{scheme}-accent-soft)",
        "font-stack": "var(--rs-font-text)",
        "font-stack--monospace": "var(--rs-font-mono)",
        "font-stack--headings": "var(--rs-font-text)",
    }


html_theme_options = {
    "light_logo": "brand/images/logo/logo-light.svg",
    "dark_logo": "brand/images/logo/logo-dark.svg",
    "sidebar_hide_name": True,
    "light_css_variables": _furo("light"),
    "dark_css_variables": _furo("dark"),
}
