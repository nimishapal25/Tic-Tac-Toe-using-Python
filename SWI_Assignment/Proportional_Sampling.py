import random

# no_of_ele = int(input('Enter number of elements in list: '))
# lst = []
#
# while no_of_ele:
#     ele = int(input('Enter list elements: '))
#     lst.append(ele)
#     no_of_ele -= 1
# print(lst)
lst = [0, 5, 27, 6, 13, 28, 100, 45, 10, 79]


def pick_a_number_from_list(l1):
    # num1 = 0
    # num = int(input('Pick a number from above list: '))
    # for i in lst:
    #     if num != i:
    #         continue
    #     elif num == i:
    #         num1 = num
    #         break
    # return num1
    num = int(input('Pick a number from above list: '))
    return num


def sampling_based_on_magnitude():
    ran_num_lst = []
    count = 0
    number = pick_a_number_from_list(lst)
    print(f'{number}\n')
    for i in range(1, 100):
        ran_num = random.choices(lst, weights=lst, k=1)
        ran_num_lst.append(ran_num)
    print(ran_num_lst)
    for i in ran_num_lst:
        if i[0] == number:
            count += 1
    print(f'\n {count}')


sampling_based_on_magnitude()
# print(lst)
# print(random.choices(lst, weights=lst, k=1))

#
