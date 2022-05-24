n = input('Enter a string: ')
count = 0

for char in n:
    if char.isdigit():
        count = count + 1
for i in range(count):
    print('#', end="")
