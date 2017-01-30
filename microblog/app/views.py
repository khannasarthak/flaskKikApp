from flask import render_template, flash, redirect
# flash displays msgs based on form data, user login/failures etc
from .forms import LoginForm
from app import app


@app.route ('/') # home directory

@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        {
            'author': {'nickname': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'nickname': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template ('index.html',title='Home', user=user, posts = posts) # replaces {{}}
    # with the values provided here
    # use {% if %} {% else %} and {% endif %} in html
    # {% for post in posts %} {% endfor %}

@app.route('/login', methods = ['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit(): # does all form processing work,
    #ie check if data is compatible with form firleds
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form = form)
