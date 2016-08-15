import sys
import operator

TRUE = 1
FALSE = 0

def analyzeText(text):
	wordCounts = {}
	words = text.split()
	for word in words:
		word = str(word)
		lastLetter = word[len(word) - 1]
		firstLetter = word[0]
		ignoreChars = [",", ":", ";", "'", '"', "-"]
		if (lastLetter in ignoreChars):
			word = word[:len(word)]
		if (firstLetter in ignoreChars and len(word) > 1):
			word = word[1:]
		
		if (word != ""):
			if (word in wordCounts):
				wordCounts[word] += 1
			else:
				wordCounts[word] = 1
			
	sum = 0
	for key in wordCounts:
		sum += wordCounts[key]
	return {
		"number of unique words": len(wordCounts),
		"total number of words": sum,
		"data": wordCounts
	}
	print(str(wordCounts))

def printUsage():
	print("Count the number of words in a file")
	print("Arguments: ")
	print("\t-i or --input: the file to read and count words from")
	print("\t-o or --output: a file to output statistics to")
	print("\t-h or --help: print this message")

if __name__ == "__main__":

	inputFlag = FALSE
	outputFlag = FALSE
	inFile = None
	outFile = None
	
	for arg in sys.argv:
		if (inputFlag):
			inFile = arg
			inputFlag = FALSE
		if (outputFlag):
			outFile = open(arg, 'w')
			outputFlag = FALSE
		elif (arg == "-i" or arg == "--input"):
			inputFlag = TRUE
		elif (arg == "-o" or arg == "--output"):
			outputFlag = TRUE
		elif (arg == "-h" or arg == "--help"):
			printUsage()
			sys.exit()
	
	text = ""
	if (inFile == None):
		# Use command line input
		
		while TRUE:
			newLine = input(">>>")
			text += newLine
			if (newLine == ""):
				break
			else:
				text += "\n"
				
		print(analyzeText(text))
		
	else:
		if inFile[-4:] == ".doc" or inFile[-5:] == ".docx":
			# Parse as a doc file
			pass
		else:
			inFile = open(inFile, 'r')
			text += inFile.read()
	
	information = analyzeText(text)
	
	for key in information:
		if key == 'data':
			if (outFile):
				outFile.write("word counts:\n")
				for word in information[key]:
					outFile.write(str(word) + ": " + str(information[key][word]) + "\n")
		else:
			print(str(key) + ": " + str(information[key]))