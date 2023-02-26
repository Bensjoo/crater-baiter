from dataclasses import dataclass

from flask_login import UserMixin


from baiter import db, login_manager


@dataclass
class WOWClass:
    pretty_name: str
    css: str


classes: list[WOWClass] = [
    WOWClass("Warrior", "warrior"),
    WOWClass("Paladin", "paladin"),
    WOWClass("Hunter", "hunter"),
    WOWClass("Rogue", "rogue"),
    WOWClass("Priest", "preist"),
    WOWClass("Death Knight", "deathknight"),
    WOWClass("Shaman", "shaman"),
    WOWClass("Mage", "mage"),
    WOWClass("Warlock", "warlock"),
    WOWClass("Druid", "druid"),
    WOWClass("Demon Hunter", "demonhunter"),
    WOWClass("Evoker", "evoker")
]


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


