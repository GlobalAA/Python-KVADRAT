import os  # os треба для першої функції read_from_file
import time

import pyautogui

num = int(input ("Введіть к-ть: "))
word = input ("Введіть слово: ")
Time = int(input("Через скільки почати: "))
filename = input("Введіть назву файлу: ")

def gui(num, word, Time):
	i = 0
	pyautogui.hotkey("win", "r")
	pyautogui.press("enter")
	time.sleep(2)
	pyautogui.typewrite("notepad")
	pyautogui.press("enter")
	time.sleep(Time)
	while i < num:
		pyautogui.typewrite(word)
		i += 1
		print("№", i)

def read_from_file(filename):
	if not os.path.exists(filename):
		return print("Файл не знайдено")
	with open(filename, 'r') as f:
		string = ""
		for line in f.readlines():
			string += line

		f.close()
		print(string)

def read_from_file(filename):
	try:
		with open(filename, 'r') as f:
			string = ""
			for line in f.readlines():
				string += line

			f.close()
			print(string)
	except FileNotFoundError:
		print("Файл не знайдено")

gui(num, word, Time)
read_from_file(filename)