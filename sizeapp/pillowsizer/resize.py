from PIL import Image
import os


# filename = 'aperture.jpg'
# width = 100
# height = 100


def edit_and_save(filename, width=1000, height=1000):
	BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
	im = Image.open(os.path.join(BASE_DIR, 'media', 'uploads', filename))
	im_resized = im.resize((width, height))
	im_resized.save(os.path.join(BASE_DIR, 'media', 'uploads', filename))
	return None