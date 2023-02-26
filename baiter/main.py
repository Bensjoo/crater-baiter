from flask import redirect, request, render_template, session, Blueprint, url_for

# from flask_login import login_user

from baiter import discord, db
from baiter.auth import CALLBACK_ROUTE
# from models import classes


main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
@main_bp.route('/home')
def home():
    """
    provide link to login or 'add new victim' button
    TODO: see overview of kill statistics/list of kills if logged in?
    """
    # token = session.get('access_token')

    # if not token:
    return render_template('home.html', oauth_url=discord.oauth_url)

    # current_user = discord.get_current_user(token)
    # if 'token' in session:
    #     current_user = discord.get_current_user(session['token'])
    #     return render_template('home.html', current_user=current_user)
    # return render_template(
    #     'home.html',
    #     oauth_url=discord.oauth_url
    # )


@main_bp.route(CALLBACK_ROUTE)
def callback():
    code = request.args['code']
    session['token'] = discord.access_token(code)
    current_user = discord.get_current_user(session['token'])

    # check if user already in db of users
    #if 
    #login_user(current_user)
    return f"""current_user = {current_user} \n\n type(current_user) = {type(current_user)}"""


# @login_required
# @main_bp.route("/crater", methods=["GET", "POST"])
# def add_victim():
#     if request.method == "POST":
#         class_choice = request.form["class_choice"]
#         location = request.form["location"]
#         # Do something with the form data
#         return "Class: {} Location: {}".format(class_choice, location)
#     return render_template("add_victim.html", classes=classes)
