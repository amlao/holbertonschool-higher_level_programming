#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: start of the list
 * @number: number to insert
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
  listint_t *old;
  listint_t **new;

  if !head
    return (NULL);
  new = malloc(sizeof(listint_t));
  if !new
    return (NULL);

}
