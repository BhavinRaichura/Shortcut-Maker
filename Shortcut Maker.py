###################################################################
# Library 

from pynput import keyboard
import os

###################################################################
# Storage part 
# The key combination to check
COMBINATIONS = []


dic_key ={}


###################################################################
# 
# The currently active modifiers
current = set()

# Add new key
def add_key(prog, chr,syskey='tab'):
    COMBINATIONS.append({keyboard.Key.tab, keyboard.KeyCode(char=chr.lower())})
    COMBINATIONS.append({keyboard.Key.tab, keyboard.KeyCode(char=chr.upper())})
    dic_key[keyboard.KeyCode(char=chr.lower())]=[prog,syskey]
    dic_key[keyboard.KeyCode(char=chr.upper())]=[prog,syskey]

# Remove key
def remove_key(chr):
	COMBINATIONS.remove({keyboard.Key.tab, keyboard.KeyCode(char=chr.lower())})
	COMBINATIONS.remove({keyboard.Key.tab, keyboard.KeyCode(char=chr.upper())})
	dic_key[keyboard.KeyCode(char=chr.lower())]=None
    	dic_key[keyboard.KeyCode(char=chr.upper())]=None

# function for execute the program
def execute(str):
    print(str)
    prog_cmd=dic_key[str][0]
    print(dic_key[str][0])    
    os.system(prog_cmd)
    print (prog_cmd)
   # os.system(prog_cmd)
    #print (prog_cmd)

#######################################################################
# Function for checking key combination
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute(key)

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
