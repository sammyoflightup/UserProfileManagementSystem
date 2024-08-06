from flask import Blueprint, render_template, redirect, url_for, request
from models import db, User

main = Blueprint('main', __name__)

@main.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first()
    return render_template('profile.html', user=user)
