import time
import subprocess
from benchmarkers import benchmarkerc, benchmarkercpp, benchmarkerpython, benchmarkerooc

# TODO Clean up with main func etc.
# TODO take iterations as argument

# TODO Ability to change compiler?

# TODO Check all compiler, language versions etc. and print+store in log

languages = ["c", "cpp", "python3"] # TODO read from config file
items = ["helloworld"] # TODO read from config file
iterations = 100
results = []

# Run all items in all languages
for language in languages:
	print("Running: " + language)
	current_results = []

	for item in items:
		print("\t" + item)

		if language=="c":
			benchmarker = benchmarkerc(item)
		elif language=="cpp":
			benchmarker = benchmarkercpp(item)
		elif language=="python3":
			benchmarker = benchmarkerpython(item)
		elif language=="ooc":
			benchmarker = benchmarkerooc(item)

		result = benchmarker.prepare()

		if result:
			times = []
			for it in range(0, iterations):
				start = time.time()
				result = benchmarker.execute()
				end = time.time()
				if result:
					times.append(end - start)
				else:
					print("Running failed.")

			average = sum(times) / len(times)
			current_results.append(average)
			print("\tTime: " + str(round(average, 4)) + " s")
		else:
			print("Compilation failed")
			current_results.append(0.0)
	
	results.append(current_results)

# Generate a nice table output to file
# TODO

