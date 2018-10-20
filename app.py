#Flask APP

# Imports
import requests
from flask import Flask, render_template
from models.recipe import Recipe

app = Flask(__name__, template_folder='templates')

#########################
# File for hosting site #
#########################


#COMMANDS

@app.route("/")
def hello():
    return render_template('home.html'), "html home page"

@app.route("/findrecipe/<food>", methods=["GET", "POST"])
def find_recipe(food):
	recipe = Recipe()
	json = recipe.get_recipe(food)
	print(json)
	return render_template('index.html')

if __name__ == '__main__':
    app.run()