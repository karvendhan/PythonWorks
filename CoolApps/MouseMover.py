import win32api 
import time
import math

time.sleep(20)

for i in range(5):
    x=int(500+math.sin(math.pi*i/100)*500)
    y=int(500+math.cos(i)*100)
    win32api.SetCursorPos((x,y))
    time.sleep(1)

print("hello world")

