import config
from s3_operations import list_content, upload

import os
from flask import Flask, request, render_template, redirect
from PIL import Image, ImageOps,ImageFilter
import uuid



app = Flask(__name__)

@app.route("/home", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home():

	if request.method == "POST":

		image_transformation = request.form.get("transformation")

		if request.files:

			# after receiving image, error check it

			img = request.files["image"]
			# save to a temp diretory
			img.filename = str(uuid.uuid4()) + ".jpg"
			img.save(os.path.join(config.temp_storage, img.filename))

		# transform image
		new_image = image_transform(img.filename, image_transformation)

		# upload to s3
		upload(os.path.join(config.temp_storage, new_image), new_image)

		# erase temp images, reset form

		# redirect to content page
		return redirect("content")

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


def image_transform(image_name, transformation):


	
	image = Image.open(os.path.join(config.temp_storage, image_name))

	if transformation == 'grayscale':
		result = ImageOps.grayscale(image)
	elif transformation == 'poster':
		result = ImageOps.posterize(image, 3)
	elif transformation == 'solar':
		result = ImageOps.solarize(image, threshold=80)

	new_image = "result_" + image_name

	result.save(os.path.join(config.temp_storage, new_image))
	return new_image


if __name__ == "__main__":
	app.run(debug=True)
