#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    float letters = 0;
    float words = 1;
    float sentences = 0;
    // string a="Would you like them here or there? I would not like them here or there. I would not
    // like them anywhere."; (Grade 2)
    string a = get_string("Text: ");
    int len = strlen(a);
    for (int n = 0; n < len; n++)
    {
        char c = a[n];
        if (isalpha(c))
        {
            letters++;
        }
        else if (c == ' ')
        {
            words++;
        }
        else if (c == '!' || c == '.' || c == '?')
        {
            sentences++;
        }
    }
    // printf("%i\n%i\n%i\n",letters, words,sentences);

    float L = (letters / (words / 100));
    // printf("%f\n", L);
    float S = (sentences / (words / 100));
    // printf("%f\n%f\n", L,S);
    float end = (0.0588 * L) - (0.296 * S) - 15.8;
    int index = round(end);
    // printf("%i\n",index);
    if (index <= 16 && index >= 1)
    {
        printf("Grade %i\n", index);
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade 16+\n");
    }
}
