# print('Hello Python!')
# print(3/2)

# a = int(input('a='))
# a = 5
# print('S='+str(a*a))

# num1, num2 = map(float, input('Input numbers: ').split(','))
# print(num1, num2, num1+num2, sep='#', end='\n\n')

# name = input()
# print('Hello ', name, '!')

first_name = input('Name: ')
last_name = input('Family: ')
age = int(input('Age: '))
town = input('Town: ')
text = '{0}\n{1}\n{2} years old\nIvantown {3}.'
print(text.format(first_name, last_name, age, town))
