# name = 'Kaustubh'
#
# for char in name[1:5]:
#     print(char)

number = '9,223;372,026 874,775;987'
result = ''
for char in number:
    if char in number[1::4]:
        result += ','
    else:
        result += char

print(result)

# for i in range(0, 10, 2):
#     print(i)

# for i in range(10, 0, -2):
#     print(i)
