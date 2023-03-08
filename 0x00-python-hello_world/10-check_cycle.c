#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 *
 * @list: pointer to head of list
 * Return: 0 if list has a cycle. Otherwise 1
*/
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (!list || !list->next)
		return (0);

	temp = list;
	while (temp->next)
	{
		if (temp->next->n == list->n)
			return (1);
		temp = temp->next;
	}
	return (0);
}
