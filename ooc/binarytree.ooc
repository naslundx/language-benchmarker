Node: class {
	_left: Node = null
	_right: Node = null
	_value: Int
	value ::= this _value

	init: func (=_value)
	add: func (v: Int) {
		if (v <= this _value) {
			if (this _left == null) {
				this _left = Node new(v)
			} else {
				this _left add(v)
			}
		} else {
			if (this _right == null) {
				this _right = Node new(v)
			} else {
				this _right add(v)
			}
		}
	}
	prefix: func (list: VectorList<Int>) {
		if (this _left != null) {
			this _left prefix(list)
		}
		list add(this _value)
		if (this _right != null) {
			this _right prefix(list)
		}
	}
}

N := 500
root := Node new(N)
iterations := 1000
items := VectorList<Int> new(iterations)

for (i in 0 .. iterations) {
	N = (2 * N + 10) % 1000
	root add(N)
}

root prefix(items)

// items count toString() println()
for (i in 0 .. items count - 1) {
	if (items[i + 1] < items[i]) {
		exit(3)
	}
}
