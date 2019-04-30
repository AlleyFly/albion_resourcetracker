
import numpy
import copy
import tradeup

mats = {
	0: "wood",
	1: "brick",
	2: "leather",
	3: "metal",
	4: "cloth"
}

multable = {
	2: 1,
	3: 2,
	4: 2,
	5: 3,
	6: 4,
	7: 5,
	8: 5
}

class backend:

	#for full-clear
	def __init__(self):
		#leere Materialliste erstellen und 5x in Itemliste kopieren
		emptyMat = [0,0,0,0,0,0,0]
		self.item = [emptyMat[:] for i in mats]
		self.total = copy.deepcopy(self.item)


	#clear current item
	def clearItem(self):
		emptyMat = [0,0,0,0,0,0,0]
		self.item = [emptyMat[:] for i in mats]

	def addItem(self):
		self.total = numpy.add(self.total, self.calc())
		return self.total

	def calc(self):
		result = copy.deepcopy(self.item)

		for matlist in result:
			for i in range(6,0,-1):
				matlist[i-1] += matlist[i]
			for i in range(7):
				matlist[i] = matlist[i]*multable[i+2]
		self.total = result
		return result

	def remaining(self):
		result = []
		for matlist in self.item:
			result.append(tradeup.remainingGather(matlist))
		self.total = result

	def addmat(self, tier, mat, btnref):
		self.item[mat][tier] += 1
		btnref["text"] = self.item[mat][tier]


	def submat(self, tier, mat, btnref):
		self.item[mat][tier] -= 1
		btnref["text"] = self.item[mat][tier]
