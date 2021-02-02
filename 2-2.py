import random
n = random.randint(1,20)
count = 0
while True:
    a = int(input('number:'))
    if n >20 or n < 0:
        print("ERROR")
    else:
        if count == 5:
            print("just 5 times")
            break
        elif n<a:
            print("小一點")
            count = count+1
        elif n > a:
            print("大一點")
            count = count+1
        else:
            print("Bingo")  
            count = count+1
            print("你猜了"+str(count)+"次答對")
            break