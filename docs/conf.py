# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_material

# -- Project information -----------------------------------------------------

project = '上海交大超算平台用户手册'
copyright = '2020, 上海交通大学网络信息中心'
author = '上海交通大学网络信息中心计算业务部'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx-prompt',
    'sphinx_copybutton',
    'sphinx_substitution_extensions',
    'sphinx.ext.autosectionlabel'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'zh_CN'
html_search_language = 'zh'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- HTML theme settings -----------------------------------------------

html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

extensions.append("sphinx_material")
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_theme = "sphinx_material"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_material'


# Material theme options (see theme.conf for more information)
html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': '超算平台用户手册',

    # Set you GA account ID to enable tracking
    'google_analytics_account': 'UA-XXXXX',

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://project.github.io/project',

    # Set the color and the accent color
    'color_primary': 'blue',
    'color_accent': 'light-blue',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/SJTU-HPC/docs.hpc.sjtu.edu.cn',
    'repo_name': 'SJTU HPC Docs',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 3,
    # If False, expand all TOC entries
    'globaltoc_collapse': True,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,
}

# Add doc prefix for atutlabeling
autosectionlabel_prefix_document = True

# Image Match Order for HTML Builder
from sphinx.builders.html import StandaloneHTMLBuilder
StandaloneHTMLBuilder.supported_image_types = [
    'image/svg+xml',
    'image/gif',
    'image/png',
    'image/jpeg',
    'image/jpg'
]

# Image Match Order for HTML Builder
from sphinx.builders.latex import LaTeXBuilder
LaTeXBuilder.supported_image_types = [
    'image/pdf',
    'image/png',
    'image/jpeg',
    'image/jpg'
]

# Image Placeholder
rst_prolog = """
.. |cpu| image:: /img/cpu-icon.png
.. |gpu| image:: /img/gpu-icon.png
.. |arm| image:: /img/arm-icon.png
.. |sig| image:: /img/singularity-icon.png
.. |studio| image:: /img/studio-icon.png
"""

# LaTeX PDF customization
latex_engine = 'xelatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '12pt',

    'fncychap' : '\\usepackage[Bjornstrup]{fncychap}',

    # Additional stuff for the LaTeX preamble.
    # Reference: http://sychen.logdown.com/posts/2015/03/05/sphinx-pdf-chinese-support
    'preamble': r"""
    \usepackage{xeCJK}
    \usepackage{fontspec}
    \usepackage{indentfirst} % 中文首行缩进
	\let\cleardoublepage\clearpage
    \setlength{\parindent}{2em}
    \setCJKmainfont{Adobe Song Std}
    \setCJKmonofont[Scale=0.9]{Adobe Heiti Std}
    \setCJKfamilyfont{song}{Adobe Song Std}
    \setCJKfamilyfont{sf}{Adobe Song Std}
    \XeTeXlinebreaklocale "zh"          % 設定斷行演算法為中文
    \XeTeXlinebreakskip = 0pt plus 1pt  % 設定中文字距與英文字距
    """,

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}
