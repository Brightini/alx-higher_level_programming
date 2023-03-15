#include "lists.h"

/**
 * is_palindrome - checks if a singly-linked list is a palindrome
 *
 * @head: pointer to address of first node on the list
 * Return: 1 if list is a palindrome, otherwise 0
*/
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int list_len = 0;

	if (!*head)
		return (1);

	temp = *head;
	while (temp)
	{
		list_len++;
		temp = temp->next;
	}
	if (list_len % 2 != 0)
		return (0);

	return (1);
}
