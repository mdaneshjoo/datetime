from datetime import datetime
from datetime import timedelta
import time
import sys
import keyboard

S = 0
H = 0
M = 0

while 1:

    S = S + 1
    if S == 60:
        S = 0
        M = M + 1
        if M == 60:
            M = 0
            H = H + 1
    print(timedelta(hours=H, minutes=M, seconds=S))
    if keyboard.is_pressed('Esc'):
        sys.exit()
    time.sleep(1)
