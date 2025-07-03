#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int upper(string z);
int points(char c);
int main(void)
{
    int c;
    int final = 0;

    string a = (get_string("PLayer 1: "));
    // string a="drawing";
    // string b="illustration";
    string b = (get_string("PLayer 2: "));

    int alpha = (upper(a));
    int beta = (upper(b));
    if (alpha > beta)
    {
        printf("Player 1 wins!");
    }
    else if (alpha < beta)
    {
        printf("Player 2 wins!");
    }
    else
    {
        printf("Tie!");
    }
    // string A= toupper(a);
    // string B= toupper(b);
}

int upper(string z)
{
    int c;
    int final = 0;
    int len = strlen(z);
    for (int i = 0; i < len; i++)
    {
        int e = i;
        if (islower(z[e]))
        {
            c = toupper(z[e]);
        }
        else
            c = z[e];
        final += points(c);
        // printf("%i\n",final);
    }
    // printf("%i\n", final);
    return final;
}

int points(char c)
{
    // printf("%c", c);
    if (c == 'A' || c == 'E' || c == 'I' || c == 'L' || c == 'N' || c == 'O' || c == 'R' ||
        c == 'S' || c == 'T' || c == 'U')
    {
        return 1;
    }
    else if (c == 'D' || c == 'G')
    {
        return 2;
    }
    else if (c == 'B' || c == 'C' || c == 'M' || c == 'P')
    {
        return 3;
    }
    else if (c == 'F' || c == 'H' || c == 'V' || c == 'W' || c == 'Y')
    {
        return 4;
    }
    else if (c == ('K'))
    {
        return 5;
    }
    else if (c == 'J' || c == 'X')
    {
        return 8;
    }
    else if (c == 'Q' || c == 'Z')
    {
        return 10;
    }
    else
    {
        return 0;
    }
}
