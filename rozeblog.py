from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Els',
        'title': 'Blog Post 1',
        'content': 'Eerste blog',
        'date_posted': 'February 14, 2020'
    },
    {
        'author': 'Jane',
        'title': 'Blog Post 2',
        'content': 'Tweede blog',
        'date_posted': 'February 15, 2020'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)