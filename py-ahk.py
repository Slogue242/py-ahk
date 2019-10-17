from pynput import keyboard
from pynput.keyboard import Key, Controller
import sys
import win32clipboard

# The currently active modifiers
current = set()
kb = Controller()

# Function to be executed
def execute():
	try:
		# Get's all current data in clipboard
		win32clipboard.OpenClipboard()
		data = win32clipboard.GetClipboardData()
		win32clipboard.CloseClipboard()
		#Starts split data so it can be used in the further
		stripping = data.split("\n")[0]
		get_name = stripping.split("Name: ")[-1]

		lname = get_name.split(' ', 1)

		em_list = []
		#Add's Name to list so it will be easier to call later on
		for item in lname:
			strip_word = item.strip()
			em_list.append(strip_word)
		#Printing the name and such
		print(f"{em_list[-1]}, {em_list[0]}\tLogue, Shane")
		kb.type(f"{em_list[-1]}, {em_list[0]}\tLogue, Shane")
		pass
	except:
		pass
	
#Looks for a certain key press and then runs the function
def on_press(key):
	if key == Key.end:
		execute()
	else:
		pass
#Starts keyboard listening
with keyboard.Listener(on_press=on_press) as listener:
	listener.join()
