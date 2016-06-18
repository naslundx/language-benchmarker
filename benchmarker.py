import time
import subprocess
import json
import subprocess
import os
import argparse
import sys

FNULL = open(os.devnull, 'w')
languages = ["c", "cpp", "python2", "python3", "ooc", "rust", "go", "java", "erlang", "haskell", "js", "csharp", "lua", "ruby", "perl"] 
items = ["helloworld", "primes", "densematrix", "binarytree"]  # TODO read from config file


# Call clean on all items
def cleanup():
	for language in languages:
		config_data = open(language + '/config.json')
		config = json.load(config_data)
		config_data.close()

		for item in items:
			try:
				item_data = config[item]
				clean_cmd = item_data['clean']
				if clean_cmd != "":
					print("   > " + language + ": " + clean_cmd)
					subprocess.call(clean_cmd.split(' '), cwd=language+'/', stdout=FNULL, stderr=FNULL)
			except:
				None


# Run all items in all languages
def benchmark(iterations=3, build_only=True):
	my_env = os.environ.copy()
	my_env["GOPATH"] = os.getcwd()+'/go'

	results = []
	for language in languages:
		print("\n===\nRunning: " + language)
		language_results = []
		config_data = open(language + '/config.json')
		config = json.load(config_data)
		config_data.close()

		for item in items:
			print(" * " + item)
			try:
				item_data = config[item]
				print(item_data)
				build_cmd = item_data['build']
				run_cmd = item_data['run']
			except:
				print("   Not implemented.")
				language_results.append(float('nan'))
				continue

			try:
				print("   > "+build_cmd)
				if build_cmd != "":
					build_result = subprocess.call(build_cmd.split(' '), cwd=language+'/', env=my_env, stdout=FNULL, stderr=FNULL)
				else:
					build_result = 0
			except:
				build_result = 1
				print("   Compilation failed.")
				language_results.append(float('nan'))
				continue

			if build_only == False:
				if build_result == 0:
					print("   > "+run_cmd)
					times = []
					for it in range(0, iterations):
						try:
							start = time.time()
							run_result = subprocess.call(run_cmd.split(' '), cwd=language+'/', env=my_env, stdout=FNULL, stderr=FNULL)
							end = time.time()
							if run_result == 0:
								times.append(end - start)
							else:
								print("   Running failed.")
						except:
							print("   Running failed.")

					if len(times) > 0:
						average = sum(times) / len(times)
					else:
						average = float('nan')
					language_results.append(average) # TODO also save min and max times
					print("   Average time: " + str(round(average, 4)) + " s")

		results.append(language_results)

	return results


# Print brief summary to console
def print_to_console(results):
	languageMaxCharacter = len(max(languages, key = len))
	formattedResults = list(results)
	columnMaxes = [len(next) for next in items]
	for idx, row in enumerate(formattedResults):
		formattedResults[idx] = ["{:.3f}".format(col) + " s" for col in row]
		for jdx, (m, r) in enumerate(zip(columnMaxes, formattedResults[idx])):
			if m < len(r):
				columnMaxes[jdx] = len(r)
	
	columnGap = "    "
	firstPart = "\n" + (languageMaxCharacter + 3) * " "
	theRest = columnGap.join( ("{:^" + str(columnMaxes[colidx]) + "}").format(title) for colidx, title in enumerate(items) )
	print(firstPart + theRest)
	for idx, language in enumerate(languages):
		firstPart = language.rjust(languageMaxCharacter) + " : " 
		theRest = columnGap.join( ( "{:>" + str(columnMaxes[colidx]) + "}").format(res) for colidx, res in enumerate(formattedResults[idx]) )
		print(firstPart + theRest)


# Generate a summary to a text file
def save_to_file(results):
	outPipe = sys.stdout
	sys.stdout = open("results.txt", "w")
	print_to_console(results)
	sys.stdout = outPipe


# Generate a nice table output to file
def save_to_html(results):
	html = '<html><body><table style="text-align:right">'
	heading = "<th></th>" + "".join([ '<th style="font-style:bold;text-align:center;padding:5px 20px;">' + next + "</th>" for next in items])
	html += "<tr>" + heading + "</tr>"
	for i in range(len(languages)):
		row = "<td>" + languages[i] +  "</td>" + "".join(['<td style="padding:5px 20px;">' + "{:.3f}".format(next) + " s" + "</td>" for next in results[i]])
		html += "<tr>" + row + "</tr>"
	html += "</table></body></html>"
	htmlFile = open("results.html", "w")
	htmlFile.write(html)
	htmlFile.close()


def main():
	parser = argparse.ArgumentParser(description='Benchmarking tool for comparing different programming languages.')
	parser.add_argument("--iterations", action="store", dest="iterations", type=int, default=3, help="Number of iterations")
	parser.add_argument("--include", action="store", dest="include", default="", help="Include (only) languages/items in comma-separated list.")
	parser.add_argument("--exclude", action="store", dest="exclude", default="", help="Exclude languages/items in comma-separated list.")
	parser.add_argument("-c", "--clean", action="store_true", dest="clean", default=False, help="Only run cleanup.")
	parser.add_argument("-b", "--build-only", action="store_true", dest="buildonly", default=False, help="Build, but do not run.")
	parse_results = parser.parse_args()

	cleanup()
	if parse_results.clean == False or parse_results.buildonly == True:
		results = benchmark(parse_results.iterations, parse_results.buildonly)
		if parse_results.buildonly == False:
			print_to_console(results)
			save_to_file(results)
			save_to_html(results)


if __name__ == "__main__":
	main()
