from tkinter import *


mats = {
	0: "wood",
	1: "brick",
	2: "leather",
	3: "metal",
	4: "cloth"
}

class GUI:

		
	def __init__(self, root, backend):
		self.backend = backend
		self.buttons = []
		
		#Frame um die Eingabeanordnung zusammenzufassen
		self.intab = Frame(root)
		self.intab.pack(side=LEFT, fill=Y)
		
		#Frame für control buttons
		self.cbtns = Frame(self.intab)
		self.cbtns.grid(row=6, column=0, columnspan=7)
		
		#TextBox zur Ausgabe
		self.textfeld = Text(root, height = 10, width = 25)
		self.textfeld.pack(side=LEFT, fill=BOTH, expand=1)
		
		#submit button
		submit = Button(self.cbtns, text="Submit", command=self.resolve)
		submit.pack(side=LEFT)
		
		#clear button
		clear = Button(self.cbtns, text="Clear", command=self.clear)
		clear.pack(side=LEFT)
		
		#buttonTable labels
		labelt0 = Label(self.intab, text="Tier")
		labelt2 = Label(self.intab, text="T2")
		labelt3 = Label(self.intab, text="T3")
		labelt4 = Label(self.intab, text="T4")
		labelt5 = Label(self.intab, text="T5")
		labelt6 = Label(self.intab, text="T6")
		labelt7 = Label(self.intab, text="T7")
		labelt8 = Label(self.intab, text="T8")
		
		labelt0.grid(row=0, column=0)
		labelt2.grid(row=0, column=1)
		labelt3.grid(row=0, column=2)
		labelt4.grid(row=0, column=3)
		labelt5.grid(row=0, column=4)
		labelt6.grid(row=0, column=5)
		labelt7.grid(row=0, column=6)
		labelt8.grid(row=0, column=7)
		
		labelWood = Label(self.intab, text="Wood")
		labelBrick = Label(self.intab, text="Brick")
		labelLeather = Label(self.intab, text="Leather")
		labelMetal = Label(self.intab, text="Metal")
		labelCloth = Label(self.intab, text="Cloth")

		labelWood.grid(row=1, sticky=NSEW)
		labelBrick.grid(row=2, sticky=NSEW)
		labelLeather.grid(row=3, sticky=NSEW)
		labelMetal.grid(row=4, sticky=NSEW)
		labelCloth.grid(row=5, sticky=NSEW)
		
		for i in range(5):
			self.buttons.append([])
			for j in range(7):
				button = Button(self.intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda row=i, column=j: self.backend.addmat(column+2, mats[row], self.buttons[row][column]))
				self.buttons[i].append(button)
				self.buttons[i][j].bind("<Button-3>", lambda a, row=i, column=j: self.backend.submat(column+2, mats[row], self.buttons[row][column]))
				self.buttons[i][j].grid(row=i+1,column=j+1)		
	
	#/init
	
	def resolve(self):
		self.textfeld.delete(1.0, END)
		rwood = self.backend.calc(self.backend.wood)
		rbrick = self.backend.calc(self.backend.brick)
		rleather = self.backend.calc(self.backend.leather)
		rmetal = self.backend.calc(self.backend.metal)
		rcloth = self.backend.calc(self.backend.cloth)
		
		self.textfeld.insert(END, ["T2", "T3","T4","T5","T6","T7","T8"])
		self.textfeld.insert(END, "\n")
		self.textfeld.insert(END, rwood)
		self.textfeld.insert(END, "\n")
		self.textfeld.insert(END, rbrick)
		self.textfeld.insert(END, "\n")
		self.textfeld.insert(END, rleather)
		self.textfeld.insert(END, "\n")
		self.textfeld.insert(END, rmetal)
		self.textfeld.insert(END, "\n")
		self.textfeld.insert(END, rcloth)
		self.textfeld.insert(END, "\n")
		
	def clear(self):
		self.textfeld.delete(1.0, END)
		self.backend.__init__()		
		self.btnrenew()
		
	def btnrenew(self):
		for i in range(5):
			for j in range(7):
				val = self.backend.getElement(i,j)
				self.buttons[i][j].configure(text=val)
			