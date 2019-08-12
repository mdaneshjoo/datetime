from datetime import timedelta
import time
import winsound
import os


def zero(input):
    if input == '':
        return 0
    return int(input)


sec = zero(input("enter second:"))
minu = zero(input("enter minutes:"))
hour = zero(input("enter hours:"))
duration = 1000  # milliseconds
freq = 550  # Hz
# end = timedelta(hours=hour, minutes=minu, seconds=sec)
# timer = int(end.seconds) + 1
while 1:

    if sec == 0:
        sec = 60
        minu = minu - 1
        if minu == 0:
            minu = 60
            hour = hour - 1

    print(timedelta(hours=hour, minutes=minu, seconds=sec))
    sec = sec - 1
    if hour == 0 and minu == 0 and sec <= 5:
        winsound.Beep(freq, 250)  # play sound in windows
        # os.system('play -nq -t alsa synth {} sine {}'.format(0.25, freq)) # play sound in linux
    if hour == 0 and minu == 0 and sec == 0:
        # os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq)) # play sound in linux
        print(timedelta(hours=0, minutes=0, seconds=0))
        winsound.Beep(freq, duration)  # play sound in windows
        break

    time.sleep(1)
