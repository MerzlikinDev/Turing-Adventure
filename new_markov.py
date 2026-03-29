import time


def markovs_machine() -> str:
    file_name = input()
    word = input()
    rules = []

    #x = input().split(" ")
    '''while x != ["."]:
        if len(x) >= 3:
            l = x[0]
            a = x[1]
            r = x[2]
            rules.append((l, a, r))
        x = input().split(" ")'''
    with open(file_name, mode="r", encoding="UTF-8") as file:
        a = file.readline().split()
        while a != []:
            if len(a) == 3:
                rules.append(tuple(a))
            elif len(a) == 2:
                b = ["", a[0], a[1]]
                rules.append(tuple(b))
            a = file.readline().split()

    start_time = time.time()
    while True:
        if time.time() - start_time > 7.5:
            print('превышенно время выполнения')
            return word


        pr = False
        for l, a, r in rules:
            if l in word:
                if a == "->":
                    word = word.replace(l, r, 1)
                    pr = True
                    break
                elif a == "=>":

                    word = word.replace(l, r, 1)
                    return word

        if not pr:
            return word



result = markovs_machine()
print(result)
