#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int j = 0;
    char *stringname = (char *) malloc(sizeof(char) * 8);
    FILE *temp;
    bool first = true;
    if (argc != 2)
    {
        printf("Usage: ./recover file\n");
        return 1;
    }
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    uint8_t buffer[512];

    while (fread(buffer, 1, 512, card) == 512)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            if (first == true)
            {
                sprintf(stringname, "%03i.jpg", j);
                temp = fopen(stringname, "w");
                first = false;
            }
            else
            {
                fclose(temp);
                j++;
                sprintf(stringname, "%03i.jpg", j);
                temp = fopen(stringname, "w");
            }
        }
        if (first == false)
        {
            fwrite(buffer, 1, 512, temp);
        }
    }
    free(stringname);
    fclose(temp);
    fclose(card);
}
