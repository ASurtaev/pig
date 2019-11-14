import numpy as np

def AdditiveNoise(x, y, args={}):
	return np.random.random((x, y))

def GaussianNoise(x, y, args={'loc':0, 'scale':None}):
	args['size'] = (x,y)
	return np.random.normal(**args)