from pynput import keyboard
import time
import threading

class toggle:
	def __init__(self):
		self.start_key = None
		self.stop_key = None
		self.toggle = False
		self.thread = None

	def start_toggle(self):
		if not self.toggle:
			self.swap()

	def set_start_key(self):
		with keyboard.Events() as events:
			event = events.get(10.0)
			if event is None:
				return('You did not press a key within ten seconds, try again')
			else:
				return('{}'.format(event))
			
	def set_stop_key(self):
		with keyboard.Events() as events:
			event = events.get(10.0)
			if event is None:
				return('You did not press a key within ten seconds, try again')
			else:
				return('{}'.format(event))

	def stop_toggle(self):
		if self.toggle:
			self.swap()
			if self.listener:
				self.listener.stop()
				self.listener.join()

	def on_press(self, key):
		try:
			if key.char == 'f':
				self.start_thread()
			elif key.char == 'c':
				self.stop_thread()
		except AttributeError:
			pass

	def start_thread(self):
		if self.thread is None and not self.thread.is_alive():
			self.thread = threading.Thread(target=self.hold_f)
			self.thread.start()

	def stop_thread(self):
		if self.thread and self.thread.is_alive():
			self.thread.join()
			self.thread = None

	def hold_f(self):
		while self.toggle:
			pyautogui.press('f')
			time.sleep(0.1)

	def swap(self):
		self.toggle = not self.toggle
		if self.toggle:
			return 'on'
		else:
			return 'off'
		