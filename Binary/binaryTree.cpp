#include"nodes.cpp"
#include"baseClass.cpp"

#ifndef BINTREE
#define BINTREE
// binaryTree is the binary tree class
class binaryTree : public baseTree{

// Public variables and methods
public:
	// The constructor decides if red/black tree or not
	//	TODO: add red/black functionality
	binaryTree(){ }

	// add adds a new value to the tree.
	//	returns true if successful
	bool add(int newValue){
		// Create new node
		node* new_node = (node*)malloc(sizeof(node));
		new_node->value = newValue;
		new_node->left = NULL;
		new_node->right = NULL;
		new_node->parent = NULL;

		// Corner case: no root. In this case, make root the new node
		if(root == NULL){ root = new_node; }

		// Otherwise, find its place
		else{
			node* parent = locateEmptyParent(newValue);

			// NULL means value exists, don't add
			if(parent == NULL){ return false; }
			// Otherwise find its place
			if(parent->value > newValue){ parent->left = new_node; }
			else{ parent->right = new_node; }
			new_node->parent = parent;
		}
		// Increment size, return true
		tree_size++;
		return true;
	}

	// remove removes the node from the list
	bool remove(int value){
		// Corner case
		if(root == NULL){ return false; }
		node *tmp_node;

		// Corner case where root is the value
		if(root->value == value){ tmp_node = root; }
		else{
			tmp_node = locateNode(value);
			if(tmp_node == NULL){ return false; }
		}

		// Increment size
		--tree_size;

		// The node we will be freeing
		node* real_del;

		// Special case if only left leaf exists (just copy right leaf)
		if(tmp_node->left == NULL && tmp_node->right != NULL){
			real_del = tmp_node;
			tmp_node = tmp_node->parent;
			// If this is the root node, replace root with the node to the right
			if(tmp_node == NULL){
				root = real_del->right;
				real_del->parent = NULL;
			}else{
				tmp_node->right = real_del->right;
				tmp_node->left = real_del->left;
				tmp_node->value = real_del->value;
			}
		// If no leaves, remove
		}else if(tmp_node->left == NULL){
			real_del = tmp_node;
			if(tmp_node == (tmp_node->parent)->left){ (tmp_node->parent)->left = NULL; }
			else{ (tmp_node->parent)->right = NULL; }
		// Otherwise, find largest node to the left of current node
		}else{
			real_del = tmp_node->left;
			while(real_del->right != NULL){
				real_del = real_del->right;
			}
			// Take its value
			tmp_node->value = real_del->value;
			if(real_del->left == NULL){
				(real_del->parent)->right = NULL;
			}else{
				(real_del->parent)->right = real_del->left;
				(real_del->left)->parent = real_del->parent;
			}
		}
		// Garbage collection
		free(real_del);
		return true;
	}
};
#endif