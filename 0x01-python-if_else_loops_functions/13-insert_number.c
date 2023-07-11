include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to head
 * @number: numbert to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *num;

	node = *head;
	num = malloc(sizeof(listint_t));
	if (!num)
	{
		return (NULL);
	}
	num->n = number;
	if (node == NULL || node->n >= numer)
	{
		num->next = node;
		*head = num;
		return (num);
	}
	while (node && node->next && node->next->n < number)
	{
		node = node->next;
	}
	num->next = node->next;
	node->next = num;
	return (num);
}
