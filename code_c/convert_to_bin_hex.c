#include "parm.h"
#include "utils.h"
#include "math.h"

void run()
{
    BEGIN();

    int number;
    int choice;

    // Demander à l'utilisateur de saisir un nombre
    PUTCHAR('N','=');
    number = READINT();
    PUTCHAR('\n');

    // Demander à l'utilisateur de choisir la base de conversion
    PUTCHAR('1','2','3');  // Pour indiquer les options disponibles (1, 2, 3)
    PUTCHAR('+','B','H','D'); // Choix entre Binaire (B), Hexadécimal (H), Décimal (D)

    read:
    choice = READKEY();

    // Choisir la base de conversion en fonction du choix de l'utilisateur
    switch(choice) {
        case 'B': {
            // Conversion en binaire
            PUTCHAR('B','=');
            int n = number;
            int bin[32]; // Tableau temporaire pour stocker les bits (max 32 bits pour les entiers)
            int index = 0;

            // Remplir le tableau avec les bits
            while (n > 0) {
                bin[index++] = n % 2;
                n = n / 2;
            }

            // Afficher les bits en ordre inverse
            for (int i = index - 1; i >= 0; i--) {
                PUTCHAR('0' + bin[i]);
            }

            PUTCHAR('\n');
            break;
        }

        case 'H': {
            // Conversion en hexadécimal
            PUTCHAR('H','=');
            int n = number;
            char hex_digits[] = "0123456789ABCDEF";
            char hex[8]; // Tableau pour stocker les caractères hexadécimaux
            int index = 0;

            if (n == 0) {
                PUTCHAR('0');
                PUTCHAR('\n');
                break;
            }

            // Remplir le tableau avec les chiffres hexadécimaux
            while (n > 0) {
                hex[index++] = hex_digits[n % 16];
                n = n / 16;
            }

            // Afficher les caractères hexadécimaux en ordre inverse
            for (int i = index - 1; i >= 0; i--) {
                PUTCHAR(hex[i]);
            }

            PUTCHAR('\n');
            break;
        }

        case 'D': {
            // Afficher le nombre en décimal
            PUTCHAR('D','=');
            PUTCHAR(number + '0');  // Affichage du chiffre décimal
            PUTCHAR('\n');
            break;
        }

        default:
            // Si l'utilisateur entre une touche invalide, redemander
            goto read;
    }

    // Attendre une touche avant de fermer
    WAITKEY();

    RESET();
}
