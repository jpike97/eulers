#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>

int count = 0;

void SieveOfEratosthenes(int n) 
{
    bool prime[n+1]; 
    memset(prime, true, sizeof(prime)); 
    for (int p=2; p*p<=n; p++) 
    { 
        if (prime[p] == true) 
        { 
            for (int i=p*p; i<=n; i += p) 
                prime[i] = false; 
        } 
    } 

  
    for (int p=56003; p<56009; p+=2) {
       if (prime[p]) { 
        checkCombos(p);
    }
}
}

int checkCombos(int k) { 
    while(count < 10) {
        
    }
}


int main(int p) {
    SieveOfEratosthenes(60000);
}
