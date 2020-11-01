#! python3

import pyautogui as gui
import random
import datetime
import time

#gui.FAILSAFE will help you interrupt the script if the program is running and you take the cursor to any of the 4 corners of the screen.
#gui.PAUSE = 1
gui.FAILSAFE = True

#takes input for the amount of time you want cursor to keep moving
print('I am a program written in Python3')
print('''Skype automatically sets your status to 'Inactive/Away' if you do not move your cursor within 5 minutes''')
print('I will keep moving your cursor every 4 minutes. Skype will not show you away as long as your run me')
print('How long do you want me to run?')
x = input('Input hours (positive integer values only): ')
y = input('Minutes (positive integer values only): ')
x = int(x)
y = int(y)

#prints start time
start_time = datetime.datetime.now()
start = start_time.strftime('%H:%M:%S')
print("The start time is " + start)

#prints end time
stop_after = datetime.timedelta(hours = x, minutes = y)
end_time = start_time + stop_after
end = end_time.strftime('%H:%M:%S')
print("The end time is " + end)

#creates time_left variable which measures the time left for the script to end in seconds
time_left = (y*60) + (x*60*60)

#subtracting 500 pixels from width and height so that the cursor does not bump into the 
#upper right, lower right and lower left corners of the screen causing script to end prematurely
#upper left corner (0,0) will be taken care of in subsequent code
width, height = gui.size()
width -=  500
height -=  500

#Sprcify the minutes after which you want your cursor to move. 
after_minutes = 4

#till the time time_left = 0, this loop will keep the cursor moving at random intervals of time
while time_left>0:
    #move the cursor within the trimmed width and height, make sure it does not bump into (0,0) (adds 0.1 to random number in case it is = 0)
    random_width = ((random.random()+0.1)*width)
    
    random_height = ((random.random()+0.1)*height)
    
    gui.moveTo(random_width, random_height, duration = 0.25)
    
    #cursor_move_time_mins measures the time in mins which acts as the upper limit for the cursor to move
    #Want the cursor to move randomly between [0,5) minutes. It is with 5 minutes of inactivity that skype changes its status from 'active' to 'away'
    cursor_move_time_mins = after_minutes
    p = (random.random())*(cursor_move_time_mins*60)
    print('Next cursor move in : '+str(p)+' seconds')
    time.sleep(p)
    time_left -= p
    
print('Get back to work')