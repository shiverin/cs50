#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int cash, a, b, c, d, e;
    a = 0;
    b = 0;
    c = 0;
    d = 0;

    do
    {
        cash = get_int("Change owed: ");
    }
    while (cash <= 0);

    while (cash >= 25)
    {
        cash = cash - 25;
        a = a + 1;
    }
    // while (cash>=25);
    // printf("%i", a);
    // printf("%i", cash);

    while (cash >= 10)
    {
        cash = cash - 10;
        b = b + 1;
    }
    // printf("%i", b);

    while (cash >= 5)
    {
        cash = cash - 5;
        c = c + 1;
    }

    while (cash >= 1)
    {
        cash = cash - 1;
        d = d + 1;
    }

    // printf("%i%i%i%i",a,b,c,d);
    e = a + b + c + d;
    printf("%i\n", e);
}
