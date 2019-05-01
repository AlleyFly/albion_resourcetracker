
import operator
import math

#kosten um resourcen aus niedrigerem tier herzustellen


#berechnung der verbleibenden noetigen Materialien um alle maxtier-Mats zu verarbeiten
def remainingGather(matlist):
	tmax = maxtier(matlist)
	amount = matlist[tmax-2]/multable[tmax]
	needed = [math.ceil(amount*multable[i+2]) for i in range(tmax-2)]
	needed.append(matlist[tmax-2]) #-amount vermeiden
	
	for i in range(tmax, 8): #mit 0 auf richtige laenge padden
		needed.append(0)

	#listen verechnen
	result = map(operator.sub, needed, matlist)
	return result


def maxtier(matlist):
	counter = 8
	for x in matlist[::-1]:
		if(x != 0):
			return counter
		counter -= 1
	return 2

#berechnung ohne tradeup
def calcMax(matlist):
	pass
