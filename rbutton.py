from tkinter import Button

class rbutton:

	buttons = [] 
	
	def sink_button(self, event, btnfunc):
		for btn in self.buttons:
			btn.config(relief="raised")
			
		event.widget.config(relief="sunken")
		btnfunc()
		return "break"
		
	def __init__(self, root, btns):
		for btnname,btnfunc in btns.items():
			button = Button(root, text=btnname)
			self.buttons.append(button)
			button.bind("<Button-1>", lambda event, f=btnfunc: self.sink_button(event,f))
			button.pack()
			
	
		
