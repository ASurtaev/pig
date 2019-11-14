# -*- coding: utf-8 -*-
import numpy as np
from PIL import Image

class Generator():
	layers = []
	
	#######################################
	# метод для добавления слоя генератора#
	#######################################
	# при добавлении слоя методу передается 4 аргумента:
	# - mode - "режим" слоя. Сейчас есть два режима:
	# -- add - результат работы слоя прибавляется к текущему результату
	# -- multiply - результат работы слоя умножается на текущий результат
	# - coef - коэффициент, на который умножается результат работы слоя перед применением
	# - func - сама функция слоя, вида f(x, y, {дополнительные аргументы})
	# - args - словарь, дополнительных аргументов функции слоя
	def add(self, mode, func, args={}, coef=1):
		self.layers.append({'mode': mode,
							'coef': coef,
							'func': func,
							'args': args})

	###########################################################	
	# метод, генерирующий результат в виде numpy массива (x,y)#
	###########################################################
	def generate(self, x, y):

		# создаем массив требуемого размера, состоящий из нулей
		data = np.zeros((x,y))

		# последовательно применяем слои из массива layers в соответствии с "режимом"
		for layer in self.layers:
			if layer['mode'] == 'add':
				data+= layer['coef']*layer['func'](x, y, layer['args'])
			elif layer['mode'] == 'multiply':
				data*= layer['coef']*layer['func'](x, y, layer['args'])
		#возвращаем результат
		return data

	################################################
	# метод, преобразующий результат в изображение #
	################################################
	# (x,y) - размеры изображения (х,у)
	# mode - для настройки Image.fromarray
	# - 1 (1-bit pixels, black and white, stored with one pixel per byte)
	# - L (8-bit pixels, black and white)
	# - P (8-bit pixels, mapped to any other mode using a color palette)
	# - RGB (3x8-bit pixels, true color)
	# - RGBA (4x8-bit pixels, true color with transparency mask)
	# - CMYK (4x8-bit pixels, color separation)
	# - YCbCr (3x8-bit pixels, color video format)
	# - LAB (3x8-bit pixels, the L*a*b color space)
	# - HSV (3x8-bit pixels, Hue, Saturation, Value color space)
	# - I (32-bit signed integer pixels)
	# - F (32-bit floating point pixels)
	# save - пусть для сохранения или None, если сохранять не нужно
	# show - True, если нужно вывести изображение на экран, иначе False
	def createImage(self, x, y, mode='L', save=None, show=True):
		# генерируем результат в виде массива
		data = self.generate(x, y)

		# превращаем масссив в изображение
		image = Image.fromarray(data, mode=mode)

		# выводим изображение на экран
		if show:
			image.show()

		# сохраняем изображение, если указан путь save
		if save:
			image.save(save)

		return