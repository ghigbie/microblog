from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app import app
from app.forms import LoginForm
from app.models import User

app_title = "Microblog"

@app.route('/')
@app.route('/index')
@login_required
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', app_title=app_title, title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('logout'))

@app.route('/register')
def register():
    title = 'Registration'
    return render_template('register.html', app_title=app_title, title=title)
