

class backend:


	def __init__(self):
		self.wood = [0,0,0,0,0,0,0]
		self.brick = [0,0,0,0,0,0,0]
		self.leather = [0,0,0,0,0,0,0]
		self.metal = [0,0,0,0,0,0,0]
		self.cloth = [0,0,0,0,0,0,0]
		
	
	def calc(self, matlist):
		multable = {
			2: 1,
			3: 2,
			4: 2,
			5: 3,
			6: 4,
			7: 5,
			8: 5
		}
		result = matlist[:]
		#1 vorheriges Endprodukt wird benötigt
		for i in range(6,0,-1):
			result[i-1] += result[i]
			
		for i in range(7):
			result[i] = result[i]*multable[i+2]
			
		return result
		
	def chwood(self, tier, dekr):
		if(dekr):
			self.wood[tier] -= 1
		else:
			self.wood[tier] += 1
		return self.wood[tier]
		
	def chbrick(self, tier, dekr):
		if(dekr):
			self.brick[tier] -= 1
		else:
			self.brick[tier] += 1
		return self.brick[tier]

	def chleather(self, tier, dekr):
		if(dekr):
			self.leather[tier] -= 1
		else:
			self.leather[tier] += 1
		return self.leather[tier]
		
	def chmetal(self, tier, dekr):
		if(dekr):
			self.metal[tier] -= 1
		else:
			self.metal[tier] += 1
		return self.metal[tier]
		
	def chcloth(self, tier, dekr):
		if(dekr):
			self.cloth[tier] -= 1
		else:
			self.cloth[tier] += 1
		return self.cloth[tier]
		
		
	def addmat(self, tier, mat, btnref):
		tier = tier - 2 #correct to 0-Index
		"""switcher = {
			"wood": chwood,
			"brick": chbrick,
			"leather": chleather,
			"metal": chmetal,
			"cloth": chcloth
		}
		caller = switcher.get(mat, "ERR")
		caller(tier)"""
		if(mat == "wood"):
			btnref["text"] = self.chwood(tier,False)
		elif(mat == "brick"):
			btnref["text"] = self.chbrick(tier,False)
		elif(mat == "leather"):
			btnref["text"] = self.chleather(tier,False)
		elif(mat == "metal"):
			btnref["text"] = self.chmetal(tier,False)
		elif(mat == "cloth"):
			btnref["text"] = self.chcloth(tier,False)
		
		
	
	def submat(self, tier, mat, btnref):
		tier = tier - 2
		if(mat == "wood"):
			btnref["text"] = self.chwood(tier,True)
		elif(mat == "brick"):
			btnref["text"] = self.chbrick(tier,True)
		elif(mat == "leather"):
			btnref["text"] = self.chleather(tier,True)
		elif(mat == "metal"):
			btnref["text"] = self.chmetal(tier,True)
		elif(mat == "cloth"):
			btnref["text"] = self.chcloth(tier,True)
