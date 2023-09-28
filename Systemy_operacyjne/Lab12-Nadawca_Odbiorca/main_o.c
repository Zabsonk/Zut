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
        printf("Niepoprawna liczba argumentow. Uzycie: odbiornik [klucz_pamieci] [plik_wyjsciowy]\n");
        exit(1);
    }
    char *klucz_pamieci = argv[1];
    char *plik_wyjsciowy = argv[2];
    key_t key;
    int shmid;
    char *data;
    int fd;
    int bytes_written;
	int size;

    // Tworzenie klucza dla pamieci wspoldzielonej
    if ((key = ftok(klucz_pamieci, 'R')) == -1) {
        perror("Blad przy tworzeniu klucza");
        exit(1);
    }

    // Pobieranie dostepu do segmentu pamieci wspoldzielonej
    if ((shmid = shmget(key, 1024, 0666)) == -1) {
        perror("Blad przy pobieraniu dostepu do segmentu pamieci");
        exit(1);
    }

    // Przydzielanie segmentu pamieci do procesu
    data = shmat(shmid, (void *)0, 0);
    if (data == (char *)(-1)) {
        perror("Blad przy przydzielaniu segmentu pamieci");
        exit(1);
    }

    // Tworzenie pliku wyjsciowego
    if ((fd = open(plik_wyjsciowy, O_CREAT | O_TRUNC | O_WRONLY, 0644)) == -1) {
        perror("Blad przy tworzeniu pliku wyjsciowego");
        exit(1);
    }
	int semid;
	if((semid=semget(key,1,0666))==-1){
		perror("Błąd przy pobieraniu dostepu do semafora");
	exit(1);	
	}
	size=semctl(semid,0,GETVAL);
    // Odbieranie danych z pamieci wspoldzielonej i zapisywanie do pliku wyjsciowego
    int offset = 0;
    while (offset < size) {
	int pomoc=(size-offset)<1024 ? (size-offset):1024;
        bytes_written = write(fd, data,pomoc);
        offset += bytes_written;
        printf("Odebrano %d bajtów, postęp: %d%%\n", bytes_written, (offset * 100) / 1024); 
	}

// Zamykanie pliku wyjsciowego
	close(fd);

// Usuniecie segmentu pamieci po zakonczeniu transferu
	if (shmctl(shmid, IPC_RMID, NULL) == -1) {
    	perror("Blad przy usuwaniu segmentu pamieci");
   	 exit(1);
	}

return 0;
}
