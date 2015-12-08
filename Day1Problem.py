from re import *

def floorDisplacement(string):
	disp = 0
	while string.find("()") != -1:
		string = string.replace("()","")
	while string.find(")(") != -1:
		string = string.replace(")(","")
	return len(string) if string[0] == "(" else -len(string)

def firstPosToBasement(string):
	floor = 0
	pos = 0
	length = len(string)
	while(floor != -1 and pos != length):
		char = string[pos]
		if(char == "("):
			floor += 1
		else:
			floor -= 1
		pos += 1
	return pos

with open("Day1Text.txt",'r') as file:
	string = file.read()
	print(floorDisplacement(string))
	print(firstPosToBasement(string))