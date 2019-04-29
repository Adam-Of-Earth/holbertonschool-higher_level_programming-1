#include "lists.h"

/**
 * check_cycle - Checks if a linked list is a cycle
 * @list: The list to check
 *
 * Return: 1 (if there is a cycle)
 */
int check_cycle(listint_t *list)
{
	listint_t *firstNode, *nodePointer;

	firstNode = list;
	nodePointer = list;
	while (nodePointer != NULL)
	{
		if (nodePointer->next == NULL)
			return (0);
		nodePointer = nodePointer->next;
		if (nodePointer == firstNode)
			return (1);
	}
	return (2);
}
