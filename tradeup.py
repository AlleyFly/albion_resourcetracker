
import operator
#kosten um resourcen aus niedrigerem tier herzustellen
cost = {
	3: 3,
	4: 6,
	5: 9,
	6: 15,
	7: 25,
	8: 42
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

#berechnung der verbleibenden noetigen Materialien um alle maxtier-Mats zu verarbeiten
def remainingGather(matlist):
	tmax = maxtier(matlist)-2 #listindex des maxtiers = tatsaechliches maxtier-2
	amount = matlist[tmax]/multable[tmax+2]
	needed = [amount*multable[i+2] for i in range(tmax)]

	needed.append(matlist[tmax]) #-amount vermeiden
	for i in range(tmax+1, 7): #mit 0 auf richtige laenge padden
		print(i+2)
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
	return 1

#berechnung ohne tradeup
def calcMax(matlist):
	pass
