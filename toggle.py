from pynput import keyboard
import time
import threading

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
				return 'You did not press a key within ten seconds, try again'
			else:
				if hasattr(event.key,'char'):
					if start:
						self.start_key = event.key.char
					else:
						self.stop_key = event.key.char
					return event.key.char
				else:
					if start:
						self.start_key = event.key
					else:
						self.stop_key = event.key
					return event.key

	def stop_toggle(self):
		if self.toggle:
			self.swap()
			if self.listener:
				self.listener.stop()
				self.listener.join()

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
			self.thread.stop()
			self.thread = None

	def hold_f(self):
		while self.hold:
			keyboard.Controller().press('f')

	def swap(self):
		self.toggle = not self.toggle
		if self.toggle:
			return 'on'
		else:
			return 'off'
		