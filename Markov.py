import time
def markovs_machine():
    word = input()
    rules = {}
    x = input().split()
    while x != ["end"]:
        rules[x[0]] = x[1]
        x = input().split()
    for keys in rules:
        d = rules[keys]
        if d in rules.keys():
            if rules[d] == keys:
                return "цикл"
    sm_fd = True
    while sm_fd:
        count = 0
        for i in list(rules.keys()):
            if i not in word:
                count += 1
                if count == len(list(rules.keys())):
                    sm_fd = False
                    return word
            else:
                break
        time1 = time.time()
        for i in list(rules.keys()):
            while i in word:
                word = word.replace(i, rules[i])
                time_dis = time.time() - time1
                if time_dis > 7.5: 
                    print('цикл')
                    return word
    return word
print(markovs_machine())
