import re
S = "_,_,30,_,_,_,50,_,_"

finalList = []
lst = []


def curve_smoothing(string):
    result = re.split(r',', string)
    print(result)
    count = 0
    while len(result):
        for i in result:
            if i.isdigit():
                break
            count += 1
        ans = int(result[2])/(count + 1)
        for i in range(count + 1):
            finalList.append(ans)
        lst.append(finalList)
    return lst


print(curve_smoothing(S))
# smoothed_values= curve_smoothing(S)
# print(# print above values)
