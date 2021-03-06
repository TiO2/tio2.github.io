from flask import render_template
from project.app import app, pages
 
 
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/cv/')
def cv():
    return render_template('cv.html')

@app.route('/publication/')
def publication():
    return render_template('publication.html')
    
@app.route('/links/')
def links():
    return render_template('links.html')
        
@app.route('/blog/')
def blog():
    posts = [page for page in pages if 'date' in page.meta]
    # Sort pages by date
    sorted_posts = sorted(posts, reverse=True,
        key=lambda page: page.meta['date'])
    return render_template('blog.html', pages=sorted_posts)
 
@app.route('/blog/<path:path>/')
def page(path):
    # `path` is the filename of a page, without the file extension
    # e.g. "first-post"
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)
