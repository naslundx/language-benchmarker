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
		result = subprocess.call([self.compiler, self.srcpath + self.filename, "-o", self.binpath + self.item, "-std=c11"], stdout=FNULL)
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
	srcpath = "python/"
	suffix = "py"

	def __init__(self, version, item):
		# Put in all the neccessary stuff
		if version == 2:
			self.compiler = "python"
		else:
			self.compiler = "python3"
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		return True

	def execute(self):
		# Run whatever has been done
		result = subprocess.call([self.compiler, self.srcpath + self.filename], stdout=FNULL)
		return result == 0


class benchmarkerooc:
	compiler = "rock"
	srcpath = "ooc/"
	binpath = "ooc/"
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
		my_env["OOC_LIBS"] = "/home/naslundx/versioned/" # TODO Should not have to do this!
		result = subprocess.call([self.compiler, "-q", self.filename], cwd="ooc/", env=my_env, stdout=FNULL)
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["./" + self.binpath + self.item], stdout=FNULL)
		return result == 0


class benchmarkerrust:
	compiler = "rustc"
	srcpath = "rust/"
	binpath = "rust/bin/"
	suffix = "rs"

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


class benchmarkergo:
	compiler = "go"
	srcpath = "go/"
	binpath = "/bin/"
	suffix = "go"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		if not os.path.exists(self.binpath):
			os.makedirs(self.binpath)
		my_env = os.environ.copy()
		my_env["GOPATH"] = "/home/naslundx/versioned/language-benchmarker/go" # TODO Should not have to do this!
		result = subprocess.call([self.compiler, "install", self.item], env=my_env, stdout=FNULL)
		return result == 1

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["./go" + self.binpath + self.item], stdout=FNULL)
		return result == 0


class benchmarkerjava:
	compiler = "javac"
	runner = "javac"
	srcpath = "java/"
	binpath = "java/"
	suffix = "java"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		if not os.path.exists(self.binpath):
			os.makedirs(self.binpath)
		result = subprocess.call([self.compiler, self.filename], cwd="java/", stdout=FNULL)
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["java", self.item], cwd="java/", stdout=FNULL)
		return result == 0


class benchmarkererlang:
	compiler = "erlc"
	runner = "erl"
	srcpath = "erlang/"
	binpath = "erlang/"
	suffix = "erl"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		if not os.path.exists(self.binpath):
			os.makedirs(self.binpath)
		result = subprocess.call([self.compiler, self.filename], cwd="erlang/", stdout=FNULL)
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["erl", "-noshell", "-s", self.item, self.item, "-s", "init", "stop"], cwd="erlang/", stdout=FNULL)
		return result == 0


class benchmarkerhaskell:
	compiler = "ghc"
	srcpath = "haskell/"
	binpath = "haskell/"
	suffix = "hs"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		if not os.path.exists(self.binpath):
			os.makedirs(self.binpath)
		result = subprocess.call([self.compiler, self.filename, "-o", self.item], cwd="haskell/", stdout=FNULL)
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = subprocess.call(["./" + self.item], cwd="haskell/", stdout=FNULL)
		return result == 0


class benchmarkerjavascript:
	compiler = "node"
	srcpath = "js/"
	suffix = "js"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		return True

	def execute(self):
		# Run whatever has been done
		result = subprocess.call([self.compiler, self.filename], cwd="js/", stdout=FNULL)
		return result == 0


class benchmarkercsharp:
	compiler = "mcs"
	runner = "mono"
	srcpath = "csharp/"
	suffix = "cs"
	exesuffix = "exe"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix
		self.binary = self.item + "." + self.exesuffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		result = subprocess.call([self.compiler, self.filename], cwd="csharp/", stdout=FNULL)
		return result == 0

	def execute(self):
		# Run whatever has been done
		result = subprocess.call([self.runner, self.binary], cwd="csharp/", stdout=FNULL)
		return result == 0


class benchmarkerlua:
	compiler = "lua"
	srcpath = "lua/"
	suffix = "lua"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		return True

	def execute(self):
		# Run whatever has been done
		result = subprocess.call([self.compiler, self.filename], cwd="lua/", stdout=FNULL)
		return result == 0



class benchmarkerruby:
	compiler = "ruby"
	srcpath = "ruby/"
	suffix = "rb"

	def __init__(self, item):
		# Put in all the neccessary stuff
		self.item = item
		self.filename = self.item + "." + self.suffix

	def prepare(self):
		# Languages like C, C++ need to compile, script languages need nothing?
		return True

	def execute(self):
		# Run whatever has been done
		result = subprocess.call([self.compiler, self.filename], cwd="ruby/", stdout=FNULL)
		return result == 0