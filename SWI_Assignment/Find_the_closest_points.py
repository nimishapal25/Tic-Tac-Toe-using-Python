import math

S = [(1, 2), (3, 4), (-1, 1), (6, -7), (0, 6), (-5, -8), (-1, -1), (6, 0), (1, -1)]
P = (3, -4)


def cosine_similarity(v1, v2):
    cosine_distance_lst = []
    sumxp, sumyq, sumxy, sumpq = 0, 0, 0, 0
    for vector1 in v1:
        x, y, p, q = vector1[0], vector1[1], v2[0], v2[1]
        sumxp += x * p
        sumyq += y * q
        sumxy += x * x + y * y
        sumpq += p * p + q * q

        cosine_distance = 1 - ((sumxp + sumyq) / (math.sqrt(sumxy) * math.sqrt(sumpq)))
        cosine_distance_lst.append(cosine_distance)

    cosine_distance_dict = dict(zip(v1, cosine_distance_lst))
    return sorted(cosine_distance_dict.items(), key=lambda xc: xc[1])


def five_closest_points():
    cosine_lst = cosine_similarity(S, P)
    return [i[0] for idx, i in enumerate(cosine_lst) if idx < 5]


print(five_closest_points())
