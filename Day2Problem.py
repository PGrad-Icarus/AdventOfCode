from re import *
from itertools import combinations
def totalWrappingPaper(string):
	return sum([2 * sum(a) + min(a) for a in [[b * c for b,c in combinations([int(d) for d in split("x",e)],2)] for e in split("\n",string)]])
def totalRibbon(string):
	return sum([a * b * c + 2 * (a + b + c - max(a,b,c)) for a,b,c in [list([int(d) for d in split("x",e)]) for e in split("\n",string)]])
with open("Day2Text.txt","r") as file:
	string = file.read()
	print(totalWrappingPaper(string))
	print(totalRibbon(string))