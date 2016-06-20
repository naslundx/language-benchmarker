#include <stdio.h>
#include <stdlib.h>

struct node {
	struct node *left;
	struct node *right;
	int value;
};

void add_node(struct node *root, int v) {
	if (v <= root->value) {
		if (!root->left) {
			root->left = (struct node*)malloc(sizeof(struct node));
			root->left->left = NULL;
			root->left->right = NULL;
			root->left->value = v;
		} else {
			add_node(root->left, v);
		}
	} else {
		if (!root->right) {
			root->right = (struct node*)malloc(sizeof(struct node));
			root->right->left = NULL;
			root->right->right = NULL;
			root->right->value = v;
		} else {
			add_node(root->right, v);
		}
	}
}

int index = 0;
void prefix(struct node *root, int *array) {
	if (root->left) {
		prefix(root->left, array);
	}
	array[index++] = root->value;
	if (root->right) {
		prefix(root->right, array);
	}
}

int main()
{
	int N = 500;
	const int iterations = 10;
	int *array = (int*)calloc(iterations + 1, sizeof(int));
	struct node root;
	root.left = NULL;
	root.right = NULL;
	root.value = N;

	for (int i=0; i<iterations; ++i) {
		N = (2 * N + 10) % 1000;
		add_node(&root, N);
	}

	prefix(&root, array);

	if (index < 1000) {
		return 1;
	}
	for (int i=1; i<iterations; ++i) {
		if (array[i] < array[i - 1]) {
			return i;
		}
	}

	return 0;
}
