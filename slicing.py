a = "Kaustubh"
print(a[0:])

# step in slicing
print(a[0:6:2])

number = '9,223;372,026 874,775;987'
result = [9, 223, 372, 26, 874, 775, 987]
separators = number[1::4]
print(separators)

values = ''.join(char if char not in separators else ' ' for char in number).split()
print(values)
print([int(val) for val in values])

letters = 'abcdefghijklmnopqrstuvwxyz'
sliceStr = letters[25::-1]
print(sliceStr)

print(letters[-10:-13:-1])   # qpo
print(letters[4::-1])        # edcba
print(letters[:17:-1])
print(letters[-1:-9:-1])

