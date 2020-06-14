#include <stdio.h>
#include <math.h>
#include <time.h>
#include <stdbool.h>
#include <windows.h>

int a = 0;
int othertemp = 0;
int num[9] = {0};
int i = 0;
int temp = 0;

int checkDigits(int b) {
int temp = b;
for (int i = 1; i < 6; i++) {
    while (b != 0) {
       num[b % 10] = (num[b % 10]) + (1);
       if (num[b%10] != 0 && num[b%10] != i) {
           for (int i = 0; i <= 9; i++) { 
            num[i] = 0;
            }
           return false;
       }
       b /= 10;
  }
    othertemp = temp * (i  + 1);
    b = othertemp;
}
return true;
}

int main() {
    long start_time, end_time, elapsed;
    start_time = clock();
    for (a=125874; a<170000; a++) {
    if (checkDigits(a)) {
        end_time = clock();
        elapsed = (end_time - start_time);
        printf("%d", a);
        printf("%d", elapsed);
        return a;
    };      
}
}

    
    