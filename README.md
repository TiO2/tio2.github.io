tio2.github.io
==============

This is a test of static Flask site by Frozen-Flask (for building static content) and Flask-FlatPages (for writing pages in Markdown).

测试下RST 
------------

这个格式是自动的在GITHUB 上render为HTML？

*这个？*


History:
03-25-2016
the csv as the format for post input
check the csv_to_md.py
However, pay attention, that the created md filename can not contian blanks or the github will not render the page at all. 
Delete the csv rows after the run? (temporary solution for the constant updates issue by making a copy of the original csv or append to a backup csv. see source code.) 



$ pip install -r requirements.txt
# Run local server
$ python run.py
# Build static content
$ python freeze.py

Reference: https://github.com/sloria/flask-ghpages-example







