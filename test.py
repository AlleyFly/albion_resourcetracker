
import tkinter as tk
import rbutton

def call1():
	print("1 called")

def call2():
	print("2 called")

root = tk.Tk()

rbuttons = {
	"1": call1,
	"2": call2
}

rbuttons = rbutton.rbutton(root, rbuttons)

root.mainloop()
