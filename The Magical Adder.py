
inp = input()
res = []

for value in inp.split(','):
    res.append(int(value))
print(res[0] + res[1] - res[2])

# print(int('-1'))
l = [None] * 10
print(len(l))

resList = [x+y for x in ['Hello ', 'Good '] for y in ['Dear', 'Bye']]
print(resList)
