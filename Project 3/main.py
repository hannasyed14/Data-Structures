import document

import hashmap

filename = "FILES/treasure island.txt"
#filename = "FILES/getty.txt"
#filename = "FILES/moby dick.txt"
book = document.Document(filename, "filename")

print(f"Now analyzing {filename}")

words = book.getAllWords()

numwords = len(words)
print(f"{numwords} words total (unique in each line)")

wordhash = hashmap.HashMap(100)

for word in words:
	wordhash.setAppend(word[0], word[1])

wordhash.stats()

response = input("Do you want to display the hashmap? (y/n)")
if response == "y":
	wordhash.display()

keys = wordhash.getKeys()

response = input("Do you want to display the concordance? (y/n)")
if response == "y":
	for key in keys:
		print(f"{key:20s}   {wordhash.get(key)}")

response = input("Do you want to see the frequencies? (y/n)")
if response == "y":
	print("Frequencies...")
	for key in keys:
		pagenumbers = wordhash.get(key)
		print(f"{key:30s}   {len(pagenumbers.split(',')):4d}")


