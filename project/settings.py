# -*- coding: utf-8 -*-
 
import os

# http://stevenloria.com/hosting-static-flask-sites-for-free-on-github-pages/
 
REPO_NAME = "tio2" # Used for FREEZER_BASE_URL
DEBUG = True
 
# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))
 
def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))
 
PROJECT_ROOT = parent_dir(APP_DIR)
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = PROJECT_ROOT
# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
# FREEZER_BASE_URL = "http://localhost/{0}".format(REPO_NAME)

#L22: We also need to explicitly set FREEZER_BASE_URL since Github Pages hosts your repo pages on http://username.github.com/your-reponame. 
# uncomment line 22 if for other repo. This one is default one.

FREEZER_REMOVE_EXTRA_FILES = False # IMPORTANT: If this is True, all app files
# will be deleted when you run the freezer
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'
