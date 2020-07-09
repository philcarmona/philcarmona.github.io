#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
#import bulrush


PLUGINS = ['sitemap', 'post_stats', 'feed_summary','assets']
SITEURL = 'http://localhost:8000'
AUTHOR = 'Philippe Carmona'
SITENAME = 'Philippe Carmona'
SITETITLE = 'Philippe Carmona'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



SITELOGO = '/images/profile.png'
FAVICON = '/images/favicon.ico'

# Sitemap Settings
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}

# Add a link to your social media accounts
SOCIAL = (
    ('github', 'https://github.com/philcarmona'),
)

STATIC_PATHS = ['images', 'extra']


# Blogroll
LINKS = (         ('Master de Mathématiques', 'http://www.sciences-techniques.univ-nantes.fr/formations/masters/fiches-formations-master/master-math/master-mathematiques-et-applications-2021883.kjsp?RH=INSTITUTIONNEL_FR'),
         ('Département de Mathématiques', 'http://www.math.sciences.univ-nantes.fr/'),)


DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


THEME = 'themes/Flex'
PLUGIN_PATHS = ['./pelican-plugins']


PAGE_EXCLUDES=['home.html']

# Main Menu Items
# MAIN_MENU = True
# MENUITEMS = (('Enseignement/Teaching', '/enseignement'),('Publications', '/publications'),('Prépublications/Preprint', '/prepublications'))

# Code highlighting the theme
#PYGMENTS_STYLE = 'friendly'

# ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
# ARTICLE_SAVE_AS = ARTICLE_URL + 'index.html'

# PAGE_URL = '{slug}/'
# PAGE_SAVE_AS = PAGE_URL + 'index.html'

# ARCHIVES_SAVE_AS = 'archives.html'
# YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
# MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# # Feed generation is usually not desired when developing
# FEED_DOMAIN = SITEURL
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

# # HOME_HIDE_TAGS = True
# FEED_USE_SUMMARY = True
