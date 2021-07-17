# -*- coding: utf-8 -*-
import numpy as np
from opensimplex import OpenSimplex

# Обертка аддитивного шума из numpy #
def AdditiveNoise(x, y, args={}):
	return np.random.random((x, y))

# Обертка нормального шума из numpy #
def GaussianNoise(x, y, args={'loc':0, 'scale':None}):
	args['size'] = (x,y)
	return np.random.normal(**args)

# Симплексный шум из opensimplex #
#####################################
# В будущем хотелос бы конечно свою #
# реализацию написать, чтобы не     #
# таскать лишние зависимости        #
#####################################
# Аргументы:
# x_size и y_size - растяжение по осям
#	(позволяет добиться гладкости)
def SimplexNoise(x, y, args={'x_size':1, 'y_size':1}):
		
	if 'x_size' in args.keys():
		x_size = args['x_size']
	else:
		x_size = 1
	if 'y_size' in args.keys():
		y_size = args['y_size']
	else:
		y_size = 1
	
	simplex = OpenSimplex()
	data = np.array([[simplex.noise2d(i/x_size , j/y_size)/2+0.5 for i in range(y)] for j in range(x)])
	return data