print ("Hello, Apple Wi-Fi team!")

#Variables
latency = 25    # stores the number
device_name = "Apple Watch" # stores the text
is_connected = True  # stores yes/no 

#Functions
def check_latency(ms):
    if ms < 50:
        print("Great connection!")
    else: 
        print("Slow connection")

# def means define a function aka call this function later with chec_latency.

#Loops
for i in range(5):
    print("Ping #", i)
# this runs the print 5 times - like pinging a device 5 times

#Import
import subprocess
import time
import statistics 
# these toolboxes is built by someone else for you to borrow, subprocess lets you run system commands, time measures timing, statistics does math like averages. 

#pip
pip install ping3
# pip is like an app store for python tools. This installs the ping3 library while you will use to ping your watch.

