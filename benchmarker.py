import time
import json
import subprocess
import os
import argparse
import sys
import math

FNULL = open(os.devnull, 'w')


# Find all languages being used
def get_languages(include_str="", exclude_str=""):
	languages = []
	possible_languages = [x[0] for x in os.walk(os.getcwd()) if not '.' in x[0] or '_' not in x[0]]

	for dir in possible_languages:
		files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
		if 'config.json' in files:
			directory = os.path.split(dir)
			languages.append(directory[1])

	if include_str:
		includes = include_str.split(',')
		if set(languages) & set(includes):  # Only do this if at least one language is in the include string
			result = [language for language in languages if language in includes]
			languages = result

	if exclude_str:
		excludes = exclude_str.split(',')
		result = [language for language in languages if language not in excludes]
		languages = result

	return sorted(languages)


# Find all implementations
def get_items(languages, include_str="", exclude_str=""):
	items = []
	for language in languages:
		config_data = open(language + '/config.json')
		config = json.load(config_data)
		config_data.close()

		for item in config.keys():
			if item not in items:
				items.append(item)

	if include_str:
		includes = include_str.split(',')
		if set(items) & set(includes):  # Only do this if at least one item is in the include string
			result = [item for item in items if item in includes]
			items = result

	if exclude_str:
		excludes = exclude_str.split(',')
		result = [item for item in items if item not in excludes]
		items = result

	return sorted(items)


# Call clean on all items
def cleanup(languages, items):
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


def statistical_analysis(times):
	if len(times) == 0:
		return {'average':float('nan'), 'std_dev':float('nan'), 'minimum':float('nan'), 'maximum':float('nan')}
	
	average = sum(times) / len(times)
	maximum = max(times)
	minimum = min(times)
	std_dev = math.sqrt(sum([(x - average)**2 for x in times]) / len(times))

	return {'average':average, 'std_dev':std_dev, 'minimum':minimum, 'maximum':maximum}

# Run all items in all languages
def benchmark(languages, items, iterations=3, build_only=True):
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
				language_results.append(statistical_analysis([]))
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
				language_results.append(statistical_analysis([]))
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

					language_results.append(statistical_analysis(times))

		results.append(language_results)

	return results


# Print brief summary to console
def print_to_console(languages, items, results):
	languageMaxCharacter = len(max(languages, key = len))
	for measure in sorted(results[0][0].keys()):
		localResult = []
		for lang in results:
			localResult.append([x[measure] for x in lang])
		formattedResults = list(localResult)
		columnMaxes = [len(next) for next in items]
		print("\n" + ("{:^" + str(sum(columnMaxes)) + "}").format(measure))
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
def save_to_file(languages, items, results):
	outPipe = sys.stdout
	sys.stdout = open("results.txt", "w")
	print_to_console(languages, items, results)
	sys.stdout = outPipe


# Generate a nice table output to file
def save_to_html(languages, items, results):
	html = '<html><body>'
	for measure in sorted(results[0][0].keys()):
		table = '<div> <p style="text-align:center">' + measure + '</p>'
		table += '<table style="text-align:right">'
		localResult = []
		for lang in results:
			localResult.append([x[measure] for x in lang])
		heading = "<th></th>" + "".join([ '<th style="font-style:bold;text-align:center;padding:5px 20px;">' + next + "</th>" for next in items])
		table += "<tr>" + heading + "</tr>"
		for i in range(len(languages)):
			row = "<td>" + languages[i] +  "</td>" + "".join(['<td style="padding:5px 20px;">' + "{:.3f}".format(next) + " s" + "</td>" for next in localResult[i]])
			table += "<tr>" + row + "</tr>"
		table += "</table></div>" + "<br><br>"
		html += table
	html += "</body></html>"
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
	languages = get_languages(parse_results.include, parse_results.exclude)
	items = get_items(languages, parse_results.include, parse_results.exclude)

	cleanup(languages, items)
	if parse_results.clean == False or parse_results.buildonly == True:
		results = benchmark(languages, items, parse_results.iterations, parse_results.buildonly)
		if parse_results.buildonly == False:
			print_to_console(languages, items, results)
			save_to_file(languages, items, results)
			save_to_html(languages, items, results)


if __name__ == "__main__":
	main()
