// Includes
#include<iostream> // for i/o
#include <stdlib.h> // malloc and free

// node is a helpful struct for creating the leaves in the binary tree
struct node{
	int value;
	node* left = NULL;
	node* right = NULL;
	node* parent = NULL;
};


// binaryTree is the binary tree class
class binaryTree{

// Public variables and methods
public:
	// The constructor decides if red/black tree or not
	//	TODO: add red/black functionality
	binaryTree(bool is_rb=false){
		rb = is_rb;
	}

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
		size++;
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
		--size;
		node* real_del;
		if(tmp_node->left == NULL && tmp_node->right != NULL){
			*tmp_node = *(tmp_node->right);
			real_del = tmp_node->right;
		}else if(tmp_node->left == NULL){
			real_del = tmp_node;
			if(tmp_node == (tmp_node->parent)->left){ (tmp_node->parent)->left = NULL; }
			else{ (tmp_node->parent)->right = NULL; }
		}else{
			real_del = tmp_node->left;
			while(real_del->right != NULL){
				real_del = real_del->right;
			}
			tmp_node->value = real_del->value;
			if(real_del->left == NULL){
				(real_del->parent)->right = NULL;
			}else{
				(real_del->parent)->right = real_del->left;
				(real_del->left)->parent = real_del->parent;
			}
		}
		// free(real_del);
		return true;
	}

	bool contains(int value){
		// If tree is empty, obviously it does not contain the value
		if(root == NULL){ return false; }

		// But if not...
		return locateEmptyParent(value) != NULL;
	}

	int maxValue(){
		// Corner case
		if(root == NULL){ return 0; }
		node* tmp_node = root;

		// Find max node
		while(tmp_node->right != NULL){ tmp_node = tmp_node->right; }
		return tmp_node->value;
	}

	int minValue(){
		// Corner case
		if(root == NULL){ return 0; }
		node* tmp_node = root;

		// Find max node
		while(tmp_node->left != NULL){ tmp_node = tmp_node->left; }
		return tmp_node->value;
	}

	std::string toString(){
		if(root == NULL){ return ""; }
		std::string output = "";
		recurseString(&output, root);
		return output;
	}

private:
	node* root = NULL;
	bool rb = false;
	int size = 0;

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

int main(int argc, char *argv[]){
	binaryTree b = new binaryTree();
	b.add(1);
	b.add(5);
	b.add(3);
	b.add(4);
	std::cout << b.toString();
	b.remove(3);
	std::cout << b.toString();

	// for (int i = 0; i < 10; ++i){
	// 	/* code */
	// }
    
    return 0;
}