import time


def markovs_machine() -> str:
    word = input()
    rules = []

    x = input().split(" ")
    while x != ["."]:
        if len(x) >= 3:
            l = x[0]
            a = x[1]
            r = x[2]
            rules.append((l, a, r))
        x = input().split(" ")

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
