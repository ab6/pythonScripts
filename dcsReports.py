import re
import argparse
import nltk.data



parser = argparse.ArgumentParser(description='Break batch file up into individual reports.')
parser.add_argument('inputFile', help='Batch file path.')
parser.add_argument('savePath', help='Path to folder for storing files')
args = parser.parse_args()
inputFile = args.inputFile
savePath = args.savePath

batch = open(inputFile, 'r')
case = ""
currentFile = None
recordTop = True
next = batch.readline()

while next:
	line = next.strip()
	print(line.replace('\W+', ' '))
	if line is not "":
		#At first line in page
		if re.search("Case #", line):
			print("in case")
			#New case
			if cmp(line, case) is not 0:
				case = line.strip()
				if currentFile:
					currentFile.close()
		#At top of record
		elif re.search("Tennessee Department of Children's Services", line):
			recordTop = True
		elif recordTop is True:
			if re.search("Hotline", line):
				currentFile = open(savePath + "/CAHS-" + case[6:] + ".txt", 'w')
			if re.search("Investigation", line):
				currentFile = open(savePath + "/CPSIS-" + case[6:] + ".txt", 'w')
			if re.search("Recording", line):
				currentFile = open(savePath + "/CRS-" + case[6:] + ".txt", 'w')
			if re.search("Safety", line):
				currentFile = open(savePath + "/SA-" + case[6:] + ".txt", 'w')
			recordTop = False
		else:
			currentFile.write(line.replace('\W+', ' '))
	next = batch.readline()


batch.close()
