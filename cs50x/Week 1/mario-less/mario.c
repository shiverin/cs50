#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Height: ");
    }

    while (n < 1 || n > 8);
    for (int h = 0; h < n; h++)
    {
        for (int space = 0; space + h < n - 1; space++)
        {
            printf(" ");
        }
        for (int line = 0; line < h + 1; line++)
        {
            printf("#");
        }

        printf("\n");
    }
}
