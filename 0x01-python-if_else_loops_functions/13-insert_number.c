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
  listint_t **new = NULL;

  old = head;
  new = malloc(sizeof(listint_t));
  if (new == NULL)
    return (NULL);
  new->n = number;
  new->next = NULL;
  if (*head == NULL || new->n < old->n)
    {
      new->next = *head;
      *head = new;
      return (new);
    }
  while (old->next != NULL && new->n < old->n &&
         new->n <(old->next)->n)
    old = old->next;
  new->next = old->next;
  old->next = new;
  return (new);
}
