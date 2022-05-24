number = '9,223;372,026 874,775;987'
print(number[1::4])
result = ''
for value in number:
    if value in number[1::4]:
        result += ', '
    else:
        result += value
print(result.split(', '))
res = result.split(', ')

for index in range(len(res)):
    res[index] = int(res[index])
print(res)




































