from tkinter import *
from gui_list import *
from backend import *


root = Tk()
backend = backend()
gui = GUI(root, backend)



root.mainloop()