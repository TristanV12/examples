// Includes
#include<iostream> // for i/o
#include<stdlib.h> // malloc and free

// node is a helpful struct for creating the leaves in the binary tree
struct node{
	int value;
	node* left = NULL;
	node* right = NULL;
	node* parent = NULL;
};

// node is a helpful struct for creating the leaves in the binary tree
struct linked_node{
	int value;
	node* next = NULL;
	node* prev = NULL;
};


// binaryTree is the binary tree class
class binaryTree{

// Public variables and methods
public:
	// The constructor decides if red/black tree or not
	//	TODO: add red/black functionality
	binaryTree(bool is_rb=false){ rb = is_rb; }

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
			*tmp_node = *(tmp_node->right);
			real_del = tmp_node->right;
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
private:
	// variables
	node* root = NULL; // root node
	bool rb = false; // true if red/black enables
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

class linkedList
{
public:
	// Constructor just sets size to 0
	linkedList(){ size = 0; }

	bool add(int value){
		linked_node* new_node = (linked_node*)malloc(sizeof(linked_node));
		new_node->value = value;
		if(root == NULL){
			root = new_node;
			root->prev = NULL;
			root->next = NULL;
			end = new_node;
			++length;
			return true;
		}
		if(root->value > value){
			root->prev = new_node;
			new_node->prev = NULL;
			new_node->next = root;
			++length;
			return true;
		}

		linked_node* curr_node = root;
		while(true){
			if(curr_node->value == value){ return false; }
			if(curr_node->next == NULL || (curr_node->next)->value > value){
				curr_node->next = new_node;
				new_node->prev = curr_node;
				new_node->next = curr_node->next;
				if(curr_node->next == NULL){ end = new_node; }
				++length;
				return true;
			}
			curr_node = curr_node->next;
		}
	}

	bool remove(int value){
		// Corner case
		if(root == NULL){ return false; }
		linked_node* real_del;
		if(root->value == value){
			real_del = root;
			root = root->next;
			root->prev = NULL;
			free(real_del);
			--length;
			return true;
		}

		linked_node* curr_node = root;
		while(true){
			if(curr_node == NULL || curr_node-value > value){ return false; }
			if(curr_node->value == value){
				(curr_node->prev)->next = curr_node->next;
				if(curr_node->next != NULL){
					(curr_node->next)->prev = curr_node->prev;
				}
				free(curr_node);
				--length;
				return true;
			}
		}
	}

	int maxValue(){
		if(root == NULL){ return 0; }
		return end->value;
	}

	int minValue(){
		if(root == NULL){ return 0; }
		return root->value;
	}

	int size(){ return length; }

private:
	linked_node* root = NULL;
	linked_node* end = NULL;
	int length;
};

void test(){
	binaryTree b = new binaryTree();
	std::string str = "";
	for(int i = 0; i < 30; ++i){
		b.add(i);
	}
	for(int i = 50; i < 100; ++i){
		b.add(i);
	}
	for(int i = 20; i < 60; ++i){
		b.add(i);
	}
	for(int i = 0; i < 100; ++i){
		if(i != 0){ str += ", "; }
		str += std::to_string(i);
	}
	std::cout << "toString 100 digits test: ";
	if(b.toString().compare(str) != 0){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }

	std::cout << "maxValue 100 digits test: ";
	if(b.maxValue() != 99){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }

	std::cout << "minValue 100 digits test: ";
	if(b.minValue() != 0){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }

	std::cout << "size 100 digits test: ";
	if(b.size() != 100){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }

}

int main(int argc, char *argv[]){
	test();
    
    return 0;
}