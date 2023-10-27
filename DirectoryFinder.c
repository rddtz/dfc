#include <stdio.h>

//Script: DCF
//Objective: C Script to find hidden directory in web-aplications
//Use: 'dfc WordlistPath URL' or 'dfc WordlistPath URL/here'
//Options: -a "Append commun extensions such as .txt, .php after the first try, (may be slower than the normal list)"
//         -f "Filter the wanted response codes"
//         -o "Filter out the unwanted response codes and show all others, defalut -o 404"

int main(int argc, char **argv){

    char url[50];
    char wordlist[50];

    printf("\nWordlist Path: ");
    scanf("%s", &wordlist);


    printf("\nURL: %s \nWordlist Path: %s\n", url, wordlist);

    return 0;
}
