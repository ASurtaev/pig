import numpy as np
from PIL import Image
from pprint import pprint
from pig import *
from Layers import *

if __name__ == '__main__':

	# создаем генератор
	gen = Generator()

	# задаем слои генератора
	gen.add('add', SimplexNoise, args={'x_size':50, 'y_size':50})
	gen.add('fit', BinFilter, args={'threshold':0.5})
	gen.add('fit', CellarAutomate, args={'loops':1, 'nbs_to_die':8})
	
	# генерируем изображение
	gen.createImage(500,500)