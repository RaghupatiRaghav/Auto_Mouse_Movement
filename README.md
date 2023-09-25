# Auto_Mouse_Movement

## About
The Python script in this repository automatically moves the cursor randomly within 4 minutes. You can increase or decrease the default time for cursor movement.

Code is written in Python3 and uses [pyautogui module](https://pyautogui.readthedocs.io/en/latest/) to achieve cursor movement automation. It also uses [datetime](https://docs.python.org/3/library/datetime.html), [time](https://docs.python.org/3/library/time.html) and [random](https://docs.python.org/3/library/random.html) modules to time the automated cursor movement. After first movement, the code stops running until the next cursor move to save computational resources. This process is repeated till the time you want the code to run.

## Getting Started:

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