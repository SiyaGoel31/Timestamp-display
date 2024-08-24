import time
t = time.strftime('%H:%M:%S')
print(t)
hour = int(time.strftime('%H'))

if(hour>=0 and hour<12):
    print("good morning !")
elif(hour>=12 and hour<16):
    print("good afternoon !")          
elif(hour>=16 and hour<20):
    print("good evening !")          
else:
    print("good night !")  