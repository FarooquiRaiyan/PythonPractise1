import datetime
import winsound
import time
duration=10000
freq= 440
days={'18-03-2025':'18:51',
      '19-03-2025':'18:51',
      '20-03-2025':'18:51',
      '21-03-2025':'18:51',
      '22-03-2025':'18:51',
      '23-03-2025':'18:51',
      '24-03-2025':'18:51',
      '25-03-2025':'18:51',
      '26-03-2025':'18:51',
      '27-03-2025':'18:51',
      '28-03-2025':'18:51',
      '29-03-2025':'18:51',
      '30-03-2025':'18:51',
      }
print(days, type(days))
def chcktime():
    todaystr =datetime.datetime.today().strftime("%d-%m-%Y")
    current_time=datetime.datetime.now().strftime("%H:%M")
    for key,val in days.items():
        if key == todaystr  and val == current_time:
            winsound.Beep(frequency=freq,duration=duration)
            print("beeping...")
            break
        
while True:
    chcktime()
    time.sleep(30)