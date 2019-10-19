from pynput import keyboard
from pynput.keyboard import Key, Controller
import sys
import win32clipboard

# The currently active modifiers
current = set()
kb = Controller()

def req():
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

		kb.type(f"{em_list[-1]}, {em_list[0]}\t\t\t\t\t\tLogue, Shane\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
		for item in cleaning:
			clean = item.strip('\n')
			kb.type(rf"{clean}")
			pass
		print(f"{data}")
	except:
		pass
	
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

		kb.type(f"{em_list[-1]}, {em_list[0]}\t\t\t\t\t\tLogue, Shane\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t")
		for item in cleaning:
			clean = item.strip('\n')
			kb.type(rf"{clean}")
			pass
		print(f"{data}")
	except:
		pass


def on_press(key):
	if key == Key.page_up:
		req()
	elif key == Key.page_down:
		incident()
	else:
		pass

with keyboard.Listener(on_press=on_press) as listener:
	listener.join()
