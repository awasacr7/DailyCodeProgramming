from threading import Thread
import time

def delayedrun(f,ms):
    time.sleep(ms)
    return f()

def myFunc(st):
    print('Hello %s we are testing the timer function '%(st))
    
j= Thread(target=delayedrun,  args=(lambda: myFunc('Awanesh'),1))
j.start()

print('Starting')
time.sleep(2)
print('Ending')