points = int(input('Input points: '))

bonus_points = 0
if points <= 100:
    bonus_points = 5
elif points > 1000:
    bonus_points = points*0.1
else:
    bonus_points = points*0.2

if points % 2 == 0:  # even number
    bonus_points += 1
elif points % 10 == 5:  # 105/10 => 10 and reminder 5
    bonus_points += 2

print(f'Points: {points} Bonus: {bonus_points} All: {points+bonus_points}')
