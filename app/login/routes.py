from flask import Flask, render_template, request, url_for, flash, redirect
from app.login import bp

@bp.route('/', methods=('GET', 'POST'))
def login():
    return render_template('login/login.html')

@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    return render_template('login/signup.html')