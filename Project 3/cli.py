import hashmap
import traceback

def help():
	print("q                quit")
	print("+KEY=VALUE       add a KEY,VALUE pair or change VALUE")
	print("?KEY             find the value associated with the KEY")
	print("-KEY             delete KEY,VALUE pair")
	print("samples          populate with sample data")
	print("hash STRING      show the hash value of the string STRING")
	print("p                print everything")

def makeSamples(map):
	map.set("Robert", "378943")
	map.set("Katerina", "secret")
	map.set("Ronda", "weird")
	map.set("Alvin", "geheimnis")

def main():
	map = hashmap.HashMap(10)
	while True:
		try:
			response = input("Enter command: ")
			if response == "q": break
			if response == "help":
				help()
			elif response == "p":
				map.display()
			elif response[0] == "+":
				key,value = response[1:].split("=")
				map.set(key,value)
			elif response[0] == "-":
				key = response[1:]
				map.delete(key)
			elif response[0] == "?":
				key = response[1:]
				print(map.get(key))
			elif response.startswith("hash "):
				print(map.hashme(response[5:]))
			elif response == "samples":
				makeSamples(map)
			else:
				print("Unknown command")
		except Exception as e:
			tb = traceback.format_exc()
			print("Caught a run-time error and recovered from it.")
			print(e.__class__.__name__, end=", ")
			print(e)
			print(tb)

main()