def process(w):
    w = [i for i in w]

    condition = 'q0'
    i = 0
    while True:
        if i < 0:
            return w[:-1]
        if i > len(word) - 1:
            return w[:-1]
        if w[i] == 'a':
            w[i] = rules['a'][0]

            condition = rules['a'][2]
            if rules['a'][1] == 'R':
                i += 1
            else:
                i -= 1
        elif w[i] == 'b':
             w[i] = rules['b'][0]

             condition = rules['b'][2]
             if rules['b'][1] == 'R':
                 i += 1
             else:
                 i -= 1
        elif w[i] == 'c':
             w[i] = rules['c'][0]

             condition = rules['c'][2]
             if rules['c'][1] == 'R':
                 i += 1
             else:
                 i -= 1
        else:
            break
    return f'Okay, Result is: {w[:-1]}'
print(process(word))
