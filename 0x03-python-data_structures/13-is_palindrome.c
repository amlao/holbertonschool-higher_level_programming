#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head of a list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
        int counter = 0;
        int len = 0;
        int *new;
        listint_t *tmp;

        if (!head)
                return (1);
        tmp = *head;
        for (; tmp; len++)
                tmp = tmp->next;
        tmp = *head;
        new = malloc(sizeof(int) * len);
        while (tmp)
        {
                new[counter] = tmp->n;
                counter++;
                tmp = tmp->next;
        }
        for (counter = 0; counter < len / 2; counter++)
        {
                if (new[counter] != new[len - 1 -counter])
                {
                        free(new);
                        return (0);
                }
        }
        free(new);
        return (1);
}
