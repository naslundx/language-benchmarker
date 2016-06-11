import subprocess
import os

FNULL = open(os.devnull, 'w')

class benchmarkerc:
	compiler = "gcc"
	srcpath = "c/"
	binpath = "c/bin/"
	suffix = "c"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		if not os.path.exists(self.binpath):
			os.makedirs(self.binpath)
		result = subprocess.call([self.compiler, self.srcpath + self.filename, "-o", self.binpath + self.item], stdout=FNULL)
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["./" + self.binpath + self.item], stdout=FNULL)
		return result == 0

class benchmarkercpp:
	compiler = "g++"
	srcpath = "cpp/"
	binpath = "cpp/bin/"
	suffix = "cpp"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		if not os.path.exists(self.binpath):
			os.makedirs(self.binpath)
		result = subprocess.call([self.compiler, self.srcpath + self.filename, "-o", self.binpath + self.item], stdout=FNULL)
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["./" + self.binpath + self.item], stdout=FNULL)
		return result == 0

class benchmarkerpython:
	srcpath = "python3/"
	suffix = "py"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		return True

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["python3", self.srcpath + self.filename], stdout=FNULL)
		return result == 0

class benchmarkerooc:
	compiler = "rock"
	srcpath = "ooc/"
	binpath = "ooc/bin/"
	suffix = "ooc"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		if not os.path.exists(self.binpath):
			os.makedirs(self.binpath)
		my_env = os.environ.copy()
		my_env["OOC_LIBS"] = "/home/mnaslund/versioned/ooc/"
		result = subprocess.call([self.compiler, "-x", "-q", self.srcpath + self.filename, "+o " + self.binpath], env=my_env, stdout=FNULL)
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["./ooc/run-ooc.sh"], stdout=FNULL)
		return result == 0
