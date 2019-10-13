import keyboard
import sys
import win32clipboard

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


print(f"{em_list[-1]}, {em_list[0]}")
