def sum_eo(n, t):
    sum_no = 0
    if t == 'e':
        for i in range(0, n):
            if i % 2 == 0:
                sum_no += i
    elif t == 'o':
        for i in range(0, n):
            if i % 2 != 0:
                sum_no += i
    else:
        sum_no = -1
    return sum_no


no = int(input('Enter a number: '))
ti = input('Choose e or o: ')

x = sum_eo(no, ti)
print(x)
