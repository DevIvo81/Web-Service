from flask import Blueprint, render_template

users = Blueprint('users', __name__)

@users.route('/users')
def user():
    return render_template('user.html')