from PIL import Image, ImageOps,ImageFilter


image_path = "test_image.jpg"

def image_transform(image_path, transformation):
	
	image = Image.open(image_path)

	if transformation == 'grayscale':
		result = ImageOps.grayscale(image)
	elif transformation == 'poster':
		result = ImageOps.posterize(image, 3)
	elif transformation == 'solar':
		result = ImageOps.solarize(image, threshold=80)

	result.save("result_image_test.jpg")

image_transform(image_path, 'solar')


