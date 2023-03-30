# Jinja is a templating language for Python and is bundled with Flask so no need to install Jinja separately.
import datetime
import random
import requests
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home(name=None):
    random_number = random.randint(1,10)
    copyright_year = datetime.date.today().year
    return render_template('index.html', ran=random_number,copy_year = copyright_year)

@app.route('/guess/<name>')
def guess_age(name):
    requesting = requests.get(url=f'https://api.agify.io?name={name}')
    gender_request = requests.get(url=f'https://api.genderize.io?name={name}')
    agify_response=requesting.json()
    gender_response = gender_request.json()
    return render_template('guess.html',name=name, gender=gender_response['gender'],age = agify_response['age'])

@app.route('/blog')
def blog():
    blog_url='https://api.npoint.io/1fdb956d180291f3f459'
    blog_get = requests.get(url=blog_url)
    the_blog=blog_get.json()
    # print(the_blog)

    return render_template('blog.html',all_posts= the_blog)


if __name__ == "__main__":
    app.run(debug=True)
