#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *flash, *sloth;

	sloth = list;
	flash = list;
	if (list == NULL)
	{
		return (0);
	}
	while (sloth && flash && flash->next)
	{
		sloth = sloth->next;
		flash = flash->next->next;
		if (sloth == flash)
		{
			return (1);
		}
	}
	return (0);
}
