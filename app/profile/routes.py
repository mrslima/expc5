from flask import render_template
from app.profile import bp

@bp.route('/')
def profile():
    return render_template('profile/profile.html')

@bp.route('/dashboard/')
def dashboard():
    return render_template('profile/dashboard.html')