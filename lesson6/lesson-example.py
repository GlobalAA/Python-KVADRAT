import os
import time

import pyautogui


class Gui:
	def __init__(self, num, word, filename) -> None:
		self.num = num
		self.word = word
		self.filename = filename

	def gui(self):
		i = 0
		pyautogui.hotkey("win", "r")
		pyautogui.press("enter")
		time.sleep(2)
		pyautogui.typewrite(self.filename)
		pyautogui.press("enter")
		time.sleep(1.5)
		while i < self.num:
			pyautogui.typewrite(self.word)
			i += 1
			print("№", i)

	def read_from_file(self):
		if not os.path.exists(self.filename):
			return print("Файл не знайдено")
		with open(self.filename, 'r') as f:
			string = ""
			for line in f.readlines():
				string += line

			f.close()
			print(string)

gui = Gui(5, "hello", "test.txt")