# pig

Установка в режиме development (Linux): *git clone https://github.com/Asurtaev/pig && sudo python3 pig/setup.py build develop*


Пример использования:

    from pig.Generator import Generator
    from pig.Functions.DrunkardsWalk import drunkards_walk
    from pig.BasicInteractions import bit_or
    
    from PIL import Image
    from numpy import asarray
    
    def test():
        data = [[0 for _ in range(1000)] for _ in range(1000)]
        gen = Generator(data=data)
        gen.add_layer(drunkards_walk, steps=100000, start=(100, 100))
        gen.add_layer(drunkards_walk, interaction_func=bit_or, steps=100000, start=(100, 100))

        data_2 = [[0 for _ in range(1000)] for _ in range(1000)]
        gen_2 = Generator(data=data_2)
        gen_2.add_layer(drunkards_walk, steps=100000, start=(900, 900))
        gen.add_layer(drunkards_walk, interaction_func=bit_or, steps=100000, start=(900, 900))
    
        gen.add_layer(None, data=gen_2.get_result(), interaction_func=bit_or)

        img = asarray(gen.get_result())
        img = Image.fromarray(img)
        img.show()
    
    if __name__ == '__main__':
        test()

