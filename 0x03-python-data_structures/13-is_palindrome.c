#include "lists.h"
#include <stddef.h>
/**
 * pali - checks if palindrome
 * @h: head
 * @head: pointer to head
 * Return: 1 if palindrome 0 otherwise
 */
int pali(listint_t **h, listint_t *head)
{
	int res;

	if (head != NULL)
	{
		res = pali(h, head->next);
		if (res != 0)
		{
			res = (head->n == (*h)->n);
			*h = (*h)->next;
			return (res);
		}
		return (0);
	}
	return (1);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: head
 * Return: 0 if it is not a palindrome, 1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (!head)
		return (0);
	return (pali(head, *head));
}
