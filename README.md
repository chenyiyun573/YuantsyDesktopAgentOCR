On Windows:
```
python -m venv .venv
.venv/Scripts/activate
python -m pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple
```

On Mac
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple
```




20240701 2249 PT


Add OCR information into Single Agent, the code works.

There are several things to solve the next:

From user prompt, get a decription text of steps to execute.
Then by Agent - Computer Interface, convert the description text into precious code executions.

1. is the OCR location allied with the location of screen? because I see errors when GPT decide where to click - done;
2. sometimes, the GPT reponse with some other words include JSON, which we cannot convert to executions preciously, maybe use a small model to process it then pass it into execution.

3. Current, we do not need to use GPT to make decisions of planning, just write some knowledge, steps to execute then let the agent execute the text decription one by one. 


20240702 1256 PT
Now, I am thinking to code cmd recorder to recorder mouse and keyboard event and then execute the recorder cvs to replay.
But I found the replay's mouse click position is not correctly the same with the recorded result.
I coded coordinate_match to check it get the results that:
```
Automated clicking will start in 3 seconds...
Detected click at (200, 200)
Clicked at (100, 100)
Detected click at (2999, 200)
Clicked at (2900, 100)
Detected click at (200, 1999)
Clicked at (100, 1900)
```

Ask GPT 4 for it, given:
```
import ctypes

# Get the scaling factor
def get_scaling_factor():
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()  # Optional, makes the app DPI aware to get accurate scaling
    # Get the scaling factor
    return user32.GetSystemMetrics(0) / user32.GetSystemMetrics(78), user32.GetSystemMetrics(1) / user32.GetSystemMetrics(79)

scaling_factor_x, scaling_factor_y = get_scaling_factor()
print(f"Scaling Factor X: {scaling_factor_x}, Scaling Factor Y: {scaling_factor_y}")
```

seems not this problem: 
```
PS C:\Users\yiyun\Desktop\YuantsyDesktopAgentOCR> & c:/Users/yiyun/Desktop/YuantsyDesktopAgentOCR/.venv/Scripts/python.exe c:/Users/yiyun/Desktop/YuantsyDesktopAgentOCR/scale.py
Scaling Factor X: 1.0, Scaling Factor Y: 1.0
PS C:\Users\yiyun\Desktop\YuantsyDesktopAgentOCR>
```
seems not this way, I guess, recorder is correct, exe will double position scale.
Just divide 2 then try. 

20240702 0107 PT
Divide by 2 then execute (x,y) in cmd exe script works. So damn weird. 


20240702 2100 PT
For this subtask:
2. sometimes, the GPT reponse with some other words include JSON, which we cannot convert to executions preciously, maybe use a small model to process it then pass it into execution.

Now, I am thinking that using a small LLM model still face problems of non-precise response we want. 
For this sub-task, I am thinking that since transformer is a prediction model, we can define a small transformer, which takes description text (precise to human) to precise command (precise to machine.). It converts uncounterable possibilities of response into limited several response we want. Like fill one to two blanks with limited choices in exams. 


20240705-2204-PT
I downloaded the repo and tried it on my mac M1, it cannot work correctly.
I see the following drawbacks in just one try:
1. For multiple key pressed short cut like cmd+space to open search bar, it cannot be recorded and replayed correctly.
2. For mac, we often use the three-finger swipe left or right, my code cannot support it.
So, the code demo need a lot of modifications to support mac. 
Thus, I store current code repo as 1.0.0 which only support my several initial trials on windows. 


20240706-1545-PT
Then I tried to code MacOS application to perform these recorder and executor functions, but it doesn't work well.
https://github.com/chenyiyun573/20240706_LearningMacOSApp


20240706-1550-PT
But then it seems python can still execute gestures by using Apple Script, also the 3 finger swipe left or right can be executed by keyboard actions like ctrl+left or ctrl+right.

I will replace the cmd_exe.py and cmd_recorder.py with the support to key press and key release. the version 1.0.0 only support press and release as one action, now it will be two actions recorded and replayed. So I hope it can support multiple key events together. 


20240706-2040-PT
I tried to use pynput to execute multiple key events together, but it seems not work well for some gestures like 3 finger swipe left or right.
I also try to call Apple Scripts, it works well. 


Also, I modified the cmd_recorder.py and cmd_exe.py to support multiple key events together on Mac. The modification is like that, for example, the key press and key release will be recorded as two actions, and the key press and key release will be executed as two actions.

20240706-2051-PT
The pynput cannot support 'ctrl+left' or 'ctrl+right' on Mac. I use the pyautogui instead in cmd_exe2.py, it works well to support the 3 finger swipe left or right using ctrl+left or ctrl+right.


20240706-2103-PT
I found that the cvs of special key recorded by pynput cannot be executed by pyautogui in cmd_exe2.py successfully.
like the cmd and command below. So it need to be converted to the format of pyautogui.
This is modified into cmd_exe3.py.

This version of code is stored as 1.0.1. 


20240707-1304-PT
On the mac:
I found that pynput cannot record F1-F12 keys on mac. Another problem I face is that the pyautogui on the desktop screen of mac, it cannot execute cmd+space to open search bar. But on other app whole screen of mac, it can execute cmd+space to open search bar.
Next step, I will try to verify these problems.

This version of code is stored as 1.0.2



20240709 1228 PT
Added a script under frames, which can be used to find differences between two screenshots and take the first one as the base, second one as changes.
The result and some test cases are stored under the folder screenshots.

This version of code is stored as 1.0.3.


20240709 1641 PT
Doing: Provide OCR results and PNG to GPT4o web page chatting box directly and let it make one simple decision like "Find location of the search button then return (x,y) as click action". This decision can generalize a lot of different scenarios. 

I added a folder click_position_verify to verify the click position of the button on the web page from the result of GPT4 webpage. 

It works well. 

This version of code is stored as 1.0.4.


20240717 2144 PT
I added a folder keyboard_iteration to iterate the keyboard events on macbook.
Next todo is to test on windows. 

This version of code is stored as 1.0.5.


20240718 2324 PT 
Add windows part to the keyboard_iteration part. 
There are several unsolved problems in it.

This version of code is stored as 1.0.6

