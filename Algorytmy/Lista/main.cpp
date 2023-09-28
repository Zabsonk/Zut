/ALG02 IS1 212B LAB01
/Kacper ¯abiñski
/zk51162@zut.edu.pl
#include <iostream>
#include <time.h>


#pragma once
using namespace std;
template <class T>
struct element
{
	T value;
	element<T>* next, * prev;

};
template <class T>
class Lista {
private:
	element<T>* head, * tail;
	int liczba_elementow;
public:
	Lista()
	{
		this->head = NULL;
		this->tail = NULL;
		this->liczba_elementow = 0;
	}
	~Lista()
	{
		element* wsk;
		while (head)
		{
			wsk = head->next;
			delete head;
			head = wsk;

		}
	}
	int rozmiar()
	{
		return liczba_elementow;
	}
	void pokaz();
	void nowy_element_na_koncu(const T& value);
	void nowy_element_na_poczatku(const T& value);
	void usun_ostatni();
	void usun_pierwszy();
	void podmiana(int id, const T& value1);
	void wyszukanie_id(int id);
	void wyszukanie_usuniecie(int);
	void dodanie_po_wartosci(int, const T& value);
	void czyszczenie();
	void wyszukanie_wartosc(const T& value1);

};
template <class T>
void Lista<T>::pokaz() {
	if (head == NULL) {
		cout << "lista jest pusta";
	}
	element<T>* el = head;
	while (el) {
		cout << "=====  " << el->value << "  ======\t";
		el = el->next;
	}
	cout << endl;
}
template <class T>
void Lista<T>::nowy_element_na_poczatku(const T& value) {
	element<T>* el = new element<T>{ value };
	el->next = head;
	if (head != nullptr) {
		head->prev = el;
	}
	head = el;
	if (liczba_elementow == 0) {
		tail = head;
	}
	liczba_elementow = liczba_elementow + 1;
}
template <class T>
void Lista<T>::nowy_element_na_koncu(const T& value) {
	if (liczba_elementow == 0) {
		nowy_element_na_poczatku(value);
		return;
	}
	element<T>* el = new element<T>{ value };
	tail->next = el;
	el->prev = tail;
	tail = el;
	liczba_elementow = liczba_elementow + 1;
}
template <class T>
void Lista<T>::usun_ostatni() {
	if (liczba_elementow == 0) {
		return;
	}
	if (liczba_elementow == 1) {
		usun_pierwszy();
	}
	element<T>* el = tail;
	tail = tail->prev;
	tail->next = nullptr;
	delete el;
	liczba_elementow = liczba_elementow - 1;
}
template <class T>
void Lista<T>::usun_pierwszy() {
	if (liczba_elementow == 0) {
		return;
	}
	element<T>* el = head;
	head = head->next;
	head->prev = nullptr;
	delete el;
	liczba_elementow = liczba_elementow - 1;
}
template<class T>
void Lista<T>::wyszukanie_id(int id) {
	if (liczba_elementow == 0) {
		return;
	}
	if (id<0 || id>liczba_elementow) {
		return;
	}
	int i;
	element<T>* el = head;
	for (i = 0; i < id - 1; i++) {
		el = el->next;
	}
	cout << el->value << "   id= " << i + 1 << endl;
}
template <class T>
void Lista<T>::wyszukanie_usuniecie(int id) {
	if (liczba_elementow == 0) {
		return;
	}
	if (id<0 || id>liczba_elementow) {
		return;
	}
	if (id == 0) {
		usun_pierwszy();
	}
	if (id == liczba_elementow - 1) {
		usun_ostatni();
	}
	element<T>* el1 = head;
	element<T>* tmp;

	for (int i = 0; i < id - 1; i++)
	{
		el1 = el1->next;
	}
	tmp = el1->next;
	el1->next = tmp->next;
	el1->next->prev = el1;

	delete tmp;
	liczba_elementow = liczba_elementow - 1;
}
template <class T>
void Lista<T>::czyszczenie() {
	element<T>* el = head;
	for (int i = 0; i < liczba_elementow - 1; i++) {
		el = el->next;
		el->prev = NULL;

	}
	head = nullptr;
	tail = nullptr;

	delete el;
}
template <class T>
void Lista<T>::dodanie_po_wartosci(int id, const T& value) {
	if (id == 0) {
		nowy_element_na_poczatku(value);
		return;
	}
	if (id == liczba_elementow - 1) {
		nowy_element_na_koncu(value);
		return;
	}
	else {
		element<T>* el = head;
		for (int i = 0; i < id - 1; i++) {
			el = el->next;
		}
	}
}
template <class T>
void Lista<T>::wyszukanie_wartosc(const T& value1) {
	element<T>* el = head;
	int i = 0;
	while (el->value != value1 && i < liczba_elementow - 1) {

		el = el->next;
		i++;
	}
	cout << "jest taki element" << endl;
	cout << el->value << endl;
}
template <class T>
void Lista<T>::podmiana(int id, const T& value1) {
	if (liczba_elementow == 0) {
		return;
	}
	if (id<0 || id>liczba_elementow) {
		return;
	}
	int i;
	element<T>* el = head;
	element<T>* tmp;
	for (i = 0; i < id - 1; i++) {
		el = el->next;
	}
	el->value = value1;

}




