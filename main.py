from tkinter import *
from gui import *
from backend import *


root = Tk()
backend = backend()
gui = GUI(root, backend)



root.mainloop()