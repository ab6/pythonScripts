import re
import argparse
import nltk.data

def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)

parser = argparse.ArgumentParser(description='Break batch file up into individual reports.')
parser.add_argument('inputFile', help='Batch file path.')
parser.add_argument('savePath', help='Path to folder for storing files')
args = parser.parse_args()
inputFile = args.inputFile
savePath = args.savePath

b = re.compile(r"\d+\.\d+")

batch = open(inputFile, 'r')
case = ""
currentFile = None
recordTop = True
next = batch.readline()

while next:
	line = strip_non_ascii(next).strip()
	if line is not "":
		print(line.replace('\W+', ' '))
		#At first line in page
		if re.search("Case #", line):
			m = re.search("Case #", line)
			start = line[m.start():]
			#New case
			if cmp(re.findall(b, start)[0], case) is not 0:
				case = re.findall(b, start)[0]
				if currentFile:
					currentFile.close()
		#At top of record
		elif re.search("Tennessee Department of Children's Services", line):
			recordTop = True
		elif recordTop is True:
			if re.search("Hotline", line):
				currentFile = open(savePath + "/CAHS-" + case + ".txt", 'w')
			if re.search("Investigation", line):
				currentFile = open(savePath + "/CPSIS-" + case + ".txt", 'w')
			if re.search("Recording", line):
				currentFile = open(savePath + "/CRS-" + case + ".txt", 'w')
			if re.search("TM", line):
				currentFile = open(savePath + "/SA-" + case + ".txt", 'w')
			if re.search("Fatality", line):
				currentFile = open(savePath + "/NCF-" + case + ".txt", 'w')
			recordTop = False
		else:
			if not re.search("= Page", line):
				currentFile.write(line.replace('\W+', ' '))
	next = batch.readline()


batch.close()
