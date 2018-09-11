#include<iostream> // for i/o
#include<stdlib.h> // malloc and free
#include"nodes.cpp"

#ifndef BASE
#define BASE
// baseTree is the base class
class baseTree{

// Public variables and methods
public:
	// The constructor decides if red/black tree or not
	//	TODO: add red/black functionality
	baseTree(){ }

	// contains checks if value exists in the tree
	bool contains(int value){
		// If tree is empty, obviously it does not contain the value
		if(root == NULL){ return false; }

		// But if not...
		return locateEmptyParent(value) == NULL;
	}

	// maxValue finds the maximum value in the tree
	int maxValue(){
		// Corner case
		if(root == NULL){ return 0; }
		node* tmp_node = root;

		// Find max node
		while(tmp_node->right != NULL){ tmp_node = tmp_node->right; }
		return tmp_node->value;
	}

	// minValue finds the minimum value in the tree
	int minValue(){
		// Corner case
		if(root == NULL){ return 0; }
		node* tmp_node = root;

		// Find min node
		while(tmp_node->left != NULL){ tmp_node = tmp_node->left; }
		return tmp_node->value;
	}

	// toString returns a sorted, readable representation of the tree
	std::string toString(){
		if(root == NULL){ return ""; }
		std::string output = "";
		recurseString(&output, root);
		return output;
	}

	// size returns the size of the tree
	int size(){ return tree_size; }

// Private variables and methods
protected:
	// variables
	node* root = NULL; // root node
	int tree_size = 0; // number of nodes in the list

	// locateEmptyParent is a helper method for finding the parent where a new node
	//	should be inserted. Returns NULL if the value exists
	node* locateEmptyParent(int value){
		node* curr_node = root;
		while(true){
			// If the node is in the list, return NULL
			if(value == curr_node->value){ return NULL; }

			// Otherwise, check to see where to go
			if(value < curr_node->value){
				if(curr_node->left == NULL){ return curr_node; }
				curr_node = curr_node->left;
			}else{
				if(curr_node->right == NULL){ return curr_node; }
				curr_node = curr_node->right;
			}
		}
	}

	// locateNode by contrast is a helper method for finding the location of a value
	//	in the tree. Returns NULL if the value DOES NOT exist
	node* locateNode(int value){
		node* curr_node = root;
		while(true){
			// If the node is in the list, return node
			if(value == curr_node->value){ return curr_node; }

			// Otherwise, check to see where to go
			if(value < curr_node->value){
				if(curr_node->left == NULL){ return NULL; }
				curr_node = curr_node->left;
			}else{
				if(curr_node->right == NULL){ return NULL; }
				curr_node = curr_node->right;
			}
		}
	}

	// recurseString is a helper recursive function for printing the sorted tree
	void recurseString(std::string* output, node* root_node){
		if(root_node->left != NULL){
			recurseString(output, root_node->left);
			*output += ", ";
		}
		*output += std::to_string(root_node->value);
		if(root_node->right != NULL){
			*output += ", ";
			recurseString(output, root_node->right);
		}
	}
};
#endif