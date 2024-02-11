from pynput import keyboard
import time
import threading
from tkinter.messagebox import showerror

class toggle:
	def __init__(self):
		self.start_key = None
		self.stop_key = None
		self.toggle = False
		self.thread = None
		self.listener = None
		self.hold = False

	def start_toggle(self):
		if not self.toggle:
			self.swap()
			self.listener = keyboard.Listener(
				on_press=self.on_press)
			self.listener.start()

	def set_key(self, start):
		with keyboard.Events() as events:
			event = events.get(10.0)
			if event is None:
				showerror("Error", "You did not press a key within ten seconds, try again")
				return 'try again'
			else:
				new_key = event.key.char if hasattr(event.key, 'char') else str(event.key)

				if start:
					if self.stop_key and new_key == self.stop_key:
						showerror("Error", "Start key and stop key cannot be the same, try again")
						return 'try again'
					self.start_key = new_key
				else:
					if self.start_key and new_key == self.start_key:
						showerror("Error", "Start key and stop key cannot be the same, try again")
						return 'try again'
					self.stop_key = new_key

				return new_key

	def stop_toggle(self):
		if self.toggle:
			self.swap()
			self.listener.stop()
			self.listener = None

	def on_press(self, key):
		try:
			if key.char == self.start_key:
				self.start_thread()
			elif key.char == self.stop_key:
				self.stop_thread()
		except AttributeError:
			pass

	def start_thread(self):
		if self.thread is None or not self.thread.is_alive():
			self.hold = True
			print('Starting Thread')
			with keyboard.Listener(on_press=self.on_press) as listener:
				self.thread = threading.Thread(target=self.hold_f)
				self.thread.start()

	def stop_thread(self):
		if self.thread and self.thread.is_alive():
			self.hold = False
			keyboard.Controller().release('f')
			self.thread.join()
			self.thread = None

	def hold_f(self):
		while self.hold and self.toggle:
			keyboard.Controller().press('f')

	def swap(self):
		self.toggle = not self.toggle
		if self.toggle:
			return 'on'
		else:
			return 'off'
		
	def both_keys_set(self):
		if self.start_key and self.stop_key:
			return True
		else:
			return False