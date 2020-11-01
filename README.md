# Escaping Office Vigilantism

## About
Many offices use Skype for intra-office Instant Messaging (IM). While a decent tool for communication, Skype updates employees' status - 'Available', 'Off Work', 'Be Right Back', 'Busy' subject to employees' activity. The most notorious of them though, are 'Inactive' and 'Away'. If the employee does not move his/her cursor or hit a key on the keyboard, the status is updated to 'Inactive' after a default time of 5 minutes before updating to 'Away' after a default time of 10 minutes. The top it all off, Skype also shows the time elapsed since last computer activity (for instance, '_Away-20 minutes_') This incapacitates the employee from taking breaks in the absence (or presence) of work because an overzealous manager is keeping a constant watch. If you can run the Python script in this repository on your system, it automatically moves the cursor randomly within 4 minutes. Of course, you can increase or decrease this time.

Code is written in Python3 and uses [pyautogui](https://pyautogui.readthedocs.io/en/latest/) to achieve cursor movement automation. It also uses the [datetime](https://docs.python.org/3/library/datetime.html), [time](https://docs.python.org/3/library/time.html) and [random](https://docs.python.org/3/library/random.html) to time the automated cursor movement. After first movement, the code stops running until the next cursor move to save computing resources. This process is repeated till the time you want the code to run.

## How To Use:

#### Downloading Script:

1. Clone the repository or directly download file *escaping_vigilantism.py*.
2. Drag and drop the downloaded file into a python environment (such as Anaconda Terminal or Windows Command Prompt, if it can run Python3).
3. The terminal will now ask you to input the duration in hours and minutes (both of these inputs should be positive integer values) for which you want the script to run. For instance, if I want the script to run for half an hour, my input would be *Input hours (positive integer values only): 0* and *Input minutes (positive integer values only): 30*
4. The terminal will now show you the start time, the end time and the time for next cursor movement. 
5. To stop the script prematurely, simply press *Ctrl* and *c* simultaneously. 

#### Downloading Jupyter Notebook:
1. Clone the repository or directly download file *escaping_vigilantism.ipynb*.
2. Open the downloaded file in Jupyter Notebook/Lab and press Ctrl+Enter to run.
3. Go to Kernel -> Restart Kernel to interrupt the run prematurely.

### Changing Default Cursor Movement Time:
The automated cursor movement takes place no later than 4 minutes as default. You can change this as per your requirement. Time in minutes for cursor movement is specified in *after_minutes* variable in line 44, set it to any non negative integer value.






