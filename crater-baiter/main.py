from flask import Flask, request, render_template
from dataclasses import dataclass
app = Flask(__name__)
VERSION = "v0.0.1-alpha"

## you can get app version globally in jinja by doing this
app.jinja_env.globals.update(app_version=VERSION)


@dataclass
class WOWClass:
    pretty_name:str
    css:str


classes:list[WOWClass] = [
    WOWClass("Warrior","warrior"),
    WOWClass("Paladin","paladin"),
    WOWClass("Hunter","hunter"),
    WOWClass("Rogue","rogue"),
    WOWClass("Priest","preist"),
    WOWClass("Death Knight","deathknight"),
    WOWClass("Shaman","shaman"),
    WOWClass("Mage","mage"),
    WOWClass("Warlock","warlock"),
    WOWClass("Druid","druid"),
    WOWClass("Demon Hunter","demonhunter"),
    WOWClass("Evoker","evoker")
]
@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        class_choice = request.form["class_choice"]
        location = request.form["location"]
        # Do something with the form data
        return "Class: {} Location: {}".format(class_choice, location)
    return render_template("register.html", classes=classes)

if __name__ == "__main__":
    app.run()