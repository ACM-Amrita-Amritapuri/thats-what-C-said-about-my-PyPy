#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>


 
 int main(int argc, string argv[])
 {

    if (argc != 2)
    {
        printf("Usage: ./caesar key");
        return 1;
    }
    

    int k = atoi(argv[1]);

    
    if (k < 0)
    {
        printf("Usage: ./caesar key");
        return 1;
    }
    else
    {
 
        string plaintext = GetString();
        
        for (int i = 0, i < strlen(plaintext); i++)
            {

                if islower(plaintext[i])
                {
                    printf("%c", (((plaintext[i] + k) - 97) % 26) + 97);
                }
                
                else if isupper(plaintext[i])
                {
                    printf("%c", (((plaintext[i] + k) - 65) % 26) + 65);
                }

                else
                {
                    printf("%c", plaintext[i]);
                }
                
            }
            printf("\n");
            return 0;
    }
 }