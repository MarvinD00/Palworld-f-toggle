from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
import toggle as tg

class ToggleApp:

	def __init__(self):
		self.root = Tk()
		self.root.title("Toggle GUI")
		self.root.geometry("300x200")

		self.label_frame = Frame(self.root)
		self.label_frame.pack()

		self.entry_frame = Frame(self.root)
		self.entry_frame.pack()

		self.button_frame = Frame(self.root)
		self.button_frame.pack()

		self.mode = "Start key"

		self.toggle = tg.toggle()

		self.start_key_label = Label(self.label_frame, text="Select start key")
		self.start_key_label.pack(padx=10, pady=10, side=LEFT)

		self.stop_key_label = Label(self.label_frame, text="Select stop key")
		self.stop_key_label.pack(padx=10, pady=10, side=LEFT)

		self.start_key_btn = Button(self.entry_frame, width=10, command=lambda: self.on_set_key(mode="Start key"), text="Set start key")
		self.start_key_btn.pack(padx=15, pady=10, side=LEFT)

		self.stop_key_btn = Button(self.entry_frame, width=10, command=lambda: self.on_set_key(mode="Stop key"), text="Set stop key")
		self.stop_key_btn.pack(padx=15, pady=10, side=LEFT)

		self.toggle_button = Button(self.button_frame, text="Start Toggle", command=self.start_toggle)
		self.toggle_button.pack(padx=10, pady=10, side=LEFT)

		self.stop_button = Button(self.button_frame, text="Stop Toggle", command=self.stop_toggle, state=DISABLED)
		self.stop_button.pack(padx=10, pady=10, side=LEFT)

		self.running_label = Label(self.root, text="Not Running", fg="red")
		self.running_label.pack(pady=10)
		
		self.listener = None


		self.root.mainloop()

	def on_set_key(self, mode):
		showinfo(self.mode, "The next key you press will be the " + self.mode)
		if mode == "Start key":
			self.start_key_label.config(text="Start Key: " + self.toggle.set_key(start=True))
		if mode == "Stop key":
			self.stop_key_label.config(text="Stop Key: " + self.toggle.set_key(start=False))

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
