from tkinter import *

def listpop(track):
    track += 1
    (retValue, retValue2) = (timeList[track], taskList[track])
    return (retValue, retValue2)
    
def startcommand():
    global ListLength
    ListLength = len(timeList)
    counter = 0
    while counter != ListLength:
        (NextTime, NextTask) = listpop()
        Bool = False
        while Bool == False:
            Time = strftime("%H:%M:%S", gmtime())
            Time = Time.split(':')
            if (int(Time[0]) + 9) > 24:
                Time[0] = str(int(Time[0]) + 9 - 24)
            else:
                Time[0] = int(Time[0]) + 9
            Time = ':'.join(map(str, Time))
            #print Time, NextTime, Bool
            if Time == NextTime:
                Bool = True
        call(["play","/home/edward/Downloads/robot.wav"])
        showinfo("Reminder", "It is time to %s" % NextTask)
        counter += 1
        #print counter