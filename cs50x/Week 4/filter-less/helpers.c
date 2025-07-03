#include "helpers.h"
#include <math.h>
#include <stdlib.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    float b;
    float g;
    float r;
    int z;
    for (int i = 0; i < height; i++)
    {
        for (int n = 0; n < width; n++)
        {
            b = image[i][n].rgbtBlue;
            g = image[i][n].rgbtGreen;
            r = image[i][n].rgbtRed;
            z = round((b + g + r) / 3);

            image[i][n].rgbtBlue = z;
            image[i][n].rgbtGreen = z;
            image[i][n].rgbtRed = z;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    float b;
    float g;
    float r;
    for (int i = 0; i < height; i++)
    {
        for (int n = 0; n < width; n++)
        {
            b = image[i][n].rgbtBlue;
            g = image[i][n].rgbtGreen;
            r = image[i][n].rgbtRed;
            if (round(.272 * r + .534 * g + .131 * b) > 255)
            {
                image[i][n].rgbtBlue = 255;
            }
            else
            {
                image[i][n].rgbtBlue = round(.272 * r + .534 * g + .131 * b);
            }
            if (round(.349 * r + .686 * g + .168 * b) > 255)
            {
                image[i][n].rgbtGreen = 255;
            }
            else
            {
                image[i][n].rgbtGreen = round(.349 * r + .686 * g + .168 * b);
            }
            if (round(.393 * r + .769 * g + .189 * b) > 255)
            {
                image[i][n].rgbtRed = 255;
            }
            else
            {
                image[i][n].rgbtRed = round(.393 * r + .769 * g + .189 * b);
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int a = ceil(width / 2);
    int temp = 0;
    for (int i = 0; i < height; i++)
    {
        for (int n = 0; n < a; n++)
        {
            temp = image[i][n].rgbtBlue;
            image[i][n].rgbtBlue = image[i][width - n - 1].rgbtBlue;
            image[i][width - n - 1].rgbtBlue = temp;

            temp = image[i][n].rgbtGreen;
            image[i][n].rgbtGreen = image[i][width - n - 1].rgbtGreen;
            image[i][width - n - 1].rgbtGreen = temp;

            temp = image[i][n].rgbtRed;
            image[i][n].rgbtRed = image[i][width - n - 1].rgbtRed;
            image[i][width - n - 1].rgbtRed = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int c = (width - 1);
    int d = (height - 1);
    RGBTRIPLE newimage[height][width];

    for (int i = 0; i < height; i++)
    {
        for (int n = 0; n < width; n++)
        {
            if (i == 0 && n == 0) // passed
            {
                newimage[i][n].rgbtBlue =
                    round((image[i][n].rgbtBlue + image[i][n + 1].rgbtBlue +
                           image[i + 1][n].rgbtBlue + image[i + 1][n + 1].rgbtBlue) /
                          4.0);
                newimage[i][n].rgbtGreen =
                    round((image[i][n].rgbtGreen + image[i][n + 1].rgbtGreen +
                           image[i + 1][n].rgbtGreen + image[i + 1][n + 1].rgbtGreen) /
                          4.0);
                newimage[i][n].rgbtRed =
                    round((image[i][n].rgbtRed + image[i][n + 1].rgbtRed + image[i + 1][n].rgbtRed +
                           image[i + 1][n + 1].rgbtRed) /
                          4.0);
            }
            else if (i == 0 && n == c)
            {
                newimage[i][n].rgbtBlue =
                    round((image[i][n].rgbtBlue + image[i][n - 1].rgbtBlue +
                           image[i + 1][n].rgbtBlue + image[i + 1][n - 1].rgbtBlue) /
                          4.0);
                newimage[i][n].rgbtGreen =
                    round((image[i][n].rgbtGreen + image[i][n - 1].rgbtGreen +
                           image[i + 1][n].rgbtGreen + image[i + 1][n - 1].rgbtGreen) /
                          4.0);
                newimage[i][n].rgbtRed =
                    round((image[i][n].rgbtRed + image[i][n - 1].rgbtRed + image[i + 1][n].rgbtRed +
                           image[i + 1][n - 1].rgbtRed) /
                          4.0);
            }
            else if (i == d && n == 0)
            {
                newimage[i][n].rgbtBlue =
                    round((image[i][n].rgbtBlue + image[i - 1][n].rgbtBlue +
                           image[i][n + 1].rgbtBlue + image[i - 1][n + 1].rgbtBlue) /
                          4.0);
                newimage[i][n].rgbtGreen =
                    round((image[i][n].rgbtGreen + image[i - 1][n].rgbtGreen +
                           image[i][n + 1].rgbtGreen + image[i - 1][n + 1].rgbtGreen) /
                          4.0);
                newimage[i][n].rgbtRed =
                    round((image[i][n].rgbtRed + image[i - 1][n].rgbtRed + image[i][n + 1].rgbtRed +
                           image[i - 1][n + 1].rgbtRed) /
                          4.0);
            }
            else if (i == d && n == c)
            {
                newimage[i][n].rgbtBlue =
                    round((image[i][n].rgbtBlue + image[i - 1][n].rgbtBlue +
                           image[i][n - 1].rgbtBlue + image[i - 1][n - 1].rgbtBlue) /
                          4.0);
                newimage[i][n].rgbtGreen =
                    round((image[i][n].rgbtGreen + image[i - 1][n].rgbtGreen +
                           image[i][n - 1].rgbtGreen + image[i - 1][n - 1].rgbtGreen) /
                          4.0);
                newimage[i][n].rgbtRed =
                    round((image[i][n].rgbtRed + image[i - 1][n].rgbtRed + image[i][n - 1].rgbtRed +
                           image[i - 1][n - 1].rgbtRed) /
                          4.0);
            }
            else if (i == 0)
            {
                newimage[i][n].rgbtBlue =
                    round((image[i][n].rgbtBlue + image[i][n - 1].rgbtBlue +
                           image[i + 1][n - 1].rgbtBlue + image[i + 1][n].rgbtBlue +
                           image[i + 1][n + 1].rgbtBlue + image[i][n + 1].rgbtBlue) /
                          6.0);
                newimage[i][n].rgbtGreen =
                    round((image[i][n].rgbtGreen + image[i][n - 1].rgbtGreen +
                           image[i + 1][n - 1].rgbtGreen + image[i + 1][n].rgbtGreen +
                           image[i + 1][n + 1].rgbtGreen + image[i][n + 1].rgbtGreen) /
                          6.0);
                newimage[i][n].rgbtRed =
                    round((image[i][n].rgbtRed + image[i][n - 1].rgbtRed +
                           image[i + 1][n - 1].rgbtRed + image[i + 1][n].rgbtRed +
                           image[i + 1][n + 1].rgbtRed + image[i][n + 1].rgbtRed) /
                          6.0);
            }
            else if (i == d)
            {
                newimage[i][n].rgbtBlue =
                    round((image[i][n].rgbtBlue + image[i][n - 1].rgbtBlue +
                           image[i - 1][n - 1].rgbtBlue + image[i - 1][n].rgbtBlue +
                           image[i - 1][n + 1].rgbtBlue + image[i][n + 1].rgbtBlue) /
                          6.0);
                newimage[i][n].rgbtGreen =
                    round((image[i][n].rgbtGreen + image[i][n - 1].rgbtGreen +
                           image[i - 1][n - 1].rgbtGreen + image[i - 1][n].rgbtGreen +
                           image[i - 1][n + 1].rgbtGreen + image[i][n + 1].rgbtGreen) /
                          6.0);
                newimage[i][n].rgbtRed =
                    round((image[i][n].rgbtRed + image[i][n - 1].rgbtRed +
                           image[i - 1][n - 1].rgbtRed + image[i - 1][n].rgbtRed +
                           image[i - 1][n + 1].rgbtRed + image[i][n + 1].rgbtRed) /
                          6.0);
            }
            else if (n == 0)
            {
                newimage[i][n].rgbtBlue =
                    round((image[i][n].rgbtBlue + image[i - 1][n].rgbtBlue +
                           image[i - 1][n + 1].rgbtBlue + image[i][n + 1].rgbtBlue +
                           image[i + 1][n + 1].rgbtBlue + image[i + 1][n].rgbtBlue) /
                          6.0);
                newimage[i][n].rgbtGreen =
                    round((image[i][n].rgbtGreen + image[i - 1][n].rgbtGreen +
                           image[i - 1][n + 1].rgbtGreen + image[i][n + 1].rgbtGreen +
                           image[i + 1][n + 1].rgbtGreen + image[i + 1][n].rgbtGreen) /
                          6.0);
                newimage[i][n].rgbtRed =
                    round((image[i][n].rgbtRed + image[i - 1][n].rgbtRed +
                           image[i - 1][n + 1].rgbtRed + image[i][n + 1].rgbtRed +
                           image[i + 1][n + 1].rgbtRed + image[i + 1][n].rgbtRed) /
                          6.0);
            }
            else if (n == c)
            {
                newimage[i][n].rgbtBlue =
                    round((image[i][n].rgbtBlue + image[i - 1][n].rgbtBlue +
                           image[i - 1][n - 1].rgbtBlue + image[i][n - 1].rgbtBlue +
                           image[i + 1][n - 1].rgbtBlue + image[i + 1][n].rgbtBlue) /
                          6.0);
                newimage[i][n].rgbtGreen =
                    round((image[i][n].rgbtGreen + image[i - 1][n].rgbtGreen +
                           image[i - 1][n - 1].rgbtGreen + image[i][n - 1].rgbtGreen +
                           image[i + 1][n - 1].rgbtGreen + image[i + 1][n].rgbtGreen) /
                          6.0);
                newimage[i][n].rgbtRed =
                    round((image[i][n].rgbtRed + image[i - 1][n].rgbtRed +
                           image[i - 1][n - 1].rgbtRed + image[i][n - 1].rgbtRed +
                           image[i + 1][n - 1].rgbtRed + image[i + 1][n].rgbtRed) /
                          6.0);
            }
            else
            {
                newimage[i][n].rgbtBlue =
                    round((image[i][n].rgbtBlue + image[i - 1][n].rgbtBlue +
                           image[i - 1][n - 1].rgbtBlue + image[i][n - 1].rgbtBlue +
                           image[i + 1][n - 1].rgbtBlue + image[i + 1][n].rgbtBlue +
                           image[i + 1][n + 1].rgbtBlue + image[i][n + 1].rgbtBlue +
                           image[i - 1][n + 1].rgbtBlue) /
                          9.0);
                newimage[i][n].rgbtGreen =
                    round((image[i][n].rgbtGreen + image[i - 1][n].rgbtGreen +
                           image[i - 1][n - 1].rgbtGreen + image[i][n - 1].rgbtGreen +
                           image[i + 1][n - 1].rgbtGreen + image[i + 1][n].rgbtGreen +
                           image[i + 1][n + 1].rgbtGreen + image[i][n + 1].rgbtGreen +
                           image[i - 1][n + 1].rgbtGreen) /
                          9.0);
                newimage[i][n].rgbtRed = round(
                    (image[i][n].rgbtRed + image[i - 1][n].rgbtRed + image[i - 1][n - 1].rgbtRed +
                     image[i][n - 1].rgbtRed + image[i + 1][n - 1].rgbtRed +
                     image[i + 1][n].rgbtRed + image[i + 1][n + 1].rgbtRed +
                     image[i][n + 1].rgbtRed + image[i - 1][n + 1].rgbtRed) /
                    9.0);
            }
        }
    }
    for (int a = 0; a < height; a++)
    {
        for (int b = 0; b < width; b++)
        {
            image[a][b] = newimage[a][b];
        }
    }
    return;
}
