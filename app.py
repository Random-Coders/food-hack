#Flask APP

from flask import Flask, render_template, send_from_directory, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
	return render_template("index.html")

@app.route("/findrecipe/<food>", methods=["GET", "POST"])
def generate(food):
	print(food)
	return render_template('index.html')
if __name__ == "__main__":
	app.run()