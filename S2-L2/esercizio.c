#include <stdio.h>

main(){
   int primo_numero;
   int secondo_numero;
   int risultato;

   printf("Inserisci il primo numero:\n");
   scanf("%d", &primo_numero);

printf("Inserisci il secondo numero:\n");
scanf("%d", &secondo_numero);

risultato = primo_numero*secondo_numero;

printf("Il risultato della moltiplicazione è: %d\n", risultato);

return 0;
}