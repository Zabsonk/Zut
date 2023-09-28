//ALG02 IS1 212B LAB04
//Kacper Żabiński
//zk51162@zut.edu.pl
#include <iostream>

using namespace std;
#pragma once


template <class T>
struct Node {
	T data;
	Node<T>* left, * right, * parent;
	int kolor; // 1 -> czerwony 0 -> czarny
	Node(T value) {
		left = nullptr;
		right = nullptr;
		parent = NULL;
		this->kolor = 1;
		this->data = value;

	}
};
template <class T>
class Tree {

	Node<T>* inorder(Node<T>* element) {
		if (element == NULL) {
			return 0;
		}
		inorder(element->left);
		cout << element->data << " lewy: " << element->left << " prawy: " << element->right << " kolor:" << element->kolor << endl;
		inorder(element->right);
	}

	Node<T>* preorder(Node<T>* element) {
		if (element == NULL) {
			return 0;
		}

		cout << element->data << " lewy: " << element->left << " prawy: " << element->right << " kolor:" << element->kolor << endl;
		preorder(element->left);
		preorder(element->right);
	}
	Node<T>* search(Node<T>* element, Node<T> value) {
		if (element->data == value || element == NULL) {
			return element;
		}
		else {
			if (value < element->data) {
				return search(element->left, value);
			}
			else {
				return search(element->right, value);
			}
		}
	}
	Node<T>* wysykosc(Node<T>* element) {
		int left = wysokosc(element->left);
		int right = wysokosc(element->right);
		if (left >= right)
			return left + 1;
		else
			return right + 1;

	}
	Node<T>* insert(Node<T>* element, Node<T>* p) {
		if (element == nullptr) {
			return p;
		}
		if (p->data < element->data) {
			element->left = insert(element->left, p);
			element->left->parent = element;
		}
		else if (p->data > element->data) {
			element->right = insert(element->right, p);
			element->right->parent = element;
		}
		return element;
	}
public:

	Node<T>* root;
	int size;

	void insert(T data) {
		Node<T>* p = new Node<T>(data);
		root = insert(root, p);
		rotate(root, p);

	}
	void show_inorder() {
		inorder(root);
		cout << endl;
	}
	void show_preorder() {
		preorder(root);
		cout << endl;
	}
	template<class T>
	void rotateLeft(Node<T>*& element, Node<T>*& p) {
		Node<T>* r = p->right;
		p->right = r->left;
		if (p->right != NULL) {
			p->right->parent = p;
		}
		r->parent = p->parent;
		if (p->parent == NULL) {
			element = r;
		}
		else if (p == p->parent->left) {
			p->parent->left = r;
		}
		else {
			p->parent->right = r;
		}
		r->left = p;
		p->parent = r;
	}
	template<class T>
	void rotateRight(Node<T>*& element, Node<T>*& p) {
		Node<T>* l = p->left;

		p->left = l->right;

		if (p->left != NULL) {
			p->left->parent = p;
		}
		l->parent = p->parent;

		if (l->parent == NULL) {
			element = l;
		}
		else if (p == p->parent->left) {
			p->parent->left = l;
		}
		else {
			p->parent->right = l;
		}
		l->right = p;
		p->parent = l;
	}
	template<class T>
	void rotate(Node<T>*& element, Node<T>*& p) {
		Node<T>* par = NULL;
		Node<T>* gpar = NULL;
		while ((p != element) && (p->kolor != 0) && (p->parent->kolor == 1)) {
			par = p->parent;
			gpar = p->parent->parent;



			if (par == gpar->left) {
				Node<T>* uncle = gpar->right;



				if (uncle != NULL && uncle->kolor == 1) {
					gpar->kolor = 1;
					par->kolor = 0;
					uncle->kolor = 0;
					p = gpar;
				}
				else {

					if (p == par->right) {
						rotateLeft(element, par);
						p = par;
						par = p->parent;

					}
					rotateRight(element, gpar);
					swap(par->kolor, gpar->kolor);
					p = par;
				}
			}


			else {
				Node<T>* uncle = gpar->left;


				if (uncle != NULL && uncle->kolor == 1) {
					gpar->kolor = 1;
					par->kolor = 0;
					uncle->kolor = 0;
					p = gpar;
				}
				else {
					if (p == par->left) {
						rotateRight(element, par);
						p = par;
						par = p->parent;

					}

					rotateLeft(element, gpar);
					swap(par->kolor, gpar->kolor);
					p = par;
				}



			}
		}
		element->kolor = 0;
	}


	template<class T>
	void search(T value) {
		search(root, value);
	}
	Tree() {
		root = NULL;
		size = 0;
	}
	template<class T>
	int wysokosc(Node<T>* root) {
		if (!root) {
			return 0;
		}
		else {
			wysykosc(root);
		}
	}



};


int main()
{
	Tree<double>* node = new Tree<double>;
	node->insert(23);
	node->insert(21);
	node->insert(2);
	node->insert(26);
	node->insert(13);
	node->insert(28);
	node->insert(33);
	node->insert(55);
	node->insert(67);


	
	node->show_inorder();
}

