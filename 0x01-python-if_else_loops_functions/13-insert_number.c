#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: pointer to the linked list
 * @number: value of node to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *prev;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	new_node->n = number;
	new_node->next = NULL;

	prev = *head;
	while (prev && prev->next && prev->next->n <= number)
		prev = prev->next;

	if (prev == *head)
	{
		new_node->next = *head;
		*head = new_node;
	}
	else
	{
		new_node->next = prev->next;
		prev->next = new_node;
	}

	return (new_node);
}
