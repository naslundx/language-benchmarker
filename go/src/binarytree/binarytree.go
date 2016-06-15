package main

import (
	"fmt"
	"os"
)

type Node struct {
	left, right *Node
	value int
}

func (n *Node) Add(v int) {
	if n.value == -1 {
		n.value = v
	} else if v < n.value {
		if n.left == nil {
			n.left = &Node{nil, nil, v}
		} else {
			n.left.Add(v)
		}
	} else {
		if n.right == nil {
			n.right = &Node{nil, nil, v}
		} else {
			n.right.Add(v)
		}
	}
}

var listindex int = 0
var list [1000]int

func (n *Node) Prefix() {
	if n.left != nil {
		n.left.Prefix()
	}
	list[listindex] = n.value
	listindex++
	if n.right != nil {
		n.right.Prefix()
	}
}

func main() {
	root := &Node{nil, nil, -1}
	N := 500
	iterations := 1000
	listindex = 0

	for iterations > 0 {
		iterations--
		root.Add(N)
		N = (2 * N + 10) % 1000
	}

	root.Prefix()
	if (listindex < 1000) {
		os.Exit(1)
	}
	for i := 1; i < 1000; i++ {
		if (list[i] < list[i - 1]) {
			fmt.Println("OOPS")
			os.Exit(i)
		}
	}
}
