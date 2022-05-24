activity = input('What do you want to do toady?')

if "cinema" not in activity:
    print('But I want to go to cinema')
else:
    print(f"Let's go to {activity}")

name = input('Enter your name: ')
age = (int(input('Enter your age: ')))

if 18 <= age <= 30:
    print(f'Welcome {name} to the gala!!')
else:
    print(f'Come back in {18-age} years')
