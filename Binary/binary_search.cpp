// Includes
#include<iostream> // for i/o
#include<stdlib.h> // malloc and free
#include"baseClass.cpp"
#include"binaryTree.cpp"
#include"linkedList.cpp"

void testBinaryTree(){
	std::cout << "Starting binaryTree tests" << std::endl;
	binaryTree b = binaryTree();
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
	b.remove(0);
	for(int i = 1; i < 100; ++i){
		if(i != 1){ str += ", "; }
		str += std::to_string(i);
	}
	std::cout << "toString 100 digits test: ";
	if(b.toString().compare(str) != 0){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }

	std::cout << "maxValue 100 digits test: ";
	if(b.maxValue() != 99){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }

	std::cout << "minValue 100 digits test: ";
	if(b.minValue() != 1){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }

	std::cout << "size 100 digits test: ";
	if(b.size() != 99){ std::cout << "FAILED" << std::endl << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl << std::endl; }
}

void testList(){
	std::cout << "Starting linkedList tests" << std::endl;
	linkedList b = new linkedList();
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
	b.remove(0);
	for(int i = 1; i < 100; ++i){
		if(i != 1){ str += ", "; }
		str += std::to_string(i);
	}
	std::cout << "toString 100 digits test: ";
	if(b.toString().compare(str) != 0){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }

	std::cout << "maxValue 100 digits test: ";
	if(b.maxValue() != 99){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }

	std::cout << "minValue 100 digits test: ";
	if(b.minValue() != 1){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }

	std::cout << "size 100 digits test: ";
	if(b.size() != 99){ std::cout << "FAILED" << std::endl; }
	else{ std::cout << "SUCCESS" << std::endl; }
}

int main(int argc, char *argv[]){
	testBinaryTree();
	testList();
    
    return 0;
}