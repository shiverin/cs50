#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int check(string k);
char output(char x, string argv);
int main(int argc, string argv[])
{
    while (argc == 2)
    {
        if (check(argv[1]) == 0)
        {
            string a = get_string("plaintext: ");
            int len = strlen(a);
            printf("ciphertext: ");
            for (int g = 0; g < len; g++)
            {
                output(a[g], argv[1]);
            }
            printf("\n");
            return 0;
        }
        else
        {
            break;
        }
    }
    // else
    //{
    printf("Error\n");
    return 1;
    //}
}

int check(string k)
{
    int alpha = 0;
    int repeat = 0;
    string key = k;
    int length = strlen(key);
    for (int i = 0; i < length; i++)
    {
        char c = key[i];
        if (isalpha(c))
        {
            alpha++;
        }
        // char z=key[i];
        char z = toupper(c);
        for (int e = 0; e < length; e++)
        {
            char f = key[e];
            // printf("%c%c\n",z,f);
            if (z == toupper(f))
            {
                // printf("%c\n",z);
                repeat++;
            }
        }
    }
    // printf("%i%i%i\n",length,repeat,alpha);
    if (length == 26 && repeat == 26 && alpha == 26)
    {
        // string a=get_string("plaintext: ");
        return 0;
    }
    else
    {
        return 1;
    }
}
char output(char x, string argv)
{
    if (x == 'A')
    {
        printf("%c", toupper(argv[0]));
        return 0;
    }
    else if (x == 'a')
    {
        printf("%c", tolower(argv[0]));
        return 0;
    }
    else if (x == 'B')
    {
        printf("%c", toupper(argv[1]));
        return 0;
    }
    else if (x == 'b')
    {
        printf("%c", tolower(argv[1]));
        return 0;
    }
    else if (x == 'C')
    {
        printf("%c", toupper(argv[2]));
        return 0;
    }
    else if (x == 'c')
    {
        printf("%c", tolower(argv[2]));
        return 0;
    }
    else if (x == 'D')
    {
        printf("%c", toupper(argv[3]));
        return 0;
    }
    else if (x == 'd')
    {
        printf("%c", tolower(argv[3]));
        return 0;
    }
    else if (x == 'E')
    {
        printf("%c", toupper(argv[4]));
        return 0;
    }
    else if (x == 'e')
    {
        printf("%c", tolower(argv[4]));
        return 0;
    }
    else if (x == 'F')
    {
        printf("%c", toupper(argv[5]));
        return 0;
    }
    else if (x == 'f')
    {
        printf("%c", tolower(argv[5]));
        return 0;
    }
    else if (x == 'G')
    {
        printf("%c", toupper(argv[6]));
        return 0;
    }
    else if (x == 'g')
    {
        printf("%c", tolower(argv[6]));
        return 0;
    }
    else if (x == 'H')
    {
        printf("%c", toupper(argv[7]));
        return 0;
    }
    else if (x == 'h')
    {
        printf("%c", tolower(argv[7]));
        return 0;
    }
    else if (x == 'I')
    {
        printf("%c", toupper(argv[8]));
        return 0;
    }
    else if (x == 'i')
    {
        printf("%c", tolower(argv[8]));
        return 0;
    }
    else if (x == 'J')
    {
        printf("%c", toupper(argv[9]));
        return 0;
    }
    else if (x == 'j')
    {
        printf("%c", tolower(argv[9]));
        return 0;
    }
    else if (x == 'K')
    {
        printf("%c", toupper(argv[10]));
        return 0;
    }
    else if (x == 'k')
    {
        printf("%c", tolower(argv[10]));
        return 0;
    }
    else if (x == 'L')
    {
        printf("%c", toupper(argv[11]));
        return 0;
    }
    else if (x == 'l')
    {
        printf("%c", tolower(argv[11]));
        return 0;
    }
    else if (x == 'M')
    {
        printf("%c", toupper(argv[12]));
        return 0;
    }
    else if (x == 'm')
    {
        printf("%c", tolower(argv[12]));
        return 0;
    }
    else if (x == 'N')
    {
        printf("%c", toupper(argv[13]));
        return 0;
    }
    else if (x == 'n')
    {
        printf("%c", tolower(argv[13]));
        return 0;
    }
    else if (x == 'O')
    {
        printf("%c", toupper(argv[14]));
        return 0;
    }
    else if (x == 'o')
    {
        printf("%c", tolower(argv[14]));
        return 0;
    }
    else if (x == 'P')
    {
        printf("%c", toupper(argv[15]));
        return 0;
    }
    else if (x == 'p')
    {
        printf("%c", tolower(argv[15]));
        return 0;
    }
    else if (x == 'Q')
    {
        printf("%c", toupper(argv[16]));
        return 0;
    }
    else if (x == 'q')
    {
        printf("%c", tolower(argv[16]));
        return 0;
    }
    else if (x == 'R')
    {
        printf("%c", toupper(argv[17]));
        return 0;
    }
    else if (x == 'r')
    {
        printf("%c", tolower(argv[17]));
        return 0;
    }
    else if (x == 'S')
    {
        printf("%c", toupper(argv[18]));
        return 0;
    }
    else if (x == 's')
    {
        printf("%c", tolower(argv[18]));
        return 0;
    }
    else if (x == 'T')
    {
        printf("%c", toupper(argv[19]));
        return 0;
    }
    else if (x == 't')
    {
        printf("%c", tolower(argv[19]));
        return 0;
    }
    else if (x == 'U')
    {
        printf("%c", toupper(argv[20]));
        return 0;
    }
    else if (x == 'u')
    {
        printf("%c", tolower(argv[20]));
        return 0;
    }
    else if (x == 'V')
    {
        printf("%c", toupper(argv[21]));
        return 0;
    }
    else if (x == 'v')
    {
        printf("%c", tolower(argv[21]));
        return 0;
    }
    else if (x == 'W')
    {
        printf("%c", toupper(argv[22]));
        return 0;
    }
    else if (x == 'w')
    {
        printf("%c", tolower(argv[22]));
        return 0;
    }
    else if (x == 'X')
    {
        printf("%c", toupper(argv[23]));
        return 0;
    }
    else if (x == 'x')
    {
        printf("%c", tolower(argv[23]));
        return 0;
    }
    else if (x == 'Y')
    {
        printf("%c", toupper(argv[24]));
        return 0;
    }
    else if (x == 'y')
    {
        printf("%c", tolower(argv[24]));
        return 0;
    }
    else if (x == 'Z')
    {
        printf("%c", toupper(argv[25]));
        return 0;
    }
    else if (x == 'z')
    {
        printf("%c", tolower(argv[25]));
        return 0;
    }
    else
    {
        printf("%c", x);
        return 0;
    }
}
