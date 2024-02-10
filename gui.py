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
		self.toggle = tg.toggle()

		self.select_key_label = Label(self.root, text="Select Key")
		self.select_key_label.pack(pady=10)

		self.key_entry = Entry(self.root, width=20)
		self.key_entry.pack(pady=10)

		self.key_entry.bind("<FocusIn>", self.on_focus_in) 
		self.key_entry.bind("<FocusOut>", self.on_focus_out)

		self.toggle_button = Button(self.root, text="Start Toggle", command=self.start_toggle)
		self.toggle_button.pack(pady=10)

		self.stop_button = Button(self.root, text="Stop Toggle", command=self.stop_toggle)
		self.stop_button.pack(pady=10)
		self.stop_button.config(state=DISABLED)

		self.listener = None

		self.root.mainloop()

	def on_focus_in(self, event):
		self.toggle.set_start_key()

	def on_focus_out(self, event):
		self.toggle.set_stop_key()

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
