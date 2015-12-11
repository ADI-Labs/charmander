from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True 		# delete later

@app.route("/")
def home():
	return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, page not found.", 404

if __name__ == "__main__":
    app.run(host="0.0.0.0")