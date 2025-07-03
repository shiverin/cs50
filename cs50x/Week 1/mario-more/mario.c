#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height, n;
    do
    {
        height=get_int("Enter a positive integer between 1 and 8 inclusive ");
    }
    while (height<=0 || height >=9);

    for(n=0;n<height;n++)
    {
        for (int space=0; space+n<height-1; space++)
        {printf(" ");
        }

        for (int hash=0; hash<n+1;hash++)
        {printf("#");
        }

        printf("  ");

        for (int hash=0; hash<n+1;hash++)
        {printf("#");
        }

        //for (int space=0; space+n<height-1; space++)
        //{printf(" ");
        //}

        printf("\n");
    }
}
