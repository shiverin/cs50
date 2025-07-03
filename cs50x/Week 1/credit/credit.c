#include <cs50.h>
#include <stdio.h>

int process(int lul)
{
    int result;
    int num = lul * 2;
    if (num >= 10)
    {
        result = (num / 10) + (num % 10);
    }
    else
    {
        result = num;
    }
    // printf("%i\n",result);
    return result;
}
int main(void)
{
    long credit, c;
    int n, a, b, x;
    int a1, a2, a3, a4, a5, a6, a7, a8;
    int b1, b2, b3, b4, b5, b6, b7, b8;
    int z = 0;

    credit = get_long("Number: ");
    // credit=378282246310005;
    // 378282246310005
    c = credit;
    x = 0;

    while (c > 0)
    {
        c = c / 10;
        x++;
    }
    while ((x == 13 || x == 14 || x == 15 || x == 16) && (z == 0))
    {

        if (x == 13)
        {
            a = credit / 1000000000000;
            b = credit / 100000000000;
        }
        else if (x == 15)
        {
            a = credit / 100000000000000;
            b = credit / 10000000000000;
        }
        else
        {
            a = credit / 1000000000000000;
            b = credit / 100000000000000;
        }
        // printf("%i",x);

        // printf("%i%i", a, b);
        // printf("%i", b);
        /*if (a==4)
        {printf("Visa\n");
        }

        if (b==34||b==37)
        {printf("Amex\n");
        }
        if (b==51||b==52||b==53||b==54||b==55)
        {printf("Mastercard\n");
        }*/

        a1 = (credit / 10) % 10;
        a2 = (credit / 1000) % 10;
        a3 = (credit / 100000) % 10;
        a4 = (credit / 10000000) % 10;
        a5 = (credit / 1000000000) % 10;
        a6 = (credit / 100000000000) % 10;
        a7 = (credit / 10000000000000) % 10;
        a8 = (credit / 1000000000000000) % 10;
        /*printf("%i\n",a1);
        printf("%i\n",a2);
        printf("%i\n",a3);
        printf("%i\n",a4);
        printf("%i\n",a5);
        printf("%i\n",a6);
        printf("%i\n",a7);
        printf("%i\n",a8);*/

        b1 = (credit) % 10;
        b2 = (credit / 100) % 10;
        b3 = (credit / 10000) % 10;
        b4 = (credit / 1000000) % 10;
        b5 = (credit / 100000000) % 10;
        b6 = (credit / 10000000000) % 10;
        b7 = (credit / 1000000000000) % 10;
        b8 = (credit / 100000000000000) % 10;

        z = z + 1;
    }
    int alpha = (process(a1) + process(a2) + process(a3) + process(a4) + process(a5) + process(a6) +
                 process(a7) + process(a8));
    int beta = (b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8);
    int final = (alpha + beta);
    // printf("%i",final);

    if ((a == 4) && (final % 10 == 0) && (x == 13 || x == 16))
    {
        printf("VISA\n");
    }

    else if ((b == 34 || b == 37) && (final % 10 == 0) && (x == 15))
    {
        printf("AMEX\n");
    }
    else if ((b == 51 || b == 52 || b == 53 || b == 54 || b == 55) && (final % 10 == 0) &&
             (x == 16))
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
