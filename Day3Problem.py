def moveCheck(move):
	if move == ">":
		val = (0,1)
	elif move == "<":
		val = (0,-1)
	elif move == "^":
		val = (1,1)
	else:
		val = (1,-1)
	return val

def checkInSet(tup,homes,numHomes):
	if tup not in homes: 
		homes.add(tup)
		numHomes += 1
	return homes,numHomes

def numHousesReceiveAtLOnePresent(string,numSantas): #Generalizing the Santa(s) problem for any given number of Santas, given that number is a divisor of the total number of moves.
	if(len(string) % numSantas != 0): 
		raise ValueError("Every Santa must get the same number of moves.")
	point = [[0,0] for k in range(numSantas)]
	homes = set(tuple([0,0]) for k in range(numSantas))
	numHomes = 1
	move = [[0,0] for k in range(numSantas)]
	for i in range(0,len(string),numSantas):
		for j in range(numSantas): 
			move[j] = moveCheck(string[i + j])
			point[j][move[j][0]] += move[j][1]
			homes,numHomes = checkInSet(tuple(point[j]),homes,numHomes)
	return numHomes

with open("Day3Text.txt",'r') as file:
	string = file.read()
	for k in range(1,3):
		print(numHousesReceiveAtLOnePresent(string,k))