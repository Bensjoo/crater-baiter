from flask import Flask, request, render_template

app = Flask(__name__)

classes = [
    "Warrior",
    "Paladin",
    "Hunter",
    "Rogue",
    "Priest",
    "Death Knight",
    "Shaman",
    "Mage",
    "Warlock",
    "Druid",
    "Demon Hunter",
    "Evoker"
]
classes.sort()
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