#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: 0 if there's no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
  listint_t *one = list;
  listint_t *two = list;

  if (!list)
    return (0);

  while (one != NULL && two != NULL)
    {
      one = one->next;
      if (one == NULL)
	return (0);

      one = one->next;
      two = two->next;
      if (one == two)
	return (1);
    }
  return (0);
}