int main() {



	Lista<string>* list = new Lista<string>();

	int wybor;

	do {
		cout << "co chcesz zrobic" << endl;
		cout << "1.Pokaz liste" << endl;
		cout << "2.Dodaj element na poczatku" << endl;
		cout << "3.Dodaj element na koncu" << endl;
		cout << "4.Usun pierwszy element" << endl;
		cout << "5.Usun ostatni element" << endl;
		cout << "6.Usun element z id" << endl;
		cout << "7.Pokaz element z id" << endl;
		cout << "8.Usun liste" << endl;
		cout << "9.Dodanie po wartosci" << endl;
		cout << "10.Wyszukaj po wartosci" << endl;
		cout << "11.Podmiana" << endl;
		cin >> wybor;
		switch (wybor) {
		case 1: {
			list->pokaz();
			system("pause");
			system("cls");
			break;
		}
		case 2: {
			cout << "co chcesz dodac na poczatku" << endl;
			string a;
			cin >> a;
			list->nowy_element_na_poczatku(a);
			system("pause");
			system("cls");
			break;
		}
		case 3: {
			cout << "co chcesz dodac na koncu" << endl;
			string a;
			cin >> a;
			list->nowy_element_na_koncu(a);
			system("pause");
			system("cls");
			break;
		}
		case 4: {


			list->usun_pierwszy();
			system("pause");
			system("cls");
			break;
		}
		case 5: {

			list->usun_ostatni();

			system("pause");
			system("cls");
			break;
		}
		case 6: {
			cout << "podaj id ktore chcesz usunac" << endl;
			int a;
			cin >> a;
			list->wyszukanie_usuniecie(a);
			system("pause");
			system("cls");
			break;
		}
		case 7: {
			cout << "podaj id co chcesz zobaczyc" << endl;
			int a;
			cin >> a;
			list->wyszukanie_id(a);

			system("pause");
			system("cls");
			break;
		}
		case 8: {
			list->czyszczenie();
			system("pause");
			system("cls");
			break;
		}
		case 9: {
			int a;
			string b;
			cout << "podaj id" << endl;
			cin >> a;
			cout << "podaj co chcesz dodac " << endl;
			cin >> b;

			list->dodanie_po_wartosci(a, b);
			system("pause");
			system("cls");
			break;
		}

		case 10: {
			cout << "podaj co chcesz znalezc" << endl;
			string b;
			cin >> b;
			list->wyszukanie_wartosc(b);
			system("pause");
			system("cls");
			break;
		}
		case 11: {
			int a;
			cout << "podaj id" << endl;
			cin >> a;
			string b;
			cout << "podaj wartosc" << endl;
			cin >> b;

			list->podmiana(a, b);
			system("pause");
			system("cls");
			break;
		}
		}
	} while (wybor < 12);
	return 0;
}