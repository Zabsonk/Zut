//SO IS1 212B LAB13
//Kacper Żabiński
//zk51162@zut.edu.pl
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>
#include <process.h>

#define MAX 12

char board[MAX];

void print_board() {
int i;
for (i = 1; i < 10; i++) {
if (i % 3 == 0)
printf(" %c ", board[i]);
else
printf(" %c |", board[i]);
if (i % 3 == 0 && i != 9)
printf("\n---+---+---\n");
else if (i == 9)
printf("\n");
}
}

void pick(char player) {
printf("Wykonaj ruch: ");
int move;
scanf("%d", &move);
if (move < 0 || move > 9) {
pick(player);
} else {
if (board[move] != 'o' && board[move] != 'x') {
board[move] = player;
if (board[12] == 'o')
board[12] = 'x';
else
board[12] = 'o';
} else {
printf("To pole jest zajete!\n");
pick(player);
}
}
printf("\n");
print_board();
}

void check(char player) {
char winner;
int win = 0;
if (board[1] == board[2] && board[2] == board[3]) {
winner = board[1];
win = 1;
} else if (board[4] == board[5] && board[5] == board[6]) {
winner = board[4];
win = 1;
} else if (board[4] == board[5] && board[5] == board[6]) {
winner = board[4];
win = 1;
} else if (board[1] == board[4] && board[4] == board[7]) {
winner = board[1];
win = 1;
} else if (board[2] == board[5] && board[5] == board[8]) {
winner = board[2];
win = 1;
} else if (board[3] == board[6] && board[6] == board[9]) {
winner = board[3];
win = 1;
} else if (board[3] == board[5] && board[5] == board[7]) {
winner = board[3];
win = 1;
} else if (board[1] == board[5] && board[5] == board[9]) {
winner = board[1];
win = 1;
}

if (win == 1) {
if (player == winner)