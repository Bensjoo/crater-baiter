from flask import (
    redirect,
    request,
    render_template,
    Blueprint,
    url_for
)


from flask_login import login_required, login_user, current_user, logout_user


from baiter import discord, db
from baiter.models import User, Victim
from baiter.auth import CALLBACK_ROUTE
from baiter.models import classes


main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
@main_bp.route('/home')
def home():
    """
    TODO: see overview of kill statistics/list of kills if logged in?
    """
    if current_user.is_authenticated:
        victims = Victim.query.order_by(Victim.added.desc())
        return render_template('victims.html', victims=victims, classes=classes)
    else:
        return render_template('home.html', oauth_url=discord.oauth_url)


@main_bp.route(CALLBACK_ROUTE)
def callback():
    code = request.args['code']
    token = discord.access_token(code)
    current_user = discord.get_current_user(token)

    user = User.query.filter_by(discord_id=current_user['id']).first()
    if not user:
        user = User(
            discord_id=current_user['id'],
            username=current_user['username']
        )
        db.session.add(user)
        db.session.commit()

    login_user(user)
    return redirect(url_for('main_bp.home'))


@main_bp.route('/logout')
@login_required
def logout():
    logout_user()
    # flash('You have been logged out.')
    return redirect(url_for('main_bp.home'))

# @main_bp.route("/crater", methods=["GET", "POST"])
# def add_victim():
#     if request.method == "POST":
#         class_choice = request.form["class_choice"]
#         location = request.form["location"]
#         # Do something with the form data
#         return "Class: {} Location: {}".format(class_choice, location)
#     return render_template("add_victim.html", classes=classes)
