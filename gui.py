import tkinter as tk
from pynput import keyboard
import threading
import pyautogui
import time
import toggle as tg

class ToggleApp:

	def __init__(self, master):
		self.master = master
		self.master.title("Toggle GUI")

		self.toggle_button = tk.Button(master, text="Start Toggle", command=self.start_toggle)
		self.toggle_button.pack(pady=10)

		self.stop_button = tk.Button(master, text="Stop Toggle", command=self.stop_toggle)
		self.stop_button.pack(pady=10)
		self.stop_button.config(state=tk.DISABLED)

		self.toggle = tg.toggle()
		self.listener = None

	def start_toggle(self):
		self.toggle_button.config(state=tk.DISABLED)
		self.stop_button.config(state=tk.NORMAL)
		self.toggle.start_toggle()
		self.listener = keyboard.Listener(on_press=self.on_press)

	def stop_toggle(self):
		self.toggle_button.config(state=tk.NORMAL)
		self.stop_button.config(state=tk.DISABLED)
		self.toggle.stop_toggle()
		if self.listener:
			self.listener.stop()
			self.listener.join()
			self.listener = None

	def on_press(self, key):
		self.toggle.on_press(key)

if __name__ == "__main__":
	root = tk.Tk()
	app = ToggleApp(root)
	root.mainloop()
