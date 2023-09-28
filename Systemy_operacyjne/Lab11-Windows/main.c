//SO IS1 212B LAB11
//Kacper Żabiński
//zk51162@zut.edu.pl
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <windows.h>
#include <locale.h>
double pit=0;
HANDLE mutex;
struct D{
	long int size;
	long int first;
};
DWORD WINAPI fun(LPVOID a){
    double wynik_t=0;
    struct D *md=a;
    fprintf(stdout,"ID: #%lu size: %ld first=%ld \n",GetCurrentThreadId(),md->size,md->first);
    for(double i=md->first;i<=md->size+md->first;i++){
        wynik_t=wynik_t+(pow((-1),i)/((2*i)+1));
	}
	WaitForSingleObject(mutex,INFINITE);
	pit=pit+wynik_t;
    ReleaseMutex(mutex);
	fprintf(stdout,"Thread #%lu wynik=%.15f\n",GetCurrentThreadId(),wynik_t);

}
int main(int argc,char* argv[])
{
    setlocale(LC_CTYPE, "Polish");
    if (argc != 3) {
        printf("Liczba argumentów musi byæ równa 2\n");
    }
    else{

        int a=atoi(argv[1]);
        int b=atoi(argv[2]);
        if((1<a && a<1000000000)&&(1<b && b<100)) {
            int size=a/b;
            HANDLE th[b];
            DWORD thid[b];
            struct D d[b];
            int first=0;
            clock_t clock1=clock();
            for (int i=0;i<b;i++){
               d[i].first=first;
               d[i].size=size;
                first+=size;

            }

           if(a%b!=0){
                d[b-1].size+=a%b;}
            mutex=CreateMutex(NULL,FALSE,NULL);
            //clock

            for(int i=0;i<b;i++){
                th[i]=CreateThread(NULL,0,fun,&d[i],0,&thid[i]);
                }




            for(int i=0;i<b;i++){
                    WaitForSingleObject(th[i],INFINITE);

                    CloseHandle(th[i]);
                }
            clock_t clock2=clock();
            double time=(clock2-clock1)/(double)CLOCKS_PER_SEC;

            clock_t clock3=clock();
            double pi = 0;
            for(double i=0;i<=a;i++){
                pi=pi+(pow((-1),i)/((2*i)+1));
            }
            pi=pi*4;
            clock_t clock4=clock();
            double time2=(clock4-clock3)/(double)CLOCKS_PER_SEC;

            fprintf(stdout,"Z wątkami:%f czas:%.5lf \n",pit*4,time);
            fprintf(stdout,"Bez wątków : %f  czas:%.5lf \n",pi,time2);
        }
    }
}
