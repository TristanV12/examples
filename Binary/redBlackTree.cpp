
#ifndef REDBLACK
#define REDBLACK
// // binaryTree is the binary tree class
// class redBlackTree : public baseTree{

// // Public variables and methods
// public:
// 	// The constructor decides if red/black tree or not
// 	//	TODO: add red/black functionality
// 	redBlackTree(){ }

// 	// add adds a new value to the tree.
// 	//	returns true if successful
// 	bool add(int newValue){
// 		// Create new node
// 		node* new_node = (node*)malloc(sizeof(node));
// 		node* new_left = (node*)malloc(sizeof(node));
// 		node* new_right = (node*)malloc(sizeof(node));
// 		new_node->value = newValue;
// 		new_node->left = NULL;
// 		new_node->right = NULL;
// 		new_node->parent = NULL;

// 		// Corner case: no root. In this case, make root the new node
// 		if(root == NULL){
// 			root = new_node;
// 			root->color = RED;
// 			new_left->parent = root;
// 			new_right->parent = root;
// 			root->left = new_left;
// 			root->right = new_right;
// 			return true;
// 		}

// 		// Otherwise, find its place
// 		else{
// 			node* parent = insert(newValue);

// 			// NULL means value exists, don't add
// 			if(parent == NULL){ return false; }
// 			// Otherwise find its place
// 			if(parent->value > newValue){ parent->left = new_node; }
// 			else{ parent->right = new_node; }
// 			new_node->parent = parent;
// 		}
// 		// Increment size, return true
// 		tree_size++;
// 		return true;
// 	}

// 	// remove removes the node from the list
// 	bool remove(int value){
// 		// Corner case
// 		if(root == NULL){ return false; }

// 		node *tmp_node;

// 		// Corner case where root is the value
// 		if(root->value == value){ tmp_node = root; }
// 		else{
// 			tmp_node = locateNode(value);
// 			if(tmp_node == NULL){ return false; }
// 		}

// 		// Increment size
// 		--tree_size;

// 		// The node we will be freeing
// 		node* real_del;

// 		// Special case if only left leaf exists (just copy right leaf)
// 		if(tmp_node->left == NULL && tmp_node->right != NULL){
// 			*tmp_node = *(tmp_node->right);
// 			real_del = tmp_node->right;
// 		// If no leaves, remove
// 		}else if(tmp_node->left == NULL){
// 			real_del = tmp_node;
// 			if(tmp_node == (tmp_node->parent)->left){ (tmp_node->parent)->left = NULL; }
// 			else{ (tmp_node->parent)->right = NULL; }
// 		// Otherwise, find largest node to the left of current node
// 		}else{
// 			real_del = tmp_node->left;
// 			while(real_del->right != NULL){
// 				real_del = real_del->right;
// 			}
// 			// Take its value
// 			tmp_node->value = real_del->value;
// 			if(real_del->left == NULL){
// 				(real_del->parent)->right = NULL;
// 			}else{
// 				(real_del->parent)->right = real_del->left;
// 				(real_del->left)->parent = real_del->parent;
// 			}
// 		}
// 		// Garbage collection
// 		free(real_del);
// 		return true;
// 	}

// // Private variables and methods
// private:
// 	bool insert(int value, node* location){
// 		if(location->value == NULL){
// 			location->value = value;
// 			location->left = (node*)malloc(sizeof(node));
// 			location->left->parent = location;
// 			location->right = (node*)malloc(sizeof(node));
// 			location->right->parent = location;
// 			return location;
// 		}else if(location->value > value){
// 			return insert(value, location->left);
// 		}else if(location->value < value){
// 			return insert(value, location->right);
// 		}else{
// 			return NULL;
// 		}
// 	}

// 	//repair tree for recursive insertion
// 	void insertRepair(node* leaf){
// 		if(leaf->parent == NULL){
// 			//case 1
// 			leaf->color = BLACK
// 		}else if(leaf->parent->color == BLACK){
// 			//case 2
// 		}else if(uncle(leaf)->color == RED){
// 			//case 3
// 			leaf->parent->color = BLACK;
// 			uncle(leaf)->color = BLACK;
// 			grandparent(leaf)->color = RED;
// 			insertRepair(grandparent(leaf));
// 		}else{
// 			//case 4
// 			node* grandparent = grandparent(leaf);
// 			node* parent = parent(leaf);
// 			if(leaf == grandparent->left->right){
// 				rotateLeft();
// 				leaf = leaf->left;
// 			}else if(leaf == grandparent->right->left){
// 				rotateRight();
// 				leaf = leaf->right;
// 			}

// 			grandparent = grandparent(leaf);
// 			parent = parent(leaf);
// 			if(leaf == parent->left){
// 				rotateRight(grandparent);
// 			}else{
// 				rotateLeft(grandparent);
// 			}
// 			parent->color = BLACK;
// 			grandparent->color = RED;
// 		}
// 	}
// };
#endif