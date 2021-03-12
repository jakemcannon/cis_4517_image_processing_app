from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def home():
	return render_template('home.html')

@app.route("/content")
def get_images_from_s3():


	test_urls = [
		"https://i.scdn.co/image/f3b3ca20f243a0417b649fd6a955ced67ab0587b",
		"https://i.scdn.co/image/1f13382660213676af972512faf826f3543e776e",
		"https://i.scdn.co/image/7333fa3cf2e6a45bafe2db5e2cfcd6915f255b33",
		"https://i.scdn.co/image/64bba7062a23676cdb12d9282b1ffa374205d181",
		"https://i.scdn.co/image/3cb69d597c64e1b6f066233e3357627c434a4dc2",
		"https://i.scdn.co/image/3cb69d597c64e1b6f066233e3357627c434a4dc2",
		"https://i.scdn.co/image/3cb69d597c64e1b6f066233e3357627c434a4dc2",
		"https://i.scdn.co/image/3cb69d597c64e1b6f066233e3357627c434a4dc2",
		"https://image-processing-4517.s3.amazonaws.com/result_image_test.jpg",
		"https://i.scdn.co/image/3cb69d597c64e1b6f066233e3357627c434a4dc2",
		"https://i.scdn.co/image/3cb69d597c64e1b6f066233e3357627c434a4dc2",
		"https://i.scdn.co/image/3cb69d597c64e1b6f066233e3357627c434a4dc2",
		"https://i.scdn.co/image/3cb69d597c64e1b6f066233e3357627c434a4dc2",
	]

	# make request to s3 that gets list of all files in bucket
	# response = aws.get_bucket_all()

	# get the url for every file
	#photos = [response["url"] for ..]

	# inject that url into html img tag

	#photos=photo_urls
	print(test_urls)
	return render_template('content.html', photo_urls=test_urls)


if __name__ == "__main__":
	app.run(debug=True)
