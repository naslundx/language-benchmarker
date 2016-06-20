#include <iostream>
#include <vector>

class Node {
public:
	Node(int v) : value(v) { }
	void add(int v);
	void prefix(std::vector<int>&);
private:
	int value;
	Node *left = nullptr;
	Node *right = nullptr;
};

void Node::add(int v) {
	if (v <= this->value) {
		if (!this->left) {
			this->left = new Node(v);
		} else {
			this->left->add(v);
		}
	} else {
		if (!this->right) {
			this->right = new Node(v);
		} else {
			this->right->add(v);
		}
	}
}

void Node::prefix(std::vector<int>& vec) {
	if (this->left) {
		this->left->prefix(vec);
	}
	vec.push_back(this->value);
	if (this->right) {
		this->right->prefix(vec);
	}
}

int main() {
	int N = 500;
	const int iterations = 1000;
	std::vector<int> vec;

	Node root(N);

	for (int i=0; i<iterations; ++i) {
		N = (2 * N + 10) % 1000;
		root.add(N);
	}

	root.prefix(vec);
	if (vec.size() < 1000) {
		return 1;
	}

	for (int i = 1; i < iterations; i++) {
		if (vec[i] < vec[i - 1]) {
			return i;
		}
	}

	return 0;
}
