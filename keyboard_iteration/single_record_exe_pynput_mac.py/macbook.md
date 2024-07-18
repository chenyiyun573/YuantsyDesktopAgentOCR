20240717 21:25 PT from Yiyun Chen

### Part1: 

Part1 can all be recorded by pynput.
Chars are chars in like 'a', 'b', 'c', '1', '2', '3', etc.
Arrow keys are stored as 'Key.up', 'Key.down', 'Key.left', 'Key.right'.
-- Yiyun Chen 20240717 2129 PT 

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
These keys are recorded as 'Key.shift' (shift), 'Key.cmd' (command), 'Key.alt' (option), 'Key.ctrl' (control).
-- Yiyun Chen 20240717 2132 PT

- Shift keys (left and right)
- Control keys (left and right)
- Option keys (left and right, also known as Alt)
- Command keys (left and right)

### Function Keys : 12 keys
- Function keys (F1-F12)

Part3 cannot be recorded correctly by pynput on macbook.
Among them, 
F1, F2 cannot be recorded.

F3:
```
Logged: {'time': 1721277385.1839528, 'key': None, 'action': 'press'}
Logged: {'time': 1721277385.25838, 'key': '<160>', 'action': 'release'}
```

F4:
```
Logged: {'time': 1721277413.7830331, 'key': None, 'action': 'press'}
Logged: {'time': 1721277413.805185, 'key': '<177>', 'action': 'release'}
```

F5:
```
Logged: {'time': 1721277427.600182, 'key': None, 'action': 'press'}
Logged: {'time': 1721277427.6006458, 'key': '<176>', 'action': 'release'}
```

F6:
```
Logged: {'time': 1721277460.557075, 'key': None, 'action': 'press'}
Logged: {'time': 1721277460.634762, 'key': '<178>', 'action': 'release'}
```

F7 and F9 cannot be recorded. 

F8:
```
Logged: {'time': 1721277499.983263, 'key': 'Key.media_play_pause', 'action': 'press'}
Logged: {'time': 1721277500.0535738, 'key': 'Key.media_play_pause', 'action': 'release'}
```

F10 - F12 are the followings:
```
Logged: {'time': 1721277518.27875, 'key': 'Key.media_volume_mute', 'action': 'press'}
Logged: {'time': 1721277518.3489091, 'key': 'Key.media_volume_mute', 'action': 'release'}
Logged: {'time': 1721277518.612949, 'key': 'Key.media_volume_down', 'action': 'press'}
Logged: {'time': 1721277518.686063, 'key': 'Key.media_volume_down', 'action': 'release'}
Logged: {'time': 1721277518.9409542, 'key': 'Key.media_volume_up', 'action': 'press'}
Logged: {'time': 1721277519.005931, 'key': 'Key.media_volume_up', 'action': 'release'}
```



### Special Purpose Keys
These keys exclude Fn are recorded as 'Key.esc' (escape), 'Key.space' (space), 'Key.tab' (tab), 'Key.caps_lock' (caps lock), 'Key.enter' (enter), 'Key.backspace' (delete)。

When Fn pressed, quick press and long press will be different, I guess it's due to the language switch function defined by Apple MacOS. 
```
Logged: {'time': 1721277766.2400682, 'key': '<63>', 'action': 'release'}
Logged: {'time': 1721277766.333198, 'key': '<63>', 'action': 'release'}
Logged: {'time': 1721277766.333954, 'key': None, 'action': 'press'}
Logged: {'time': 1721277766.334629, 'key': '<179>', 'action': 'release'}
Logged: {'time': 1721277767.9967859, 'key': '<63>', 'action': 'release'}
Logged: {'time': 1721277768.090833, 'key': '<63>', 'action': 'release'}
Logged: {'time': 1721277768.091676, 'key': None, 'action': 'press'}
Logged: {'time': 1721277768.092322, 'key': '<179>', 'action': 'release'}
Logged: {'time': 1721277769.5664692, 'key': '<63>', 'action': 'release'}
Logged: {'time': 1721277769.6842399, 'key': '<63>', 'action': 'release'}
Logged: {'time': 1721277769.6857321, 'key': None, 'action': 'press'}
Logged: {'time': 1721277769.686433, 'key': '<179>', 'action': 'release'}
```


-- Yiyun Chen 20240717 2135 PT

- Escape (Esc) key
- Space bar
- Tab key
- Caps Lock key
- Enter/Return key
- Delete (Backspace) key
- Fn key (Function key, used to access secondary functions of other keys)


- Power button (on some models) (most system do not allow this function by keyboard. )

These keys represent the typical layout on a Mac keyboard, which may slightly vary depending on the model and region.