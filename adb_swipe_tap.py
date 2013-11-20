import os
import re
from Tkinter import *
import subprocess


os.system('adb wait-for-device root')
os.system('adb wait-for-device remount')
os.system('adb wait-for-device devices')

devices = 'nil'
try:
	devices = subprocess.Popen(['adb', 'shell', 'dumpsys', 'window'], stdout=subprocess.PIPE, shell=True).stdout.read()
except Exception as e:
	print str(e)

display_size = re.search(r'cur=([0-9]+)x([0-9]+)', devices)

display_width = int(display_size.group(1))
display_height = int(display_size.group(2))

root = Tk()

def callback(event):
	global start_x
	global start_y

	start_x = event.x
	start_y = event.y

	print 'clicked at ', event.x, event.y

def release(event):
	global start_x
	global start_y

	if start_x == event.x and start_y == event.y:
		os.system('adb shell input tap {} {}'.format(event.x*2, event.y*2))
		print 'tap ({}, {})'.format(event.x*2, event.y*2)
	else:
		os.system('adb shell input swipe {} {} {} {}'.format(start_x*2, start_y*2, event.x*2, event.y*2))
		print 'swipe ({}, {}) -> ({}, {})'.format(start_x*2, start_y*2, event.x*2, event.y*2)

	print 'release at ', event.x, event.y

canvas_width = display_width/2
canvas_height = display_height/2
frame = Canvas(root, width=display_width/2, height=display_height/2)
frame.bind('<Button-1>', callback)
frame.bind('<ButtonRelease-1>', release)
frame.pack()
frame.create_line(0, canvas_height/2, canvas_width, canvas_height/2)
frame.create_line(canvas_width/2, 0, canvas_width/2, canvas_height)

root.mainloop()
