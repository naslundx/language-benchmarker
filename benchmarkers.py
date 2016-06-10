import subprocess
import os

# TODO only supply language folder name and have the rest inside class

class benchmarkerc:
	compiler = "gcc"

	def __init__(self, binpath, srcpath, item, suffix):
		# Put in all the neccessary stuff
		self.binpath = binpath
		self.srcpath = srcpath
		self.item = item
		self.suffix = suffix
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		if not os.path.exists(self.binpath):
			os.makedirs(self.binpath)
		result = subprocess.call([self.compiler, self.srcpath + self.filename, "-o", self.binpath + self.item])
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["./" + self.binpath + self.item], stdout=None) # TODO pipe away output
		return result == 0

class benchmarkercpp:
	compiler = "g++"

	def __init__(self, binpath, srcpath, item, suffix):
		# Put in all the neccessary stuff
		self.binpath = binpath
		self.srcpath = srcpath
		self.item = item
		self.suffix = suffix
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		if not os.path.exists(self.binpath):
			os.makedirs(self.binpath)
		result = subprocess.call([self.compiler, self.srcpath + self.filename, "-o", self.binpath + self.item])
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["./" + self.binpath + self.item], stdout=None) # TODO pipe away output
		return result == 0

class benchmarkerpython:
	def __init__(self, binpath, srcpath, item, suffix):
		# Put in all the neccessary stuff
		self.binpath = binpath
		self.srcpath = srcpath
		self.item = item
		self.suffix = suffix
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		return True

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["python3", self.srcpath + self.filename], stdout=None) # TODO pipe away output
		return result == 0

class benchmarkerooc:
	compiler = "rock"

	def __init__(self, binpath, srcpath, item, suffix):
		# Put in all the neccessary stuff
		self.binpath = binpath
		self.srcpath = srcpath
		self.item = item
		self.suffix = suffix
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		if not os.path.exists(self.binpath):
			os.makedirs(self.binpath)
		my_env = os.environ.copy()
		my_env["OOC_LIBS"] = "/home/mnaslund/versioned/ooc/"
		result = 0 #subprocess.call([self.compiler, "-x", "-q", self.srcpath + self.filename, "+o " + self.binpath], env=my_env)
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = 0 #subprocess.call(["./ooc/run-ooc.sh"])
		return result == 0
