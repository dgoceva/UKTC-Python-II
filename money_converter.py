amount = float(input('Amount = '))
money = input('From = ')
out_money = input('To = ')

result = amount
if money == 'USD':
    result *= 1.79549  # result = result * 1.79549
elif money == 'EUR':
    result *= 1.95583
elif money == 'GBP':
    result *= 2.53405
elif money != 'BGN':
    print('Invalid money')

if out_money == 'USD':
    result /= 1.79549  # result = result * 1.79549
elif out_money == 'EUR':
    result /= 1.95583
elif out_money == 'GBP':
    result /= 2.53405
elif out_money != 'BGN':
    print('Invalid money')

print('{0} {1} = {2} {3}'.format(amount, money, round(result, 2), out_money))
