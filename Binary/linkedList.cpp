#include"nodes.cpp"

#ifndef LINKEDLIST
#define LINKEDLIST

class linkedList
{
public:
	// Constructor just sets size to 0
	linkedList(bool hi=false){ length = 0; }

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
			root = new_node;
			++length;
			return true;
		}

		linked_node* curr_node = root;
		while(true){
			if(curr_node->value == value){ return false; }
			if(curr_node->next == NULL || (curr_node->next)->value > value){
				new_node->next = curr_node->next;
				curr_node->next = new_node;
				new_node->prev = curr_node;
				if(new_node->next == NULL){ end = new_node; }
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
			if(curr_node == NULL || curr_node->value > value){ return false; }
			if(curr_node->value == value){
				(curr_node->prev)->next = curr_node->next;
				if(curr_node->next != NULL){
					(curr_node->next)->prev = curr_node->prev;
				}
				free(curr_node);
				--length;
				return true;
			}
			curr_node = curr_node->next;
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

	std::string toString(){
		linked_node* curr_node = root;
		std::string output = "";
		while(curr_node != NULL){
			output += std::to_string(curr_node->value);
			if(curr_node->next != NULL){ output += ", "; }
			curr_node = curr_node->next;
		}
		return output;
	}

private:
	linked_node* root = NULL;
	linked_node* end = NULL;
	int length;
};
#endif