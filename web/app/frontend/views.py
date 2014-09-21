from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app import db
from app.user.forms import RegisterForm, LoginForm
from app.user.models import User
from app.user.decorators import requires_login

mod = Blueprint('frontend', __name__)

@mod.route('/')
def index():
    return render_template('index.html', user=g.user)

@mod.before_request
def before_request():
    '''
    pull user's profile from the database before every request are treated
    '''
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])
