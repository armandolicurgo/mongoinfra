def getfile(file):
	t = "EEERRROOORRR"
	try:
		f = open(file,"r")
		t = f.read()	
		f.close()
	except:
		pass
	return t


	

programs=getfile("files.txt").split("\n")
for filename in programs:
	if filename.find(".pyc") == -1 and filename.find(".py") != -1:
		program = getfile("."+filename)
		print("=" * 78)
		print(filename)
		for line in program.split("\n"):
			if line.find("def ") > -1:
				print(line)

