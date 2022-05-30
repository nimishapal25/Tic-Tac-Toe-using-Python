import re

# P(x1,y1)
# line Ax+By+C=0
# (Ax1+By2+C)/B>0

# Red= [(1,1),(2,1),(4,2),(2,4), (-1,4)]
# Blue= [(-2,-1),(-1,-2),(-3,-2),(-3,-1),(1,-3)]
# Lines=["1x+1y+0","1x-1y+0","1x+0y-3","0x+1y-0.5"]

Red = [(1, 1), (2, 1), (4, 2), (2, 4), (-1, 4)]
Blue = [(-2, -1), (-1, -2), (-3, -2), (-3, -1), (1, -3)]
Lines = ["1x+1y+0", "1x-1y+0", "1x+0y-3", "0x+1y-0.5"]

for i in Lines:
    result = re.split(r'[x|y]', i)
    lst_blue: list[float] = []
    lst = []
    try:
        for points in Red:
            print(f'{points[0]}, {points[1]}')
            print(f'{result[0]}, {result[1]}, {result[2]}')
            ans = (float(result[0]) * float(points[0]) + float(result[1]) * float(points[1]) +
                   float(result[2])) / float(result[1])
            lst.append(ans)
        print(f'red list: {lst}\n')
    except:
        print(f'red list: {lst}\n')

    try:
        for points in Blue:
            print(f'{points[0]}, {points[1]}')
            print(f'{result[0]}, {result[1]}, {result[2]}')
            ans_blue = (float(result[0]) * float(points[0]) + float(result[1]) * float(points[1]) +
                        float(result[2])) / float(result[1])
            lst_blue.append(ans_blue)
        print(f'blue list: {lst_blue}\n')
    except:
        print(f'blue list: {lst_blue}\n')
