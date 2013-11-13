import os
import time
import sys
import thread
import threading
import string
import glob
import re
import shutil
from xml.dom.minidom import *
import Tkinter as tk
from Tkinter import *
from datetime import datetime
from time import strftime, localtime
import tkFileDialog
import threading

keycode_table = [
	'UNKNOWN',
	'SOFT_LEFT',
	'SOFT_RIGHT',
	'HOME',
	'BACK',
	'CALL',
	'ENDCALL',
	'0',
	'1',
	'2',
	'3',
	'4',
	'5',
	'6',
	'7',
	'8',
	'9',
	'STAR',
	'POUND',
	'DPAD_UP',
	'DPAD_DOWN',
	'DPAD_LEFT',
	'DPAD_RIGHT',
	'DPAD_CENTER',
	'VOLUME_UP',
	'VOLUME_DOWN',
	'POWER',
    'CAMERA',
    'CLEAR',
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z',
    'COMMA',
    'PERIOD',
    'ALT_LEFT',
    'ALT_RIGHT',
	'SHIFT_LEFT',
    'SHIFT_RIGHT',
    'TAB',
    'SPACE',
    'SYM',
    'EXPLORER',
    'ENVELOPE',
    'ENTER',
    'DEL',
    'GRAVE',
    'MINUS',
    'EQUALS',
    'LEFT_BRACKET',
    'RIGHT_BRACKET',
    'BACKSLASH',
    'SEMICOLON',
    'APOSTROPHE',
    'SLASH',
    'AT',
    'NUM',
    'HEADSETHOOK',
    'FOCUS',
    'PLUS',
    'MENU',
    'NOTIFICATION',
    'SEARCH',
]

html_src = '''
<!doctype html>
<head>
	<script>
		i= 0;

		window.onload = function() {
			setInterval(function() {
				window.location.reload(true);
				document.getElementById('img_src').attribute('src') = 'temp' + '0' + '.png';
				++i;
			}, 1500);
		}



	</script>

</head>

<body>
	<img id="img_src" src="temp0.png" width="30%" height="30%"/>

</body>
</html>
'''



# GUI path dialog
class AdbKeyboardDialog:

	def __init__(self, root):

		# root
		self.root = root

		self.root_width = 500 
		self.root_height = 700
		root.geometry('{}x{}'.format(self.root_width, self.root_height))


		root.resizable(0, 0)
		scrollbar = Scrollbar(root)
		scrollbar.pack(side=RIGHT, fill=Y)

		# key bind
		root.bind('<Escape>', self.exit)
		root.protocol('WM_DELETE_WINDOW', self.exit)
		root.bind_all('<MouseWheel>', self._on_mousewheel)

		# cancel button
		for i, button_text in enumerate(keycode_table):

			# closure
			def adb_keyevent(keycode, key_name):
				def execute():
					print 'Send a key event: {}'.format(key_name)
					os.system('adb shell input keyevent {}'.format(keycode))
				return execute

			Button(root, text=button_text, font='Consolas 10', command=adb_keyevent(i, button_text)).pack()


		root.mainloop()


	def exit(self, event=None):
		sys.exit(0)
	
	def _on_mousewheel(self, event):
		self.yview(-1*(event.delta/120), "units")

def adb_display():

	viewer = open('adb_viewer.html', 'w')
	viewer.write(html_src)
	viewer.close()

	os.system('start adb_viewer.html')

	while True:
		take_screenshot()
		time.sleep(0.1)


def take_screenshot():
	os.system('adb shell screencap -p /data/temp{}.png'.format(0))
	os.system('adb pull /data/temp{}.png .'.format(0))

os.system('adb wait-for-device root')
os.system('adb wait-for-device remount')
os.system('adb wait-for-device devices')

threading.Thread(target=adb_display).start()
threading.Thread(target=AdbKeyboardDialog, args=(tk.Tk(),)).start()


'''
adb shell /system/bin/screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png screenshot.png
'''


