import os
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

]


# GUI path dialog
class AdbKeyboardDialog:

	def __init__(self, root):

		# root
		self.root = root

		self.root_width = 500 
		self.root_height = 500
		root.geometry('{}x{}'.format(self.root_width, self.root_height))

		root.resizable(0, 0)

		# key bind
		root.bind('<Escape>', self.exit)
		root.protocol('WM_DELETE_WINDOW', self.exit)

		# cancel button
		for i, button_text in enumerate(keycode_table):

			# closure
			def adb_keyevent(keycode, key_name):
				def execute():
					print 'Send a key event: {}'.format(key_name)
					os.system('adb shell input keyevent {}'.format(keycode))
				return execute

			Button(root, text=button_text, font='Consolas 14', command=adb_keyevent(i, button_text)).grid(row=i/3, column=i%3)


		root.mainloop()


	def exit(self, event=None):
		sys.exit(0)



AdbKeyboardDialog(tk.Tk())
