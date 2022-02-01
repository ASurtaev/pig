# -*- coding: utf-8 -*-
from pig.Layer import Layer
from pig.BasicInteractions import continuation
from typing import List


class Generator:
	def __init__(self, data=None, automate=True):
		self._layers: List[Layer] = []
		self._interactions = []

		self.automate = automate
		self.last_layer = None
		if data:
			self._result = data
		else:
			self._result = [[0]]

	def add_data(self, data):
		self._result = data

	def add_layer(self, layer_func, data=None, interaction_func=continuation, **kwargs):
		new_layer = Layer(layer_func, **kwargs)
		if data:
			new_layer.set_data(data)
		else:
			new_layer.set_empty_data(len(self._result), len(self._result[0]))
		self._layers.append(new_layer)
		self._interactions.append(interaction_func)
		if self.automate:
			self.apply_layer()

	def apply_layer(self):
		if self._layers:
			# It is first layer or the func is continuation
			if self._interactions[-1] is None or self._interactions[-1] == continuation:
				self._layers[-1].set_data(self._result)
				if self._layers[-1].func:
					self._layers[-1].call_function()
				self._result = self._layers[-1].get_data()
			# all the other funcs have the same interface
			else:
				if self._layers[-1].func:
					self._layers[-1].call_function()
				self._result = self._interactions[-1](self._result, self._layers[-1].get_data())

	def show_layers_info(self):
		for layer in self._layers:
			print(layer)

	def remove_layer(self, index):
		self._layers.pop(index)

	def generate(self):
		for layer in self._layers:
			layer.call_function()

	def get_result(self):
		return self._result
