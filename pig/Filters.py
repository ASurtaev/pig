# -*- coding: utf-8 -*-
import numpy as np

#########################################
# Функция, сводящая масстив к бинарному #
#########################################
# threshold - порог, выше которого элементы массива
# 				превращаются в 1., ниже - в 0.
def BinFilter(data, args={'threshold': 0}):
	if 'threshold' in args.keys():
		threshold = args['threshold']
	else:
		threshold = 0
	vect = np.vectorize(lambda x: 1. if x > threshold else 0.)
	return vect(data)