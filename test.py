from pig import Generator, AdditiveNoise, GaussianNoise

if __name__ == '__main__':
	# создаем генератор
	gen = Generator()

	# первый слой - +белый шум
	gen.add('add', AdditiveNoise)
	# второй слой - *2*гауссовсикй шум
	gen.add('multiply', GaussianNoise, {'loc': 1}, coef=2)
	# третий слой - *белый шум
	gen.add('multiply', AdditiveNoise)

	# генератор может создавать изображения
	gen.createImage(500,500)