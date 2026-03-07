import time
def markovs_machine():
    alph = input().split()
    word = input()
    rules = {}
    for i in range(len(alph)):
        x = input().split()
        rules[alph[i]] = x[0]
    all_fd = True
    while all_fd:
        for i in alph:
            if i not in word:
                all_fd = False
        for i in range(len(rules)):
            time1 = time.time()
            while alph[i] in word:
                word = word.replace(alph[i], rules[alph[i]])
                time_dis = time.time() - time1
                if time_dis > 7.5: # спорно конечно, например если большая строка то это все же может быть не цикл
                    print('цикл')
                    return word
    return word
print(markovs_machine())
