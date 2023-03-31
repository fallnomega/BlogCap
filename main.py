import requests
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    # print(num)
    blog_url = 'https://api.npoint.io/1fdb956d180291f3f459'
    blog_get = requests.get(url=blog_url)
    the_blog = blog_get.json()
    return render_template("index.html", all_posts=the_blog)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url='https://api.npoint.io/1fdb956d180291f3f459'
    blog_get = requests.get(url=blog_url)
    the_blog=blog_get.json()
    return render_template('blog.html', all_posts=the_blog,blog_id=int(num))

if __name__ == "__main__":
    app.run(debug=True)
