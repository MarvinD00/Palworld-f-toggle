from tkinter import *
from tkinter import ttk
import toggle as tg

class ToggleApp:

	def __init__(self):
		self.root = Tk()
		self.root.title("Toggle GUI")
		self.root.geometry("300x300")

		self.running_label = Label(self.root, text="Not Running", fg="red")
		self.running_label.pack(pady=10)

		self.keys = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

		self.select_key_label = Label(self.root, text="Select Key")
		self.select_key_label.pack(pady=10)

		self.cmb = ttk.Combobox(self.root, values=self.keys)		
		self.cmb.pack(pady=10)

		self.toggle_button = Button(self.root, text="Start Toggle", command=self.start_toggle)
		self.toggle_button.pack(pady=10)

		self.stop_button = Button(self.root, text="Stop Toggle", command=self.stop_toggle)
		self.stop_button.pack(pady=10)
		self.stop_button.config(state=DISABLED)

		self.toggle = tg.toggle()
		self.listener = None

		self.root.mainloop()

	def start_toggle(self):
		self.running_label.config(text="Running", fg="green")
		self.toggle_button.config(state=DISABLED)
		self.stop_button.config(state=NORMAL)
		self.toggle.start_toggle()

	def stop_toggle(self):
		self.running_label.config(text="Not Running", fg="red")
		self.toggle_button.config(state=NORMAL)
		self.stop_button.config(state=DISABLED)
		self.toggle.stop_toggle()
		if self.listener:
			self.listener.stop()
			self.listener.join()
			self.listener = None

	def on_press(self, key):
		self.toggle.on_press(key)

if __name__ == "__main__":
	ToggleApp()
