#include<iostream> // for i/o
#include<stdlib.h> // malloc and free

#ifndef NODES
#define NODES
#define BLACK 0;
#define RED 1;

// node is a helpful struct for creating the leaves in the binary tree
struct node{
	int value;
	node* left = NULL;
	node* right = NULL;
	node* parent = NULL;
	short color = BLACK;
};

// node is a helpful struct for creating the leaves in the binary tree
struct linked_node{
	int value;
	linked_node* next = NULL;
	linked_node* prev = NULL;
};
#endif