//SO IS1 212B LAB10
//Kacper Żabiński
//zk51162@zut.edu.pl
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>
#include <time.h>
#include <math.h>
pthread_mutex_t mutex;
double pit=1;
struct D{
	int size;
	int first;
};
void* fun(void* a){
	
	struct D *md=a;
	double wynik_t=1.0;
	printf("Wątek #%ld rozmiar=%d pierwszy_wyraz=%d\n", pthread_self(),md->size,md->first);
	
        for (double i = md->first; i <=md->size+md->first; i++) {
            wynik_t = (double)wynik_t * (((2*i) * (2*i)) /(((2*i)-1)*((2*i)+1)));	
        }
	pthread_mutex_lock(&mutex);
	pit=pit*wynik_t;
	pthread_mutex_unlock(&mutex);
	printf("Wynik wątku: %.15f\n",wynik_t);
	
}

int main(int argc,char* argv[])
{
    if (argc != 3) {
        printf("Liczba argumentów musi być równa 2\n");
    }
   
    else {
	struct timespec start,stop,start2,stop2;
	double time_t;
	double time;
	int a=atoi(argv[1]);
	int b=atoi(argv[2]);
	pthread_t th[b];
	//double* wyn;
	pthread_mutex_init(&mutex, NULL);
	
		
		int i;
		struct D d[b];
		
		int first=1;
		int size=a/b;
		for(int i=0;i<b;i++){
		d[i].first=first;
		d[i].size=size;
		first+=size;
		}		
		
		if(a%b!=0){
			d[b-1].size+=a%b;}
		
		clock_gettime(CLOCK_REALTIME,&start);
		for(i=0;i<b;i++){
			if(pthread_create(&th[i], NULL,&fun,&d[i])!=0){
			return 0;
			}
					
		}
		for(i=0;i<b;i++){
			if(pthread_join(th[i],NULL)!=0){
			return 0;
			}
		
		}
		
		clock_gettime(CLOCK_REALTIME,&stop);
		time_t=(double)(stop.tv_sec-start.tv_sec)+(stop.tv_nsec-start.tv_nsec)*pow(10,-9);
		printf("Z wątkami:%f czas: %.20f\n",pit*2,time_t);
	
	

	// pi bez wątków ->
        double pi = 1;
	 clock_gettime(CLOCK_REALTIME,&start2);
        for (double i = 1; i <= a; i++) {
            pi = pi * (((2*i) * (2*i)) /(((2*i)-1)*((2*i)+1)));
		
        }
	pi=pi*2;
	clock_gettime(CLOCK_REALTIME,&stop2);
		time=(double)(stop2.tv_sec-start2.tv_sec)+(stop2.tv_nsec-start2.tv_nsec)*pow(10,-9);
	fprintf(stdout,"Bez wątków : %f  czas %.20lf\n",pi,time);
	
    	// <- pi bez wątków
	

	pthread_mutex_destroy(&mutex);

	}


}
