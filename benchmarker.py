import time
import subprocess
from benchmarkers import benchmarkerc, benchmarkercpp
from benchmarkers import benchmarkerpython, benchmarkerooc
from benchmarkers import benchmarkerrust, benchmarkergo
from benchmarkers import benchmarkerjava, benchmarkererlang
from benchmarkers import benchmarkerhaskell, benchmarkerjavascript
from benchmarkers import benchmarkercsharp

# TODO Ability to change compiler?

# TODO Check all compiler, language versions etc. and print+store in log

languages = ["c", "cpp", "py3", "ooc", "rust", "go", "java", "erl", "hskl", "js", "csharp"]  # TODO read from config file
items = ["helloworld", "primes"]  # TODO read from config file
iterations = 2


# Run all items in all languages
def benchmark():
	results = []
	for language in languages:
		print("Running: " + language)
		current_results = []

		for item in items:
			print("\t" + item)

			if language == "c":
				benchmarker = benchmarkerc(item)
			elif language == "cpp":
				benchmarker = benchmarkercpp(item)
			elif language == "py3":
				benchmarker = benchmarkerpython(item)
			elif language == "ooc":
				benchmarker = benchmarkerooc(item)
			elif language == "rust":
				benchmarker = benchmarkerrust(item)
			elif language == "go":
				benchmarker = benchmarkergo(item)
			elif language == "java":
				benchmarker = benchmarkerjava(item)
			elif language == "erl":
				benchmarker = benchmarkererlang(item)
			elif language == "hskl":
				benchmarker = benchmarkerhaskell(item)
			elif language == "js":
				benchmarker = benchmarkerjavascript(item)
			elif language == "csharp":
				benchmarker = benchmarkercsharp(item)
			else:
				print("Unsupported language!")

			try:
				result = benchmarker.prepare()
			except:
				result = 0

			if result:
				times = []
				for it in range(0, iterations):
					try:
						start = time.time()
						result = benchmarker.execute()
						end = time.time()
						if result:
							times.append(end - start)
						else:
							print("\tRunning failed.")
					except:
						print("\tRunning failed.")

				if len(times) > 0:
					average = sum(times) / len(times)
				else:
					average = float('nan')
				current_results.append(average) # TODO also save min and max times
				print("\tTime: " + str(round(average, 4)) + " s")
			else:
				print("\tCompilation failed")
				current_results.append(float('nan'))

		results.append(current_results)

	return results


# Generate a nice table output to file
def save_to_file(results):
	print("\n\t" + "\t".join(items))
	for i in range(0, len(languages)):
		print(languages[i] + ":\t" + "\t\t".join(str(round(x, 3))+"s" for x in results[i])) # TODO needs better formatting
	# TODO save to nice format file
	None


def main():
	results = benchmark()
	save_to_file(results)


if __name__ == "__main__":
	main()
