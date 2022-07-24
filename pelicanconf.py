#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'openradarscience'
SITENAME = u'openradarscience.org'
HIDE_SITENAME = True
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'spacelab'
BOOTSTRAP_NAVBAR_INVERSE = False
BOOTSTRAP_FLUID = False

# Todo: add Banner
# BANNER = #'images/banner.jpeg'
# BANNER_ALL_PAGES = False

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#FEED_ALL_RSS = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['extra', 'images', 'templates']
EXTRA_PATH_METADATA = {
    #'extra/robots.txt': {'path': 'robots.txt'},
    # todo: add favicon
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/custom.css': {'path': 'static/custom.css'},
    'extra/CNAME': {'path': 'CNAME'},
}

# Blogroll
LINKS = [('ERAD2016', '/erad2016/'), ('ERAD2018', '/erad2018/'), ('ERAD2022', '/erad2022/'),]

# Social widget
SOCIAL = (('GitHub', 'http://github.com/openradar'),
          ('Gitter', 'https://gitter.im/openradar', 'comments'),
          )

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'authors', #'archives',
                    'search')

DEFAULT_PAGINATION = 5

# display items settings
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_ARCHIVE_ON_MENU = False

DISPLAY_ARTICLE_INFO_ON_INDEX = False

DISABLE_SIDEBAR_TITLE_ICONS = True
DISPLAY_ARCHIVE_ON_SIDEBAR = False
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_TAGS_ON_SIDEBAR = True

# breadcrumbs are disabled
DISPLAY_BREADCRUMBS = False
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

MARKDOWN = {
  'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
  },
  'output_format': 'html5',
}

TYPOGRIFY = True

CC_LICENSE = "CC-BY-NC-SA"

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
    #'liquid_tags.img', 'liquid_tags.video',
    #'liquid_tags.youtube', 'liquid_tags.vimeo',
    #'liquid_tags.include_code', 'tipue_search',
    #'tag_cloud',
    'i18n_subsites']

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# tag_cloud settings
DISPLAY_TAGS_INLINE = True
TAG_CLOUD_STEPS = 4
TAG_CLOUD_MAX_ITEMS = 100
TAG_CLOUD_SORTING = 'random'
TAG_CLOUD_BADGE = True

# Force Pelican to use the file name as the slug, instead of derivating it
# from the title.
FILENAME_METADATA = '(?P<slug>.*)'

ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'
ARTICLE_PATHS = ['posts']

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = PAGE_URL + 'index.html'
PAGE_PATHS = ['pages']

TAG_URL = 'tags/{slug}.html'
TAG_SAVE_AS = 'tags/{slug}.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = CATEGORY_URL + 'index.html'

INDEX_SAVE_AS = 'blog/' + 'index.html'

#YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

## Tags, categories and archives are Direct Templates, so they don't have a
## <NAME>_URL option.
TAGS_SAVE_AS = 'tags/index.html'
CATEGORIES_SAVE_AS = 'categories/index.html'
#ARCHIVES_SAVE_AS = 'archives/index.html'

SITELOGO = 'images/or_logo.png'
SITELOGO_SIZE = 26
MENUITEMS = (
    ('Home', '/'),
    ('Projects', '/projects/'),
    ('Community', '/community/'),
    ('News', '/category/news'),
    ('Virtual Machine', '/vm-docs/'),
    ('Open data', '/opendata/'),
)

