import os, os.path, sys, re

class Document:
	def __init__(self, parm, parmtype="str"):
		'''   parm is either a big string that is the text to store,
		     or it is a filename.  parmtype tells which.
		     if parmtype == 'str' then it is the text.
		     if parmtype == 'filename' then it is the name of a file
		'''
		text = parm      # assume it is "str"
		if parmtype == "filename":
			if os.path.isfile(parm):
				with open(parm) as f:
					text = f.read()
			else:
				print(f"No such file named '{parm}'")
				text = ""
		self.lines = text.split("\n")
		print(f"Number of lines = {len(self.lines)}")

	def size(self):
		return len(self.lines)

	def __str__(self):
		return "\n".join(self.lines)

	def getWords(line, linenum=0):
		'''  This breaks up the text of line 'linenum' into words, and removes punctuation.  
		    It then delivers a list of tuples   (word, linenum).   So for example [("the",0),("cat",0),("in",0),("hat",0)]
		    but suppresses duplicates.  So "the cat in the hat" leaves out the second "the".
		    It uses a regular expression to split on a string of multiple blanks (actually space chars).
		'''
		#print(f"{linenum}:  line={line}")
		words = re.split("\s+",line)
		words = [remPunc(word) for word in words]
		words = list(set(words))
		return [(word,linenum) for word in words]
		
	def getAllWords(self):
		biglist = []
		i = 0
		for line in self.lines:
			biglist += Document.getWords(line,i)
			i += 1
		return biglist
			
def remPunc(word):
	while len(word) > 0:
		ch = word[0].lower()
		if not ('a' <= ch <= 'z'):
			word = word[1:]
		else:
			break
	while len(word) > 0:
		ch = word[-1].lower()
		if not ('a' <= ch <= 'z'):
			word = word[0:-1]
		else:
			break
	return word