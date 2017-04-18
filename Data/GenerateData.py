import sys, math, operator
from random import randint
from collections import Counter

def main(argv):
	#print("\nGenerating Random Data...")

	generatedString = ""
	motif = ["AACGCTTGCACCTTATTCGA","ACCGCGCCTGATTTGCGAA"]
	#motif = ["---","___"]
	finalString = ""
	#print("\nLooking for motifs: " + str(motif) + "\n")
	addedLocations = []
	currentLine = ""
	count = 0
	while len(generatedString) <= 1000000:

		currentRandom = randint(0,12)
		if currentRandom == 0 or currentRandom == 1 or currentRandom == 2:
			generatedString += "A"
			#index+=1

		if currentRandom == 3 or currentRandom == 4 or currentRandom == 5:
			generatedString += "C"
			#index+=1

		if currentRandom == 6 or currentRandom == 7 or currentRandom == 8:
			generatedString += "G"
			#index+=1

		if currentRandom == 9 or currentRandom == 10 or currentRandom == 11:
			generatedString += "T"
			#index+=1

		if currentRandom == 12:
			currentRandom2 = randint(0,200)
			if currentRandom2 == 5:
				motifToAdd = motif[randint(0,1)]
				generatedString += motifToAdd
				count += 1
			#addedLocations.append(index)
			#index+=len(motifToAdd)	
	
	#print(addedLocations)

	for character in generatedString:
		currentRandom = randint(0,1000)
		if currentRandom == 12:
			finalString+=motif[randint(0,1)]
			count+=1
			#addedLocations.append(currentRandom)
		finalString+=character

	#For every insert, I increased a counter. This will let us know at least how many motifs we should find. Depending
	#on how the motifs are split, we may have less or more.
	#print("We should have around " + str(count) + " motifs (at least).\n")
	#print(finalString + "\n")


	#Here, we seperate the entire string into smaller parts, in order to evaluate them. Some motifs will be cut off,
	#but this is on purpose, and is an edge case.	
	index = 0
	n = 0
	for character in finalString:
		if index == 160:
			print(">seq_"+n.__str__())
			print(str(currentLine))
			n=n+1
			index = 0
			currentLine=""
		else:
			currentLine+=character
			index+=1
	


if __name__ == "__main__":
    main(sys.argv[0:])