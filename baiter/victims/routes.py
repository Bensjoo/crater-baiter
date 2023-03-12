from datetime import datetime
from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from baiter import db
from baiter.models import Victim
from baiter.victims.forms import VictimForm


victims = Blueprint('victims', __name__)


@victims.route("/victims/new", methods=['GET', 'POST'])
@login_required
def new_victim():
    form = VictimForm()
    if form.validate_on_submit():
        victim = Victim(
            name=form.name.data,
            server=form.server.data,
            wow_class=form.wow_class.data,
            x_coord=form.x_coord.data,
            y_coord=form.y_coord.data,
            user_id=current_user.id,
            added=datetime.utcnow(),
        )
        db.session.add(victim)
        db.session.commit()
        # flash('Your victim has been created!', 'success')
        return redirect(url_for('main_bp.home'))
    return render_template('create_victim.html', title='New Victim', form=form)
