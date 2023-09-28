//SO IS1 212B LAB12
//Kacper Żabiński 
//zk51162@zut.edu.pl
#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/ipc.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/sem.h>
int main(int argc, char *argv[])
{
    if (argc != 3) {
        printf("Niepoprawna liczba argumentow. Uzycie: nadajnik [klucz_pamieci] [plik_wejsciowy]\n");
        exit(1);
    }
    char *klucz_pamieci = argv[1];
    char *plik_wejsciowy = argv[2];
    key_t key;
    int shmid;
    char *data;
    int fd;
    int size;
    int bytes_read;

    // Tworzenie klucza dla pamieci 
    if ((key = ftok(klucz_pamieci, 'R')) == -1) {
        perror("Blad przy tworzeniu klucza");
        exit(1);
    }

    // Tworzenie segmentu pamieci 
    if ((shmid = shmget(key, 1024, 0666 | IPC_CREAT)) == -1) {
        perror("Blad przy tworzeniu segmentu pamieci");
        exit(1);
    }
	
	
    // Przydzielanie segmentu pamieci do procesu
    data = shmat(shmid, (void *)0, 0);
    if (data == (char *)(-1)) {
        perror("Blad przy przydzielaniu segmentu pamieci");
        exit(1);
    }

    // Otwieranie pliku 
    if ((fd = open(plik_wejsciowy, O_RDONLY)) == -1) {
        perror("Blad przy otwieraniu pliku wejsciowego");
        exit(1);
    }

    // Pobieranie rozmiaru pliku
    size = lseek(fd, 0, SEEK_END);
    lseek(fd, 0, SEEK_SET);
	
	// semafor
	int semid;
	if((semid=semget(key,1,IPC_CREAT|0666))==-1){
		perror("Błąd przy tworzeniu semfafora");
	exit(1);		
	}
	if(semctl(semid,0,SETVAL,size)==-1){
		perror("Błąd przu ustawianu semafora");
	exit(1);	
	}
    // Wysylanie danych z pliku do pamieci
    	int offset = 0;
   	 while (offset < size) {
	int pomoc=(size-offset)<1024 ? (size-offset):1024;
        bytes_read = read(fd, data, pomoc);
        offset += bytes_read;
        printf("Wyslano %d bajtow, postep: %d%%\n", bytes_read, (offset * 100) /size);
}

// Zamykanie pliku wejsciowego
close(fd);



return 0;
}

