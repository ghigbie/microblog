from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

app_title = "Microblog"

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
                {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('home.html', app_title=app_title, title='Home', user=user, posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', app_title=app_title, title='About')

@app.route('/login', methods=['GET', 'POST']
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me= {form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', app_title=app_title, title='Sign In', form=form)