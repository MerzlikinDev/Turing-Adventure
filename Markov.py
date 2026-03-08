import time
def markovs_machine():
    word = input()
    rules = {}
    x = input().split()
    while x != ["end"]:
        rules[x[0]] = [x[1], x[2]]
        x = input().split()
    for key in rules:
        d = rules[key][0]
        if d in list(rules.keys()):
            if (rules[d][0] == key) and (rules[d][1] == rules[key][1]):
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
            if rules[i][1] == "->":
                while i in word:
                    word = word.replace(i, rules[i][0])
                    time_dis = time.time() - time1
                    if time_dis > 7.5:
                        print('цикл')
                        return word
            elif rules[i][1] == "=>":
                while i in word:
                    word = word.replace(i, rules[i][0])
                return word
    return word
print(markovs_machine())
