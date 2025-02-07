from flask import Flask, render_template # type: ignore

app = Flask(__name__)

'''
# Routing for your application.
# Put your routes below this comment
'''
@app.route('/')
def home():
    return 'My Home page'

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
