import time
def markovs_machine() -> str:
    word = input()
    rules = {}
    x = input().split(" ")
    while x != ["."]:
        rules[x[0]] = [x[1], x[2]]
        print(rules)
        x = input().split(" ")
    first_fd = True
    while first_fd:
        count = 0

        if list(rules.keys())[0] not in word:
            count += 1
            if count == len(list(rules.keys())):
                first_fd = False
                return word
        time1 = time.time()
        i = 0
        while i <= len(rules):
            if list(rules.keys())[0] == i:
                if rules[str(list(rules.keys())[i])][0] == "->":
                    while list(rules.keys())[i] in word:
                        word = word.replace(list(rules.keys())[i], rules[str(list(rules.keys())[i])][1])

                        time_dis = time.time() - time1
                        if time_dis > 7.5:
                            print('цикл')
                            return word
                elif rules[str(list(rules.keys())[i])][0] == "=>":
                     while list(rules.keys())[i] in word:
                        word = word.replace(list(rules.keys())[i], rules[str(list(rules.keys())[i])][1])
                        return word
                i += 1
            else:
                if rules[str(list(rules.keys())[i])][0] == "->":
                        if list(rules.keys())[i] in word:
                            word = word.replace(list(rules.keys())[i], rules[str(list(rules.keys())[i])][1], 1)
                elif rules[str(list(rules.keys())[i])][0] == "=>":
                        if list(rules.keys())[i] in word:
                            word = word.replace(list(rules.keys())[i], rules[str(list(rules.keys())[i])][1], 1)
                            return word
                i += 1
                if str(list(rules.keys())[0]) in word:
                    i = 0
                    continue
    return word
print(markovs_machine())
