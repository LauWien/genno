# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information ---------------------------------------------------------------

project = "genno"
copyright = "2018–2022, Genno contributors"
author = "Genno contributors"


# -- General configuration -------------------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be extensions coming
# with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "IPython.sphinxext.ipython_directive",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and directories to
# ignore when looking for source files. This pattern also affects html_static_path and
# html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -----------------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for a list of
# builtin themes.
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here, relative
# to this directory. They are copied after the builtin static files, so a file named
# "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]


# -- Options for sphinx.ext.extlinks ---------------------------------------------------

extlinks = {
    "issue": ("https://github.com/khaeru/genno/issues/%s", "#"),
    "pull": ("https://github.com/khaeru/genno/pull/%s", "PR #"),
    "gh-user": ("https://github.com/%s", "@"),
}

# -- Options for sphinx.ext.intersphinx ------------------------------------------------

intersphinx_mapping = {
    "dask": ("https://docs.dask.org/en/stable/", None),
    "ixmp": ("https://docs.messageix.org/projects/ixmp/en/latest", None),
    "joblib": ("https://joblib.readthedocs.io/en/latest/", None),
    "message_ix": ("https://docs.messageix.org/en/latest", None),
    "pandas": ("https://pandas.pydata.org/docs/", None),
    "pint": ("https://pint.readthedocs.io/en/stable/", None),
    "plotnine": ("https://plotnine.readthedocs.io/en/stable/", None),
    "pyam": ("https://pyam-iamc.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "xarray": ("https://xarray.pydata.org/en/stable/", None),
}

# -- Options for sphinx.ext.todo -------------------------------------------------------

todo_include_todos = True
