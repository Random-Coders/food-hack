#Flask APP
# Imports
from flask import Flask, render_template
from models import recipe

app = Flask(__name__, template_folder='templates')

#########################
# File for hosting site #
#########################


#COMMANDS

@app.route("/")
def hello():
    return render_template('home.html'), "html home page"

    # Marvin Webscrape Commands #
'''
@app.route("/rottentomatoes/<movie>")
def rottentomatoes(movie):
    Tomatoe_Scrape = TomatoeScrape(movie)
    movie_data = Tomatoe_Scrape.scrapeRottentomatoes()
    return jsonify(movie_data)

@app.route("/imdbrating/<movie>")
def imdbrating(movie):
    Tomatoe_Scrape = TomatoeScrape(movie)
    movie_data = Tomatoe_Scrape.IMDb()
    return jsonify(movie_data)

@app.route("/youtube/<query>")
def youtube(query):
    Youtube_Scrape = YoutubeScrape(query)
    youtube_link = Youtube_Scrape.scrapeYoutube() # function to scrape urls
    return jsonify(youtube_link)

@app.route("/definition/<query>")
def define(query):
    Definition_Find = DefinitionFind(query)
    definition_data = Definition_Find.scrapeDefinition() # function to scrape urls
    return jsonify(definition_data)
'''
if __name__ == '__main__':
    app.run()
