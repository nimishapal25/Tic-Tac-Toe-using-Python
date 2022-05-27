n = input('Enter a string: ')
count = 0

for char in n:
    if char.isdigit():
        count = count + 1
for _ in range(count):
    print('#', end="")


ans = ['#' if i.isdigit() else '' for i in n]
for i in n:
    if i.isdigit():
        ans.append('#')
    else:
        ans.append('')
print(ans)

a = True

# b = a ? 1: -1
b = 1 if a else -1
print(b)
