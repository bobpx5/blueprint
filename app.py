import os
from flask import Flask
from extensions import database, commands

app = Flask(__name__)
# setup with the configuration provided by the user / environment
app.config.from_object(os.environ['APP_SETTINGS'])

# setup all our dependencies
database.init_app(app)
commands.init_app(app)

@app.route("/")
def index():
    return "Hello World"

@app.route("/listOfClothes")
def list_of_clothes():
    return "List of clothes"

@app.route("/listOfShoes")
def list_of_shoes():
    return "List of shoes"

@app.route("/listOfTshirts")
def list_of_tshirts():
    return "List of t-shirts"

@app.route("/aboutMe")
def about_me():
    return "About me"

@app.route("/aboutMyWork")
def about_my_work():
    return "Abouy my work"

@app.route("/contactMe")
def contact_me():
    return "Contact Me"

@app.route("/contactForSponsor")
def contact_for_sponsor():
    return "Contact for Sponsor"

if __name__ == "__main__":
    app.run()
