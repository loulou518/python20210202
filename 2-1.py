import random
n = random.randint(1,20)

while True:
    a = int(input('number:'))
    if n==a:
        print('答對')
        break
    else:
        print('答錯')