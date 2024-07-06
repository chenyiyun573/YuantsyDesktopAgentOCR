
20240701 2249 PT
On Windows:
```
python -m venv .venv
.venv/Scripts/activate
python -m pip install -r requirements.txt -i https://mirrors.cloud.tencent.com/pypi/simple
```

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



