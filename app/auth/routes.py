from flask import Flask, render_template, request, url_for, flash, redirect
from app.auth import bp

@bp.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('auth/login.html')

@bp.route('/signup', methods=('GET', 'POST'))
def signup():
    return render_template('auth/signup.html')

@bp.route('/logout')
def logout():
    return 'Logout'