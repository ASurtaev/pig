def continuation(first_layer, second_layer):
    pass


def addition(first_layer, second_layer):
    res = []
    for line_f, line_s in zip(first_layer, second_layer):
        new_line = []
        for el_f, el_s in zip(line_f, line_s):
            new_line.append(el_f + el_s)
        res.append(new_line)
    return res


def multiplication(first_layer, second_layer):
    res = []
    for line_f, line_s in zip(first_layer, second_layer):
        new_line = []
        for el_f, el_s in zip(line_f, line_s):
            new_line.append(el_f * el_s)
        res.append(new_line)
    return res


def bit_and(first_layer, second_layer):
    res = []
    for line_f, line_s in zip(first_layer, second_layer):
        new_line = []
        for el_f, el_s in zip(line_f, line_s):
            new_line.append(el_f & el_s)
        res.append(new_line)
    return res


def bit_or(first_layer, second_layer):
    res = []
    for line_f, line_s in zip(first_layer, second_layer):
        new_line = []
        for el_f, el_s in zip(line_f, line_s):
            new_line.append(el_f | el_s)
        res.append(new_line)
    return res


def bit_xor(first_layer, second_layer):
    res = []
    for line_f, line_s in zip(first_layer, second_layer):
        new_line = []
        for el_f, el_s in zip(line_f, line_s):
            new_line.append(el_f ^ el_s)
        res.append(new_line)
    return res
