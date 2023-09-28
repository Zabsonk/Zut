#ALGO02 IS1 212B LAB03
#Kacper Żabiński
#zk51162@zut.edu.pl
#include <iostream>

#pragma once
using namespace std;
template <class T>
struct Node {
public:
	T data; //key
	Node<T>* left, * right, * parent;
	int id;

};
template <class T>
class Tree {
public:
	Node<T>* root;
	int size;
	Tree() {
		this->root = NULL;
		this->size = 0;
	}
	Node<T>* dodaj(Node<T>* node, const T& data);
	Node<T>* szukaj(Node<T>* node, const T& data);
	Node<T>* usun(Node<T>* node, const T& data);
	void pokaz(Node<T>* node) {
		if (node) {
			cout << node->id << "" << node << " " << node->data;
			cout << "parent:" << node->parent << "left:" << node->left << "right:" << node->right << endl;
			pokaz(node->left);
			pokaz(node->right);
		}
	};
	bool search(const T& data);
	void inorder(Node<T>* node);
	void preorder(Node<T>* node);
	void usun(const T& data);
	void insert(const T& data);
	void del(Node<T>* root);
	int wysokosc(Node<T>* root);
	
};

	
	

template<class T>
Node<T>* Tree<T>::dodaj(Node<T>* node, const T& data) {
	if (node == nullptr) {
		node = new Node<T>{};
		node->data = data;
		node->left = nullptr;
		node->right = nullptr;
		node->parent = nullptr;
	}
	else if (node->data < data) {
		node->right = dodaj(node->right, data);
		node->right->parent = node;
	}
	else {
		node->left = dodaj(node->left, data);
		node->left->parent = node;
	}
	return node;
}
template<class T>
void Tree<T>::insert(const T& data) {
	root = dodaj(root, data);
	size++;
}
template<class T>
void Tree<T>::preorder(Node<T>* node) {
	if (!node) {
		return;
	}
	cout << node->data << " ";
	preorder(node->left);
	preorder(node->right);
}
template<class T>
void Tree<T>::inorder(Node<T>* node) {
	if (!node) {
		return;
	}
	inorder(node->left);
	cout << node->data << " ";
	inorder(node->right);
}
template<class T>
Node<T>* Tree<T>::szukaj(Node<T>* node, const T& data) {
	if (!node) {

		return nullptr;
	}
	else if (node->data) {

		return node;
	}
	else if (node->data < data) {
		return szukaj(node->right, data);
	}
	else {
		return szukaj(node->left, data);
	}
}
template<class T>
bool Tree<T>::search(const T& data) {
	return szukaj(root, data);
}
template<class T>
Node<T>* Tree<T>::usun(Node<T>* node, const T& data) {
	if (node == nullptr) {
		return nullptr;
	}
	if (node->data == data) {
		if (node->left == nullptr && node->right == nullptr) {
			node = nullptr;
		}
		else if (node->left == nullptr && node->right != nullptr) {
			node->right->parent = node->parent;
			node = node->right;
		}
		else if (node->left != nullptr && node->right == nullptr) {
			node->left->parent = node->parent;
			node = node->left;
		}

	}
	else if (node->data < data) {
		node->right = usun(node->right, data);
	}
	else {
		node->left = usun(node->left, data);
	}
	return node;
}
template<class T>
void Tree<T>::usun(const T& data) {
	root = usun(root, data);
}
template<class T>
void Tree<T>::del(Node<T>* node) {

	if (!node) {
		return;
		delete(node->left);
		delete(node->left);
		if (!node->left && !node->right) {
			delete node;
			node = NULL;
		}

	}
}
template<class T>
int Tree<T>::wysokosc(Node<T>* root) {
	if (!root) {
		return 0;
	}
	else {
		int left = wysokosc(root->left);
		int right = wysokosc(root->right);
		if (left >= right)
			return left + 1;
		else
			return right + 1;
	}
}





int main()
{

    Tree<int>* node = new Tree<int>;
    node->insert(0);
    node->insert(0);
    node->inorder(node->root); cout << endl;
    node->usun(51);
    node->inorder(node->root);
    int h = node->wysokosc(node->root);
    cout << endl << h;
    node->pokaz(node->root);
    //node->inorder(node->root);
    //node->usun(51);
    node->del(node->root);
    node->inorder(node->root);
    //node->inorder(node->root);
    //int h = node->wysokosc(node->root);
    //cout << endl << h;*/
     
    return 0;
}

