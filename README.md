tio2.github.io
==============

This is the souce code for my personal site. 

The tech stack: static Flask site by Frozen-Flask (for building static content) and Flask-FlatPages (for writing pages in Markdown). The static pages can be deployed to Github for hosting. Added github actions.  

The github setup: config the branch "gh-pages". It will contain the final files for github page. 

Check out the <a href="http://tio2.github.io" target="_blank">site</a>.

## History:
03-25-2016
the csv as the format for post input
check the csv_to_md.py
However, pay attention, that the created md filename can not contian blanks or the github will not render the page at all. 
Delete the csv rows after the run? (temporary solution for the constant updates issue by making a copy of the original csv or append to a backup csv. see source code.) 

03-17-2020
update the files to Python3. Use absolute import for some of the python files. 

11-19-2020
added Github CI Actions: 




# instructions to run: 

    $ pip install -r requirements.txt

## Run local server for local development

    $ python run.py

## Build static content

    $ python freeze.py

## deploy to github:

Fork, modify, commit, push. 


Reference: 
1. https://github.com/sloria/flask-ghpages-example
2. https://github.com/peaceiris/actions-gh-pages
3. https://dev.to/peaceiris/deploy-to-github-pages-with-github-actions-for-static-site-generator-1mo6

