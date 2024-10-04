from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Home Page', heading='Welcome!', content='This is the home page content.')

@app.route('/about')
def about():
    return render_template('index.html', title='About Page', heading='About Us', content='This page provides information about us.')

@app.route('/contact')
def contact():
    return render_template('index.html', title='Contact Page', heading='Contact Us', content='This is how you can reach us.')

if __name__ == '__main__':
    app.run(debug=True)