import config

from flask import Flask, render_template
from s3_operations import list_content


app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
	return render_template('home.html')

@app.route("/content")
def get_images_from_s3():

	# make request to s3 that gets list of all files in bucket
	response = list_content()

	# get the url for every file
	photos = []
	for item in response:
		photos.append(config.base_s3_url + item["Key"])

	# inject that url into html img tag
	return render_template('content.html', photo_urls=photos)


if __name__ == "__main__":
	app.run(debug=True)
