import time

def timer(t):
    while t: 
        min, sec = divmod(t, 60)
        print(min, sec)
        time.sleep(1)
        t=t-1
        
       
timing = input("enter time in seconds: ")
t = int(timing)
timer(t)