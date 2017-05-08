#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Tharyrok'
SITENAME = 'Tharyrok'
SITEURL = '/blog'
OUTPUT_PATH = 'output/blog/'
PAGE_URL = '../{slug}.html'
PAGE_SAVE_AS = '../{slug}.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [('Home', '/'), ('Blog', '/blog/')]

PATH = 'content'

TIMEZONE = 'Europe/Brussels'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': '../robots.txt'},
    }

STATIC_PATHS = [
    'pictures',
    'extra/robots.txt',
    'cards-articles'
    ]

THEME = './themes/tharyrok'
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
AUTHORS_SAVE_AS = False
AUTHOR_SAVE_AS = False
CATEGORIES_SAVE_AS = False