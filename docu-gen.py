def main():
	# Put the file in memory
	f = open("hello.txt", "r")
	# Do all the shit I want to do with the file
	content = f.read()
	# Take the file out of memory
	f.close()

	name = raw_input("What is your name? :")
	save_name = raw_input("Name your output file :")
	greeting = "Hola"

	content = content.replace("[NAME]", name)
	content = content.replace("[GREETING]", greeting)
	print(content)

	output = open(save_name + ".txt", "w+")
	output.write(content)
	output.close()


if __name__ == '__main__':
	main()
