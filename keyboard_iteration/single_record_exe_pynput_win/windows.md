20240718 1512 PT from Yiyun Chen

### Part1: 

Part1 can all be recorded by pynput.
Chars are chars in like 'a', 'b', 'c', '1', '2', '3', etc.
Arrow keys are stored as 'Key.up', 'Key.down', 'Key.left', 'Key.right'.
-- Yiyun Chen 20240718 PT 

Character Keys
- Alphabet keys (A-Z) :26 keys 
- Number keys (0-9) : 10 keys 

The following: 9 keys

- Backtick (`) key
- Minus (-) and plus (+) keys
- Bracket keys ([ and ])
- Semicolon (;) key
- Quote (') key
- Comma (,) key
- Period (.) key
- Slash (/) key
- Backslash (\) key

Navigation Keys: 4 keys
- Arrow keys (up, down, left, right)

### Modifier Keys : 4 keys

Part2 can all be recorded by pynput.
These keys are recorded as 'Key.shift' (shift), 'Key.cmd' (win), 'Key.alt_l' (option), 'Key.ctrl_l' (control).
-- Yiyun Chen 20240718

Here, I observed a difference between mac and windows, I do not remembered clearly by the way, but when I long press the Key.shift and 'a' like keys, the logger will continues add action press, not once. Let me double check on mac if it is the same later. -Yiyun 20240718 



### Function Keys : 12 keys
- Function keys (F1-F12)

Part3 cannot be recorded correctly by pynput on macbook.
Among them, 
F1, F2, F3 cannot be recorded.

F7-F10 cannot be recorded. 

F4 - F6:
```
Logged: {'time': 1721341750.7710543, 'key': 'Key.media_volume_mute', 'action': 'press'}
Logged: {'time': 1721341750.885776, 'key': 'Key.media_volume_mute', 'action': 'release'}
Logged: {'time': 1721341751.2643785, 'key': 'Key.media_volume_down', 'action': 'press'}
Logged: {'time': 1721341751.4027438, 'key': 'Key.media_volume_down', 'action': 'release'}
Logged: {'time': 1721341756.5140607, 'key': 'Key.media_volume_up', 'action': 'press'}
Logged: {'time': 1721341756.6118388, 'key': 'Key.media_volume_up', 'action': 'release'}
```

F11:
```
Logged: {'time': 1721341839.5235255, 'key': 'Key.print_screen', 'action': 'press'}
Logged: {'time': 1721341839.594162, 'key': 'Key.print_screen', 'action': 'release'}
```

F12:
```
Logged: {'time': 1721341867.965997, 'key': 'Key.insert', 'action': 'press'}
Logged: {'time': 1721341868.0283682, 'key': 'Key.insert', 'action': 'release'}
```


### Special Purpose Keys
These keys exclude Fn are recorded as 'Key.esc' (escape), 'Key.space' (space), 'Key.tab' (tab), 'Key.caps_lock' (caps lock), 'Key.enter' (enter), 'Key.backspace' (backspace), 'Key.delete'(del)。

When Fn pressed, quick press and long press are the same on windows. 
```
Logged: {'time': 1721341973.7412522, 'key': None, 'action': 'press'}
Logged: {'time': 1721341973.8668778, 'key': '<255>', 'action': 'release'}
```


-- Yiyun Chen 20240718


- Power button (on some models) (most system do not allow this function by keyboard. )


