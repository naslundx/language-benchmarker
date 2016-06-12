import time
import subprocess
from benchmarkers import benchmarkerc, benchmarkercpp
from benchmarkers import benchmarkerpython, benchmarkerooc

# TODO Ability to change compiler?

# TODO Check all compiler, language versions etc. and print+store in log

languages = ["c", "cpp", "py3", "ooc"]  # TODO read from config file
items = ["helloworld", "primes"]  # TODO read from config file
iterations = 10


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

				if len(times) > 0:
					average = sum(times) / len(times)
				else:
					average = 0.0
				current_results.append(average) # TODO also save min and max times
				print("\tTime: " + str(round(average, 4)) + " s")
			else:
				print("Compilation failed")
				current_results.append(0.0)

		results.append(current_results)

	return results


# Generate a nice table output to file
def save_to_file(results):
	print("\n\t" + "\t".join(items))
	for i in range(0, len(languages)):
		print(languages[i] + ":\t" + "\t".join(str(round(x, 3))+"s" for x in results[i])) # TODO needs better formatting
	# TODO save to nice format file
	None


def main():
	results = benchmark()
	save_to_file(results)


if __name__ == "__main__":
	main()
