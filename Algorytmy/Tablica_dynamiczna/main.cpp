//ALG02 IS1 212B LAB02
//Kacper ¯abiñski
//zk51162@zut.edu.pl
#include <iostream>
using namespace std;
template <class T>
class Tablica {
private:
	T* arr;
	size_t maxsize;
	size_t size;
public:
	Tablica() {

		this->size = 0;
		this->maxsize = 1;
		arr = new T[maxsize];
	};
	T operator [](int index) {
		return arr[index];
	}
	void dodaj(T element);
	void stworz();
	void pokaz();
	void usun();
	void podmiana(int, T element);
	void sortuj();
	void pokaz_id(int);
};
template <class T>
void Tablica<T>::pokaz() {
	for (int i = 0; i < size; i++) {
		cout << "=====  " << arr[i] << "  ======\t";
	}
	cout << "\nsize: " << size << " maxsize: " << maxsize << endl;
}
template <class T>
void Tablica<T>::stworz() {
	maxsize = 2 * size;
	T* tmp = new T[maxsize];
	for (int i = 0; i < size; i++) {
		tmp[i] = arr[i];
	}
	delete[]arr;
	arr = tmp;
}
template <class T>
void Tablica<T>::dodaj(T element) {
	if (size == maxsize) {
		stworz();
	}
	arr[size] = element;
	size++;
}
template <class T>
void Tablica<T>::usun() {

	delete[] arr;
	arr = nullptr;
	size = 0;
	maxsize = 1;
}
template <class T>
void Tablica<T>::pokaz_id(int id){
	if (id > size || id < 0) {
		cout << "id poza zakresem";
	}

	cout << "=====  " << arr[id-1] << "  ======\t";
	cout << "\nsize: " << size << " maxsize: " << maxsize << endl;
	
}
template <class T>
void Tablica<T>::podmiana(int id, T element){
	if (id > size || id < 0) {
		cout << "id poza zakresem";
	}
	arr[id] = element;
}
template <class T>
void Tablica<T>::sortuj(){
	
	for (int i = 0; i < size; i++)
		for (int j = 1; j < size - i; j++) //pêtla wewnêtrzna
			if (arr[j - 1] > arr[j])
				//zamiana miejscami
				swap(arr[j - 1], arr[j]);
	

}

int main()
{
    Tablica<int>* tab = new Tablica<int>();
    int wybor;
    do {

        cout << "TABLICA DYNAMICZNA" << endl;
        cout << "1.dodanie nowego elementu na koñcu" << endl;
        cout << "2.zwrocenie danych i-tego elementu" << endl;
        cout << "3.podmiana" << endl;
        cout << "4.Pokaz tablice" << endl;
        cout << "5.Sortuj tablice" << endl;
        cout << "6.Czyszczenie" << endl;
        cin >> wybor;

        switch (wybor) {
        case 1: {
            int a;
            cout << "podaj co chcesz dodac" << endl;
            cin >> a;
            tab->dodaj(a);
            system("pause");
            system("cls");
            break;
        }
        case 2: {
            int a;
            cout << "podaj id";
            cin >> a;
            tab->pokaz_id(a);
            system("pause");
            system("cls");
            break;
        }
        case 3: {
            int a, b;
            cout << "podaj id";
            cin >> a;
            cout << "podaj wartosc";
            cin >>b;
            tab->podmiana(a,b);
            system("pause");
            system("cls");
            break;
        }
        case 4: {
            tab->pokaz();
            system("pause");
            system("cls");
            break;
        }
        case 5: {
            tab->sortuj();
            system("pause");
            system("cls");
            break;
        }
        case 6: {
            tab->usun();
            system("pause");
            system("cls");
            break;
        }
        default: {
            cout << "Prosze cos wybrac"<<endl;
            break;
        }
        }
    } while (wybor < 6);
}
