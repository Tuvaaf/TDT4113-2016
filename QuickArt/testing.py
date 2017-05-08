from PIL import Image
from PIL import ImageEnhance

__author__ = "Martin Langmo Karlstrøm"
__project__ = "QuickArt"


path = '/home/martin/Documents/Studier/2. klasse/Høst/Plab2/Programmeringslab 2/TDT4113-2016/QuickArt/img/brain.jpeg'

im = Image.open(path)
enh = ImageEnhance.Contrast(im)
enh.enhance(0.1).show()
