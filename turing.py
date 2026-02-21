#v.0.0.5
            #Turing macchine by mishanya
print('Now, please, write your rules for our alphabet from 3 letters: a, b and c. In format: b R q0. IN THREE LINES:')
a = input()
b = input()
c = input()
rules = {'a': a.split(), 'b': b.split(), 'c': c.split(), '-': ('!')}
print('Okay, now compare this table with your rules, if something not right, re-run program.')
print(f'a: {rules['a']}; b: {rules['b']}; c: {rules['c']}')
print('Now, if all before correct type the word:')
word = input()

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
            break
    return f'Okay, Result is: {w[:-1]}'
print(process(word))
