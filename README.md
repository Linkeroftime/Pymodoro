# Pymodoro
My pomodoro productivity tool made in python

## Installation
To install this tool and have it executable from the command line, you should either add it to your path or move it to /usr/local/bin. The latter is the recommended implementation.

Requires:

ffmpeg
pydub
from /path/to/pomodoro:

$ source venv/bin/activate

$ pip install pydub

$ apt install ffmpeg (for debian based systems like ubuntu)/pacman -S ffmpeg (for arch based systems)

### Some specifics about Python scripting
The issue with python scripting vs Bash scripting is the virtual environment, as well as the python interpreter both running as seperate entities. This requires a small amount of work around.

How I got it to run on my system was this:
#### usr/local/bin/pomodoro
in usr/local/bin, I made an executable named pomodoro to run from the command line, but here's the catch:

#!/bin/bash

#Activate the virtual environment
$ source /path/to/pomodoro/venv/bin/activate

#Run the Pomodoro script
$ python /path/to/pomodoro/main.py

It is actually a Bash script!

This is needed because the python script needs some dependencies from the python virtual environment. This will need some editing because your path will likely look different from mine. I will be implementing an automated installation process soon so this will not be an issue.

#### How to configure the bash script
After copying and pasting the script into usr/local/bin/pomodoro and configuring it to match your download location of the script, you need to run chmod +x pomodoro to ensure that it can be run from the command line. This can be done with:

$ cd /usr/local/bin/

$ sudo chmod +x pomodoro

and enter your password.

If there are any issues, please let me know!
enjoy your productivity!

## Usage
for now, just run pomodoro and you will be prompted for a command.
type 'start' to begin.
It will start a timer for 25 minutes and count down until it hits 0, at which case it will play an alarm that will then prompt you to take a break for 5 minutes. This process repeats until you type exit at a prompt or press ctrl + C

That should be all. Let me know if there are any issues and I will make certain that I get back to you!



TODO: 
add automated installation script

add command line args for different times (work and break)

eg: pomodoro --work 25 --break 5

this will allow pomodoro to be more dynamic

allow for a modular alarm sound
