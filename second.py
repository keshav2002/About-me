import math
name = 'keshav'
prep = 'is about'
height = '6'
height = int(height)
conclusion = f'{name.upper()} {prep} {height} feet tall.'
print(conclusion)

name2 = 'shrinidhi'
length = '0.3'
length = float(length)
conclusion2 = f'{name2.upper()} {prep} {height - length} feet tall'
print(conclusion2)

name = input('what is your name?\n')
age = float(input('what is your age?\n'))
passion = input('what are you passionate about?\n')
food = input('what do you like to eat?\n')
print('===========================================================')
print(f'here are your details:\nname: {name}\nage: {age}\npassion: {passion}\nfood: {food}')

# numberFloat = input('Enter a floating number:\n')
# print(f'You entered this -> {float(numberFloat)}')
# print(f'{float(numberFloat)} type casted to integer looks like this {int(float(numberFloat))}')

# print('Ceil of {} = {} and floor of {} = {}'.format(float(numberFloat), 
#     math.ceil(float(numberFloat)), 
#     float(numberFloat), 
#     math.floor(float(numberFloat))))


