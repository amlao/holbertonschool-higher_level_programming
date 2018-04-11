#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: start of the list
 * @number: number to insert
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *old = NULL;
  listint_t *new = NULL;
  listint_t *current = NULL;

  if (!head)
    return (NULL);
  new = malloc(sizeof(listint_t));
  if (!new)
    return (NULL);
  new->n = number;
  old = NULL;
  for (current = *head; current && current->n < number;)
    {
      old = current;
      current = current->next;
    }
  new->next = current;
  if (old)
    old->next = new;
  else
    *head = new;
  return (new);
}
