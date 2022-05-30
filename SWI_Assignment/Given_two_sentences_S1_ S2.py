
S1 = "the first column F will contain only 5 uniques values"
S2 = "the second column S will contain only 3 uniques values"


def string_features(Sentence1, Sentence2):
    Sentence1 = Sentence1.lower()
    Sentence2 = Sentence2.lower()
    S1List = Sentence1.split(" ")
    S2List = Sentence2.split(" ")
    b, c = [], []
    # print((set(S1List) & set(S2List)))
    a = len(list(set(S1List) & set(S2List)))

    for i in S1List:
        if i not in S2List:
            b.append(i)

    for i in S2List:
        if i not in S1List:
            c.append(i)

    return a, b, c


a, b, c = string_features(S1, S2)
print(f'{a} \n{b} \n{c}')
