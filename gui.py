from tkinter import *
woodc = "burlywood"
brickc = "red"
leatherc = "black"
metalc = "silver"
clothc = "beige"


class GUI:

	
	def resolve(self):
		self.textfeld.delete(1.0, END)
		rwood = self.backend.calc(self.backend.wood)
		rbrick = self.backend.calc(self.backend.brick)
		rleather = self.backend.calc(self.backend.leather)
		rmetal = self.backend.calc(self.backend.metal)
		rcloth = self.backend.calc(self.backend.cloth)
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

	
	def __init__(self, root, backend):
		self.backend = backend
		
		#Frame um die Eingabeanordnung zusammenzufassen
		intab = Frame(root)
		intab.pack(side=LEFT, fill=Y)
		
		#TextBox zur Ausgabe
		self.textfeld = Text(root, height = 10, width = 25)
		self.textfeld.pack(side=LEFT, fill=BOTH, expand=1)
		
		#submit button
		submit = Button(intab, text="Submit", command=self.resolve)
		submit.grid(row=0, column=0)
		
		
		#table outline horiz
		labelt2 = Label(intab, text="T2")
		labelt3 = Label(intab, text="T3")
		labelt4 = Label(intab, text="T4")
		labelt5 = Label(intab, text="T5")
		labelt6 = Label(intab, text="T6")
		labelt7 = Label(intab, text="T7")
		labelt8 = Label(intab, text="T8")
		
		labelt2.grid(row=0, column=1)
		labelt3.grid(row=0, column=2)
		labelt4.grid(row=0, column=3)
		labelt5.grid(row=0, column=4)
		labelt6.grid(row=0, column=5)
		labelt7.grid(row=0, column=6)
		labelt8.grid(row=0, column=7)
		
		#table outline vert
		labelWood = Label(intab, text="Wood", bg=woodc, fg="black")
		labelBrick = Label(intab, text="Brick", bg=brickc, fg="white")
		labelLeather = Label(intab, text="Leather", bg=leatherc, fg="white")
		labelMetal = Label(intab, text="Metal", bg=metalc, fg="black")
		labelCloth = Label(intab, text="Cloth", bg=clothc, fg="black")

		labelWood.grid(row=1, sticky=NSEW)
		labelBrick.grid(row=2, sticky=NSEW)
		labelLeather.grid(row=3, sticky=NSEW)
		labelMetal.grid(row=4, sticky=NSEW)
		labelCloth.grid(row=5, sticky=NSEW)
		
		#Buttons
		#Wood
		t2Wood = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(2, "wood", t2Wood))
		t2Wood.bind("<Button-3>", lambda a: self.backend.submat(2, "wood", t2Wood))
		t2Wood.grid(row=1, column=1)
		
		t3Wood = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(3, "wood", t3Wood))
		t3Wood.bind("<Button-3>", lambda a: self.backend.submat(3, "wood", t3Wood))
		t3Wood.grid(row=1, column=2)
		
		t4Wood = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(4, "wood", t4Wood))
		t4Wood.bind("<Button-3>", lambda a: self.backend.submat(4, "wood", t4Wood))
		t4Wood.grid(row=1, column=3)
		
		t5Wood = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(5, "wood", t5Wood))
		t5Wood.bind("<Button-3>", lambda a: self.backend.submat(5, "wood", t5Wood))
		t5Wood.grid(row=1, column=4)
		
		t6Wood = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(6, "wood", t6Wood))
		t6Wood.bind("<Button-3>", lambda a: self.backend.submat(6, "wood", t6Wood))
		t6Wood.grid(row=1, column=5)
		
		t7Wood = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(7, "wood", t7Wood))
		t7Wood.bind("<Button-3>", lambda a: self.backend.submat(7, "wood", t7Wood))
		t7Wood.grid(row=1, column=6)
		
		t8Wood = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(8, "wood", t8Wood))
		t8Wood.bind("<Button-3>", lambda a: self.backend.submat(8, "wood", t8Wood))
		t8Wood.grid(row=1, column=7)
		
		#Brick
		t2Brick = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(2, "brick", t2Brick))
		t2Brick.bind("<Button-3>", lambda a: self.backend.submat(2, "brick", t2Brick))
		t2Brick.grid(row=2, column=1)
		
		t3Brick = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(3, "brick", t3Brick))
		t3Brick.bind("<Button-3>", lambda a: self.backend.submat(3, "brick", t3Brick))
		t3Brick.grid(row=2, column=2)
		
		t4Brick = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(4, "brick", t4Brick))
		t4Brick.bind("<Button-3>", lambda a: self.backend.submat(4, "brick", t4Brick))
		t4Brick.grid(row=2, column=3)
		
		t5Brick = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(5, "brick", t5Brick))
		t5Brick.bind("<Button-3>", lambda a: self.backend.submat(5, "brick", t5Brick))
		t5Brick.grid(row=2, column=4)
		
		t6Brick = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(6, "brick", t6Brick))
		t6Brick.bind("<Button-3>", lambda a: self.backend.submat(6, "brick", t6Brick))
		t6Brick.grid(row=2, column=5)
		
		t7Brick = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(7, "brick", t7Brick))
		t7Brick.bind("<Button-3>", lambda a: self.backend.submat(7, "brick", t7Brick))
		t7Brick.grid(row=2, column=6)
		
		t8Brick = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(8, "brick", t8Brick))
		t8Brick.bind("<Button-3>", lambda a: self.backend.submat(8, "brick", t8Brick))
		t8Brick.grid(row=2, column=7)
		
		#Leather
		t2Leather = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(2, "leather", t2Leather))
		t2Leather.bind("<Button-3>", lambda a: self.backend.submat(2, "leather", t2Leather))
		t2Leather.grid(row=3, column=1)
		
		t3Leather = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(3, "leather", t3Leather))
		t3Leather.bind("<Button-3>", lambda a: self.backend.submat(3, "leather", t3Leather))
		t3Leather.grid(row=3, column=2)
		
		t4Leather = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(4, "leather", t4Leather))
		t4Leather.bind("<Button-3>", lambda a: self.backend.submat(4, "leather", t4Leather))
		t4Leather.grid(row=3, column=3)
		
		t5Leather = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(5, "leather", t5Leather))
		t5Leather.bind("<Button-3>", lambda a: self.backend.submat(5, "leather", t5Leather))
		t5Leather.grid(row=3, column=4)
		
		t6Leather = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(6, "leather", t6Leather))
		t6Leather.bind("<Button-3>", lambda a: self.backend.submat(6, "leather", t6Leather))
		t6Leather.grid(row=3, column=5)
		
		t7Leather = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(7, "leather", t7Leather))
		t7Leather.bind("<Button-3>", lambda a: self.backend.submat(7, "leather", t7Leather))
		t7Leather.grid(row=3, column=6)
		
		t8Leather = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(8, "leather", t8Leather))
		t8Leather.bind("<Button-3>", lambda a: self.backend.submat(8, "leather", t8Leather))
		t8Leather.grid(row=3, column=7)
		
		#Metal
		t2Metal = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(2, "metal", t2Metal))
		t2Metal.bind("<Button-3>", lambda a: self.backend.submat(2, "metal", t2Metal))
		t2Metal.grid(row=4, column=1)
		
		t3Metal = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(3, "metal", t3Metal))
		t3Metal.bind("<Button-3>", lambda a: self.backend.submat(3, "metal", t3Metal))
		t3Metal.grid(row=4, column=2)
		
		t4Metal = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(4, "metal", t4Metal))
		t4Metal.bind("<Button-3>", lambda a: self.backend.submat(4, "metal", t4Metal))
		t4Metal.grid(row=4, column=3)
		
		t5Metal = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(5, "metal", t5Metal))
		t5Metal.bind("<Button-3>", lambda a: self.backend.submat(5, "metal", t5Metal))
		t5Metal.grid(row=4, column=4)
		
		t6Metal = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(6, "metal", t6Metal))
		t6Metal.bind("<Button-3>", lambda a: self.backend.submat(6, "metal", t6Metal))
		t6Metal.grid(row=4, column=5)
		
		t7Metal = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(7, "metal", t7Metal))
		t7Metal.bind("<Button-3>", lambda a: self.backend.submat(7, "metal", t7Metal))
		t7Metal.grid(row=4, column=6)
		
		t8Metal = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(8, "metal", t8Metal))
		t8Metal.bind("<Button-3>", lambda a: self.backend.submat(8, "metal", t8Metal))
		t8Metal.grid(row=4, column=7)
		
		#Cloth
		t2Cloth = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(2, "cloth", t2Cloth))
		t2Cloth.bind("<Button-3>", lambda a: self.backend.submat(2, "cloth", t2Cloth))
		t2Cloth.grid(row=5, column=1)
		
		t3Cloth = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(3, "cloth", t3Cloth))
		t3Cloth.bind("<Button-3>", lambda a: self.backend.submat(3, "cloth", t3Cloth))
		t3Cloth.grid(row=5, column=2)
		
		t4Cloth = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(4, "cloth", t4Cloth))
		t4Cloth.bind("<Button-3>", lambda a: self.backend.submat(4, "cloth", t4Cloth))
		t4Cloth.grid(row=5, column=3)
		
		t5Cloth = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(5, "cloth", t5Cloth))
		t5Cloth.bind("<Button-3>", lambda a: self.backend.submat(5, "cloth", t5Cloth))
		t5Cloth.grid(row=5, column=4)
		
		t6Cloth = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(6, "cloth", t6Cloth))
		t6Cloth.bind("<Button-3>", lambda a: self.backend.submat(6, "cloth", t6Cloth))
		t6Cloth.grid(row=5, column=5)
		
		t7Cloth = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(7, "cloth", t7Cloth))
		t7Cloth.bind("<Button-3>", lambda a: self.backend.submat(7, "cloth", t7Cloth))
		t7Cloth.grid(row=5, column=6)
		
		t8Cloth = Button(intab, text="0", repeatdelay=100, repeatinterval=10, command= lambda: self.backend.addmat(8, "cloth", t8Cloth))
		t8Cloth.bind("<Button-3>", lambda a: self.backend.submat(8, "cloth", t8Cloth))
		t8Cloth.grid(row=5, column=7)