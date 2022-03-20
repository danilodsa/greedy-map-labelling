from random import randrange
import os

i = 0
while os.path.exists('tests/test%s.txt' % i):
    i += 1


max_height = 10
max_length = 20
n_elements = 500
path = 'tests/test{}.txt'
f = open('tests/test%s.txt' % i , 'a')

for e in range(n_elements):
    x1 = randrange(100)
    x2 = x1 + randrange(max_length) +1
    y1 = randrange(100)
    y2 = y1 + randrange(max_height) +1 

    f.write('L ' + str(e) + ' ' + str(x1) + ' ' + str(x2) + ' ' + str(y1) + ' ' + str(y2) + '\n')