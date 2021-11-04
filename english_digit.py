digit = int(input('Input digit [0-9]: '))

output = str(digit)+' => '
if digit == 0:
    output += 'zero'
elif digit == 1:
    output += 'one'
elif digit == 2:
    output += 'two'
elif digit == 3:
    output += 'three'
elif digit == 4:
    output += 'four'
elif digit == 5:
    output += 'five'
elif digit == 6:
    output += 'six'
elif digit == 7:
    output += 'seven'
elif digit == 8:
    output += 'eight'
elif digit == 9:
    output += 'nine'
else:
    output += 'invalid digit'

print(output)
