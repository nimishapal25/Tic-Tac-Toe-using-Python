# enumerate returns pairs of values - we get
# index position and item, as a pair of values
# the first value is index position and the second
# value is the item

Engineering = ['Computer Science', 'Electrical', 'Mechanical', 'Electronics']
# for number, branch in enumerate(Engineering):
#     print(number + 1, branch)

valid_choices = [str(idx) for idx, i in enumerate(Engineering)]
# for i in range(1, len(Engineering) + 1):
#     valid_choices.append(str(i))
current_choice = '-'
current_list = []
while current_choice != '0':
    if current_choice in valid_choices:
        print(f'Adding{current_choice}')
        index = int(current_choice) - 1
        chosen_item = Engineering[index]
        if chosen_item in current_list:
            print('Already chosen')
        else:
            current_list.append(chosen_item)
    else:
        print('Please enter the option given below')
        for num, choice in enumerate(Engineering):
            print(f'{num + 1}: {choice}')

    current_choice = input()
print(current_list)