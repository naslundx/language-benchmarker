import time
import subprocess
from benchmarkers import benchmarkerc, benchmarkercpp, benchmarkerpython, benchmarkerooc

# TODO Clean up with main func etc.
# TODO take iterations as argument

# TODO Ability to change compiler?

# TODO Check all compiler, language versions etc. and print+store in log

# Get languages
languages = ["c", "cpp", "python3", "ooc"] # TODO read from config file
suffixes = ["c", "cpp", "py", "ooc"]

for i in range(0, len(languages)):
	language = languages[i]
	item = "helloworld" # TODO get all items and process in order
	suffix = suffixes[i] # TODO read from config file
	filename = item + "." + suffix
	binpath = language + "/bin/"
	srcpath = language + "/"

	if language=="c":
		benchmarker = benchmarkerc(binpath, srcpath, item, suffix)
	elif language=="cpp":
		benchmarker = benchmarkercpp(binpath, srcpath, item, suffix)
	elif language=="python3":
		benchmarker = benchmarkerpython(binpath, srcpath, item, suffix)
	elif language=="ooc":
		benchmarker = benchmarkerooc(binpath, srcpath, item, suffix)

	result = benchmarker.prepare()

	if result:
		start = time.time()
		result = benchmarker.execute()
		end = time.time()
		if result:
			print(end - start)
		else:
			print("Running failed.")
	else:
		print("Compilation failed")

# TODO store all results, generate a nice table output
