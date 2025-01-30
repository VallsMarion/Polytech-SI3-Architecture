#include "parm.h"
#include "stdio.h"

#define N   DIP1

void run()
{
    BEGIN();

    int a = 0;      // Premier terme de Fibonacci
    int b = 1;      // Deuxième terme de Fibonacci
    int temp;
    int count = 0;  // Compteur pour afficher les termes
    int max = N;    // Nombre de termes à afficher (réglé par N)

    RES = N;

    PUTCHAR('P','r','o','j','e','t',' ','P','A','R','M', ' ', 'F','i','b','o','n','a','c','c','i', '\n');

    while (count < max)
    {
            RES = a;     // Affiche le terme courant
            count++;     // Incrémente le compteur
            temp = a;
            a = b;
            b = temp + b; // Mise à jour de a et b pour le prochain terme

    }

    END();
}
