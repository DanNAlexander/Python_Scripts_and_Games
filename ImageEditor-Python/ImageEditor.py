from PIL import Image, ImageEnhance, ImageFilter
import os

path = './images'
pathOut = '/editedImages'

for filename im os.listdir(path):
	img = Image.open(f"{path}/{filename}")
	
	edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)
	
	factor = 1.5
	enhancer = ImageEnhance.Contrast(edit)
	edit = enhancer.enhance(factor)
	
	clean_name = os.path.splitext(filename)[0]
	
	edit.save(f'.{pathOut}/{clean_name}_edited.jpg')