#v.0.0.6
            #Turing macchine by mishanya with Russian localisation
print('введите правила для a, b и с')
a = input()
b = input()
c = input()
rules = {'a': a.split(), 'b': b.split(), 'c': c.split(), '-': ('!')}
print('Сейчас, сравните таблицу ниже с вашеми правилами, если они отличаются перезапустите программу и введите данные заново.')
print(f'a: {rules['a']}; b: {rules['b']}; c: {rules['c']}')
print('введите слово, которое, вы хотите поместитьна ленту тьюринга:')
word = input()

def process(w):
    w = [i for i in w]

    condition = 'q0'
    i = 0
    for_every_step = {}
    while True:
        if i < 0:
            return w[:-1]
        if i > len(word) - 1:
            return w[:-1]

        if w[i] == 'a':
            w[i] = rules['a'][0]

            condition = rules['a'][2]

        elif w[i] == 'b':
             w[i] = rules['b'][0]

             condition = rules['b'][2]

        elif w[i] == 'c':
             w[i] = rules['c'][0]

             condition = rules['c'][2]
        if w[i] in 'abc':
            if rules[w[i]][1] == 'R':
                i += 1
            else:
                i -= 1


        else:
            return 'не цикл'
        if str(w) not in for_every_step.keys():
            for_every_step[str(w)] = i
        elif str(w) in for_every_step.keys() and for_every_step[str(w)] == i:
            return 'цикл'



print(process(word))
