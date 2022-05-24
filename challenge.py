print("""choose from the following options
1 Go swimming
2 Learn python
3 Eat pizza
4 Sleep
5 Exit""")

option = 0
while True:
    option = input()

    if option == '5':
        break
    elif option in '12345':
        print(f'You chose {option}')
    else:
        print("""choose from the following options
        1 Go swimming
        2 Learn python
        3 Eat pizza
        4 Sleep
        5 Exit""")
    # if option == 1:
    #     print('Go swimming')
    # elif option == 2:
    #     print('Learn python')
    # elif option == 3:
    #     print('Eat pizza')
    # elif option == 4:
    #     print('Sleep')
    # else:
    #     print('Invalid answer')
    #     print("""choose from the following options
    #     1 Go swimming
    #     2 Learn python
    #     3 Eat pizza
    #     4 Sleep
    #     5 Exit""")
