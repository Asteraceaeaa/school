import time

second = 60

while second:
    timer = f'{second:02d}'
    print(timer,end='\r')
    time.sleep(1)
    second-=1
    if second == 50:
        print("осталось 50 секунд")
print("0.0")

        
