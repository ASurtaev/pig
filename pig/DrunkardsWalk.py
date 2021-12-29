import random


class ArrayPosition:
	def __init__(self, x, y):
		self.x = x
		self.y = y


def get_possible_directions(position, length, width, prev_dir):
	directions = ['u', 'd', 'r', 'l']
	if position.x == 0:
		directions.remove('l')
	if position.x == length - 1:
		directions.remove('r')
	if position.y == 0:
		directions.remove('u')
	if position.y == width - 1:
		directions.remove('d')

	if len(directions) > 1 and prev_dir:
		try:
			if prev_dir == 'u':
				directions.remove('d')
			elif prev_dir == 'd':				directions.remove('u')
			elif prev_dir == 'r':
				directions.remove('l')
			else:
				directions.remove('r')
		except:
			pass

	return directions


def drunkards_walk(data, steps=50, big_rooms=True, start=(0, 0)):
	#length, width = shape[0], shape[1]

	#data = [[0 for _ in range(length)] for _ in range(width)]
	length = len(data)
	width = len(data[0])
	data[start[0]][start[1]] = 255

	position = ArrayPosition(start[0], start[1])
	prev_dir = None

	for _ in range(steps):
		possible_directions = get_possible_directions(position, length, width, prev_dir)
		direction = random.choice(possible_directions)
		prev_dir = direction
		if direction == 'u':
			position.y -= 1
		elif direction == 'd':
			position.y += 1
		elif direction == 'l':
			position.x -= 1
		elif direction == 'r':
			position.x += 1

		data[position.x][position.y] = 255

	return data


