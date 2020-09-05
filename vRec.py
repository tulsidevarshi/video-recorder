#!/usr/bin/env python3


# This code was developed by Devarshi Singh
# as a practice to learn python.
# Any misuse of this code the developer will not be responsible.
# Use this code on your laptops for learning purpose only.


# It takes about 100ms for pyautogui for 1 click
# So, all together it's 10fps. At best.
# Keep looking my github for more advanced video recorder soon. 
# fps = 1000ms/(no of pics)

import os
import pyautogui
import keyboard
import cv2
import glob
from PIL import Image


def main():
	take_screenshot()
	make_video()
	pyautogui.alert("Your video is ready!")
	#dump_all_image_files()




def take_screenshot():
	count = 0

	while True:
		count+=1
		snap = pyautogui.screenshot()
		pic = "im00"+str(count)+".png"
		snap.save(pic)

		if keyboard.is_pressed('q'):
			call = pyautogui.confirm('Shall I end the recording?')
			if call == "OK":
				return
			else:
				continue


def make_video():
	image_size = Image.open("im001.png").size
	# https://stackoverflow.com/questions/30230592/
	# loading-all-images-using-imread-from-a-given-folder
	currPath = str(os.getcwd())
	path = currPath.replace("\\","/")
	path1 = path+"/*.png"

	images = []
	images = [cv2.imread(file) for file in glob.glob(path1)]

	name = pyautogui.prompt("Please name your output file name without extension: ")

	outputFile = name + ".mp4"
	#video writer object
	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	vwo = cv2.VideoWriter(outputFile, fourcc, 10, image_size)

	for i in range(len(images)):
		vwo.write(images[i])
	vwo.release()


#def dump_all_image_files():


if __name__ == "__main__" : main()