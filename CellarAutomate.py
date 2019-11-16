import numpy as np

######################################################
# Клеточный автомат для бинарного двумерного массива #
######################################################
# Аргументы:
# - loops - количество поколений
# - nbs_to_born - количество соседей, при котором рождается новая клетка
# - nbs_to_alive - количество соседей, при котором клетка выживает
# - nbs_to_die - количество соседей, при котором живая клетка умирает
# по умолчанию заданы правила классической игры "Жизнь"
def CellarAutomate(data, args={	'loops':1,
								'nbs_to_born':3,
								'nbs_to_alive':2,
								'nbs_to_die':4}):
		# ужасный, лютый, ублюдочный костыль, который нужен, чтобы функцию нормально мог исплользовать и генератор, и пользователь
		# по сути просто значения переменных по умолчанию
		if 'loops' not in args.keys():
			loops = 1
		else:
			loops = args['loops']
		if 'nbs_to_born' not in args.keys():
			nbs_to_born = 3
		else:
			nbs_to_born = args['nbs_to_born']
		if 'nbs_to_alive' not in args.keys():
			nbs_to_alive = 2
		else:
			nbs_to_alive = args['nbs_to_alive']
		if 'nbs_to_die' not in args.keys():
			nbs_to_die = 4
		else:
			nbs_to_die = args['nbs_to_die']
		if 'threshold' not in args.keys():
			threshold = 0
		else:
			threshold = args['threshold']

		# главный цикл
		for c in range(loops):
			# новый "кадр"
			new = np.zeros(data.shape)
			# обновление кадра
			for i in range(len(data)):
				for j in range(len(data[i])):
					# считаем количество живых соседей данной клетки
					nbs = 0
					if i>0 and data[i-1][j] > 0:
						nbs+= 1
					if i<len(data)-1 and data[i+1][j] > 0:
						nbs+= 1
					if j>0 and data[i][j-1] > 0:
						nbs+= 1
					if j<len(data[i])-1 and data[i][j+1] > 0:
						nbs+= 1
					if i>0 and j>0 and data[i-1][j-1] > 0:
						nbs+= 1
					if i>0 and j<len(data[i])-1 and data[i-1][j+1] > 0:
						nbs+= 1
					if i<len(data)-1 and j>0 and data[i+1][j-1] > 0:
						nbs+= 1
					if i<len(data)-1 and j<len(data[i])-1 and data[i+1][j+1] > 0:
						nbs+= 1
					# рассчитываем, выжила клетка, или нет
					if data[i][j] < threshold:
						if nbs >= nbs_to_born and nbs < nbs_to_die:
							new[i][j] = threshold + 1
					elif nbs >= nbs_to_alive and nbs < nbs_to_die:
							new[i][j] = threshold + 1
			data = new
		return data