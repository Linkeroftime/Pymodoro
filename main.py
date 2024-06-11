#!/usr/bin/env python3

import argparse
import time
import datetime
import sys
from pydub import AudioSegment
from pydub.playback import play

alarm = AudioSegment.from_wav("/home/rylee/coding/python/pomodoro/[ONTIVA.COM] complete sound effect free -HQ.wav")


parser = argparse.ArgumentParser()

count = 0

# Create class for countdown
def countdown ():
    global count
    while True:
        if count % 2 == 0:
            minutes=25
        else:
            minutes=5
        try:
            # Calculate total number of seconds
            total_seconds = minutes * 60
            # While loop checks if total_seconds reaches zero
            # If not zero, decrements total time by one second
            while total_seconds > 0:
                # Timer = time left on countdown
                timer = datetime.timedelta(seconds = total_seconds)

                # Prints time left on timer
                print(timer, end="\r")
                # Delays the program for one second
                time.sleep(1)
                # Reduce total time by one second
                total_seconds -= 1
            play(alarm)
            if count % 2 == 0:
                print("It is time to take a break")
                ok = input("type 'ok' to take a break or 'exit' to exit!\n")
                if ok == "ok":
                    count+=1
                    continue
                else:
                    print("\nGoodbye!")
                    sys.exit(0)
            else:
                print("Time to get back to work!")
                ok = input("type 'ok' to get back to work or 'exit' to exit!\n")
                if ok == "ok":
                    count+=1
                    continue
                else:
                    print("\nGoodbye!")
                    sys.exit(0)
        except KeyboardInterrupt:
            # quit
            print("\nGoodbye!")
            sys.exit()
       

try:
    start = input("Welcome to pymodoro! type 'start' to begin!\n")

    if start == "start":
        countdown()
    else:
        print("\nGoodbye!")
        sys.exit(0)
except KeyboardInterrupt:
    print("\nGoodbye!")
    sys.exit(0)

