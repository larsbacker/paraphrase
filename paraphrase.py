#!/usr/bin/python
#Lars Backer
#26-06-2015

import sys

def main(argv):
	dictionary = {}
	for line in open(argv[1],"r") :
		if line[1] == "N" and line[2] == "N" and line[3] == "P" or line[3] == "]" and line[4] == "]":
			line = line.split("|||")
			# line[1] = first word
			# line[2] = paraphrase of first word
			dictionary.update({line[1]:line[2]})
				
	sens = argv[2]
	senssplit = sens.split()
	for word in senssplit:
		keyword = " " + word + " "
		if keyword in dictionary.keys():
			position = [i for i,x in enumerate(senssplit) if x == word]
			senssplit.remove(word)
			senssplit.insert(position[0],dictionary[keyword])
	
	print(" ".join(senssplit))
			
	
	
if __name__ == "__main__":
	main(sys.argv)
	

