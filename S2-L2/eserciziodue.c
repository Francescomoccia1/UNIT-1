#include <stdio.h>

int main(){
int numero1, numero2; 
int media;

printf("Inserisci il primo numero:");
scanf("%d", &numero1);

printf("Inserisci il secondo numero:");
scanf("%d", &numero2);

media = (numero1 + numero2)/2;

printf("La media è: %d\n", media);

return 0;
}

