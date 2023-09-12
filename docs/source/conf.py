# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

project = "Demo Project"
copyright = (
    "2023, Friedrich Miescher Institute for Biomedical Research - Tim-Oliver Buchholz"
)
author = "Tim-Oliver Buchholz"
release = "0.1"

sys.path.insert(0, os.path.abspath("../../"))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    "sphinx_inline_tabs",
    "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = []

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 5


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_static_path = ["_static"]
html_title = "Demo Project"
html_logo = "resources/logoipsum-258.svg"
html_theme_options = {
    "light_css_variables": {
        "font-stack": "Source Sans Pro, sans-serif",
        "font-stack--monospace": "Courier, monospace",
    },
}
