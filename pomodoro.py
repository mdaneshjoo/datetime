from datetime import timedelta
import time
import sys

x = 60  # second
i = 0
main_time = 25  # minute
short_break = 5  # minute
long_break = 15  # minute
while 1:

    print(timedelta(minutes=main_time))
    main_time = main_time - 1
    if main_time == 0:
        i = i + 1
    if main_time == 0 and i <= 3:
        print("short break is start : 5 minute", "===>", i,"th time break")
        while 1:
            print(timedelta(minutes=short_break))
            short_break = short_break - 1
            if short_break == 0:
                print("short break is ended")
                break
            time.sleep(x)
        main_time = 25
        short_break = 5
    if i == 4:
        print("long break is start : 15 minute")
        while 1:
            print(timedelta(minutes=long_break))
            long_break = long_break - 1
            if long_break == 0:
                print("long break is ended")
                break
            time.sleep(x)
        q = input('do you want to continue  ? (y/n)')
        if q == "n":
            sys.exit()
        main_time = 25
        short_break = 5
        long_break = 15
        i = 0
    time.sleep(x)
