from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index.html")
def index():
    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/articles.html')
def articles():
    return render_template('articles.html')

@app.route('/article1.html')
def article1():
    return render_template('article1.html')

@app.route('/article2.html')
def article2():
    return render_template('article2.html')

@app.route('/article3.html')
def article3():
    return render_template('article3.html')

if __name__ == '__main__':
    app.run(debug=True)