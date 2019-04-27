from tkinter import *


mats = {
	0: "wood",
	1: "brick",
	2: "leather",
	3: "metal",
	4: "cloth"
}

tiers = ["T2", "T3", "T4", "T5", "T6", "T7", "T8"]

class GUI:

		
	def __init__(self, root, backend):
		self.backend = backend
		self.buttons = []
		
		#Frame um die Eingabeanordnung zusammenzufassen
		self.intab = Frame(root)
		self.intab.grid(row=0, column=0, sticky=NW)
		
		#Frame für control buttons
		self.cbtns = Frame(self.intab)
		self.cbtns.grid(row=6, column=0, columnspan=8, sticky=NSEW)
		
		#TextBox zur Ausgabe
		self.textfeld = Text(root, height = 12, width = 52, spacing2 = 10)
		self.textfeld.grid(row=0, column=1, sticky=NSEW)
		
		#submit button
		submit = Button(self.cbtns, text="Add & keep", command=self.resolve)
		submit.pack(side=LEFT)
		
		#additem
		newitem = Button(self.cbtns, text="Add & new", command=self.addItem)
		newitem.pack(side=LEFT)
		
		#new button
		new = Button(self.cbtns, text="New", command=self.clearItem)
		new.pack(side=LEFT)
		
		#clear
		clear = Button(self.cbtns, text="Full Clear", command=self.clear)
		clear.pack()
		
		
		#buttonTable labels
		for i in range(7):
			label = Label(self.intab, text=tiers[i])
			label.grid(row=0, column=i+1)
			
		for i in range(5):
			label = Label(self.intab, text=mats[i].capitalize())
			label.grid(row=i+1, stick=W)
		
		for i in range(5):
			self.buttons.append([])
			for j in range(7):
				button = Button(self.intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda row=i, column=j: self.backend.addmat(column, row, self.buttons[row][column]))
				self.buttons[i].append(button)
				self.buttons[i][j].bind("<Button-3>", lambda a, row=i, column=j: self.backend.submat(column, row, self.buttons[row][column]))
				self.buttons[i][j].grid(row=i+1,column=j+1, sticky=NSEW)		
				
		#self.resolve()
	
	#/init
		
	def resolve(self):
		self.textfeld.delete(1.0, END)
		item = self.backend.addItem()
		for x in tiers:
			self.textfeld.insert(END, x + "\t")
		for i in item:
			for x in i:
				self.textfeld.insert(END, x)
				self.textfeld.insert(END, "\t")
			
	#full-clear
	def clear(self):
		self.textfeld.delete(1.0, END)
		self.backend.__init__()		
		self.btnrenew()
		
	#nur aktuelle eingabe
	def clearItem(self):
		self.backend.clearItem()
		self.btnrenew()
		
	def addItem(self):
		self.resolve()
		self.backend.clearItem()
		self.btnrenew()
		
	def btnrenew(self):
		for mat in range(5):
			for tier in range(7):
				val = self.backend.item[mat][tier]
				self.buttons[mat][tier].configure(text=val)
			