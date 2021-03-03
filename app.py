from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
	return "hello world"

if __name__ == "__main__":
	app.run(debug=True)