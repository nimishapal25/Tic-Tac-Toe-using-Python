s1 = input('S1: ').split()
s2 = input('S2: ').split()

common_words = list(set(s1) & set(s2))
s1_dominant = list(set(s1) - set(s2))
s2_dominant = list(set(s2) - set(s1))

print(f'\nCommon words: {common_words} ({len(common_words)})\nS1: {s1_dominant}\nS2: {s2_dominant}')
