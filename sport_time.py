time1 = int(input('Time 1 [1-50], sec: '))
time2 = int(input('Time 2 [1-50], sec: '))
time3 = int(input('Time 3 [1-50], sec: '))

sum = time1 + time2 + time3
print('All time: {0} min:{1:02d} sec'.format(sum//60, sum % 60))
