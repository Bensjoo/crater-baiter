from flask_login import UserMixin


from baiter import db, login_manager


classes = {
    "warrior": {"color": "#C79C6E", "pretty_name": "Warrior"},
    "paladin": {"color": "#F58CBA", "pretty_name": "Paladin"},
    "hunter": {"color": "#ABD473", "pretty_name": "Hunter"},
    "rogue": {"color": "#FFF569", "pretty_name": "Rogue"},
    "priest": {"color": "#FFFFFF", "pretty_name": "Priest"},
    "deathknight": {"color": "#C41F3B", "pretty_name": "Death Knight"},
    "shaman": {"color": "#0070DE", "pretty_name": "Shaman"},
    "mage": {"color": "#69CCF0", "pretty_name": "Mage"},
    "warlock": {"color": "#9482C9", "pretty_name": "Warlock"},
    "druid": {"color": "#FF7D0A", "pretty_name": "Druid"},
    "demonhunter": {"color": "#A330C9", "pretty_name": "Demon Hunter"},
    "evoker": {"color": "#008149", "pretty_name": "Evoker"}
}
l_classes = list(classes.keys())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    """
    simple User model based on discord Oauth info
    """
    id = db.Column(db.Integer, primary_key=True)
    discord_id = db.Column(db.Integer, unique=True, nullable=False)
    username = db.Column(db.String, unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}')"


class Victim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    added = db.Column(
        db.TIMESTAMP,
        server_default=db.func.now(),
        nullable=False
    )

    name = db.Column(db.String(50), nullable=True)
    server = db.Column(db.String(50), nullable=True)
    wow_class = db.Column(
        db.Enum(
            *[c for c in l_classes],
            name="wow_class_enum"
            ),
        nullable=False
    )
    x_coord = db.Column(db.Float, nullable=True)
    y_coord = db.Column(db.Float, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Victim(id={self.id}, name={self.name}, cls={self.wow_class})"
