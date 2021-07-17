# -*- coding: utf-8 -*-
import numpy as np
from pig.Layer import Layer

class Generator():

	def __init__(self, x=1, y=1):
		self.shape = (x, y)
		self._layers = []
		self._result = np.zeros(self.shape)

	# при добавлении слоя методу передается 4 аргумента:
	# - mode - "режим" слоя. Сейчас есть два режима:
	# -- add - результат работы слоя прибавляется к текущему результату
	# -- mult - результат работы слоя умножается на текущий результат
	# -- fit - слой обрабатывает конкретный массив, который и передается на вход, coef при этом игнорируется
	# - coef - коэффициент, на который умножается результат работы слоя перед применением
	# - func - сама функция слоя, вида f(x, y, {дополнительные аргументы})
	# - args - словарь, дополнительных аргументов функции слоя
	def add_layer(self, mode, func, coef=1, **kwargs):
		new_layer = Layer(mode, func, coef, **kwargs)
		self._layers.append(new_layer)

	def show_layers_info(self):
		for layer in self._layers:
			print(layer)

	def remove_layer(self, index):
		self._layers.pop(index)

	def generate(self):
		for layer in self._layers:
			self._result = layer.call_function(self._result, self.shape)

	def get_result(self):
		return self._result

	def change_size(self, x, y):
		self._result = np.zeros((x, y))
