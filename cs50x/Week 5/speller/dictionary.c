// Implements a dictionary's functionality

#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
int count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    node *cur;
    // TODO
    int x = hash(word);
    if (table[x] == NULL)
    {
        return false;
    }
    else
    {
        cur = table[x];
        while (cur != NULL)
        {
            if (strcasecmp(cur->word, word) == 0)
            {
                return true;
            }
            cur = cur->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
    // can add return the other digits
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    char string[LENGTH + 1];
    bool hehe = false;
    // TODO
    FILE *source = fopen(dictionary, "r");
    if (source == NULL)
    {
        return false;
    }

    while (fscanf(source, "%s", string) != EOF)
    {
        node *ptr = malloc(sizeof(node));
        if (ptr == NULL)
        {
            fclose(source);
            return false;
        }
        strcpy(ptr->word, string);
        ptr->next = NULL;
        int k = hash(string);
        // printf("%i", k);
        if (table[k] == NULL)
        {

            table[k] = ptr;
        }
        else
        {
            ptr->next = table[k];
            table[k] = ptr;
        }
        count++;
    }
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    int y = 0;
    node *temp;
    node *curr;
    while (y < 26)
    {
        if (table[y] != NULL)
        {
            curr = table[y];
            while (curr != NULL)
            {
                temp = curr;
                curr = curr->next;
                free(temp);
            }
        }
        y++;
    }
    while (y < 26)
    {
        if (table[y] != NULL)
        {
            return false;
        }
        y++;
    }
    return true;
}
