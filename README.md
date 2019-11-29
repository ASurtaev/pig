# pig

Установка в режиме development (Linux): *git clone https://github.com/Perfectrum/pig && sudo python3 pig/setup.py build develop*


Пример использования:

    from pig import Generator, SimplexNoise, BinFilter, CellarAutomate

    # создаем генератор
    gen = Generator()

    # задаем слои генератора
    gen.add('add', SimplexNoise, args={'x_size':50, 'y_size':50})
    gen.add('fit', BinFilter, args={'threshold':0.5})
    gen.add('fit', CellarAutomate, args={'loops':1, 'nbs_to_die':8})
	
    # генерируем изображение
    gen.createImage(500,500)
