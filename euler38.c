#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <string.h>

int asq = 0;
int bsq = 0;
int csq = 0;
int a = 0;
int b = 0;
int c = 0;
int prod = 0;
int index = 0;
int num[9] = {0};
int max = 0;


//has to start with 9 b/c has to be greater than 1 dig, cant be two digits because concatenation would have to have 8 or 11 digits, can't be three digits b/c over limit again. can't be 5 digits as n must be greater than 1. must be 4 digits--n must be equal to 2. can't be over 93...... as that would result in either double 8's or double 9's in solution

int main() {
       for (int a=918273645; a<938765421; a++) { 

        if (checkPan(a) && ((a / 100000) * 2) == (a % 100000)) {
        if (a > max) {
          max = a;
          printf("%d", max);
        }

        }
    } 
    printf("%d", max);
}


int checkPan(int p) {
while (p != 0) {
       num[p % 10] = (num[p % 10]) + (1);
       if (num[p % 10] > 1 || num[0] == 1) {
         //could use for loop but DOESN'T work for whatever reason lol neither does memset!
         num[0] = 0;
         num[1] = 0;
         num[2] = 0;
         num[3] = 0;
         num[4] = 0;
         num[5] = 0;
         num[6] = 0;
         num[7] = 0;
         num[8] = 0;
         num[9] = 0;
         return false;
       }
       p /= 10;
  }
      //same
         num[0] = 0;
         num[1] = 0;
         num[2] = 0;
         num[3] = 0;
         num[4] = 0;
         num[5] = 0;
         num[6] = 0;
         num[7] = 0;
         num[8] = 0;
         num[9] = 0;
    
  return true;
}