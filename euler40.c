#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>

int num[7] = {0};

void SieveOfEratosthenes(int n) 
{
    static bool prime[7654321]; 
    memset(prime, true, sizeof(prime)); 
    for (int p=2; p*p<=n; p++) 
    { 
        if (prime[p] == true) 
        { 
            for (int i=p*p; i<=n; i += p) 
                prime[i] = false; 
        } 
    } 
  
    for (int p=7654321; p>1234567; p-=2) {
       if (checkPan(p) && prime[p]) { 
        printf("%d", p);
        break;
    }
}
}
int main(int p) {
    SieveOfEratosthenes(7654321);
}

int checkPan(int p) {
while (p != 0) {
       if (p%10 == 9 || p % 10 == 8) {
         return false;
       }
       num[p % 10] = (num[p % 10]) + (1);
       if (num[p % 10] > 1 || num[0] == 1) {
         for (int i = 0; i <= 7; i++) { 
         num[i] = 0;
         }
         return false;
       }
       p /= 10;
  }

      for (int i = 1; i <= 7; i++) { 
         if (num[i] == 0) {
             return false;
         }
         }

  return true;
}