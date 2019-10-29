from pynput import keyboard
from pynput.keyboard import Key, Controller
import sys
import win32clipboard
import time

# The currently active modifiers
current = set()
kb = Controller()

#Creates the request function
def req():
	try:
		#Opens and reads the clipboard data. This then closes it so other programs can then use the clipboard again.
		win32clipboard.OpenClipboard()
		data = win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()
		
		#This grabs the users name from data. This will later be used for filling out affected end user
		stripping = data.split("\n")[0]
		get_name = stripping.split("Name: ")[-1]
		
		#Splitting the users first name and last name so they are different items
		lname = get_name.split(' ', 1)

		em_list = []
		
		#Appending the names to the above empty list
		for item in lname:
			strip_word = item.strip()
			em_list.append(strip_word)
		
		cleaning = data.strip('\r')
		
		#Fills out affected end user and tabs down to assignee
		#Have put time.sleep in to let R12 load data properly. Found script would sometimes fail because it didn't load fast enough.
		kb.type(f"{em_list[-1]}, {em_list[0]}")
		time.sleep(1)
		#6 tabs
		tab_count = 0
		while tab_count < 6:
			kb.type("\t")
			tab_count += 1
		kb.type("Logue, Shane")
		time.sleep(1)
		tab_counter = 0
		while tab_counter < 19:
			kb.type("\t")
			tab_counter += 1
		#19 tabs
		#This write out each line that is found in the clipboard. Had to do it this way as kb.type was inserting random new lines.
		#This way hopefully prevents this from happening
		kb.press(Key.ctrl)
		kb.press('a')
		kb.release('a')
		kb.release(Key.ctrl)
		time.sleep(1)
		for item in cleaning:
			clean = item.strip('\n')
			kb.type(rf"{clean}")
			pass
		print(f"{data}")
	except Exception as e:
		print(e)
	
def incident():
	try:
		win32clipboard.OpenClipboard()
		data = win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()

		stripping = data.split("\n")[0]
		get_name = stripping.split("Name: ")[-1]

		lname = get_name.split(' ', 1)

		em_list = []

		for item in lname:
			strip_word = item.strip()
			em_list.append(strip_word)

		cleaning = data.strip('\r')

		kb.type(f"{em_list[-1]}, {em_list[0]}")
		time.sleep(1)
		tab_count = 0
		while tab_count < 6:
			kb.type("\t")
			tab_count += 1
		kb.type("Logue, Shane")
		time.sleep(1)
		#tab 23
		tab_counter = 0
		while tab_counter < 23:
			kb.type("\t")
			tab_counter += 1
		kb.press(Key.ctrl)
		kb.press('a')
		kb.release('a')
		kb.release(Key.ctrl)
		time.sleep(1)
		for item in cleaning:
			clean = item.strip('\n')
			kb.type(rf"{clean}")
			pass
		print(f"{data}")
	except Exception as e:
		print(e)

#Check what each key does
def on_press(key):
	if key == Key.page_up:
		req()
	elif key == Key.page_down:
		incident()
	else:
		pass
#Starts listening for key presses
with keyboard.Listener(on_press=on_press) as listener:
	listener.join()
