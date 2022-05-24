even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
#
# print(min(even))
# print(max(odd))
#
# print()
#
# print(len(even))
#
# print()
#
# print('Mississippi'.count('s'))

even[4:] = [10, 12, 14, 16]
print(even)

# del even[1:3]
# print(even)

# id_to_del = 0
# for idx, i in enumerate(even):
#     if i <= 4:
#         id_to_del = idx
#
# print(id_to_del)
# del even[:id_to_del + 1]
# print(even)

# id_to_del = 0
# for index in range(len(even) - 1, -1, -1):
#     if even[index] >= 14:
#         id_to_del = index
#
# del even[id_to_del:]
# print(even)


id_to_del = len(even) - 1
for index, value in enumerate(reversed(even)):
    if value >= 14:
        del even[id_to_del - index]
print(even)

a = input('Please input three numbers')
inp = a.split(',')

res = int(inp[0]) + int(inp[1]) - int(inp[2])
print(res)

