#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the address of the linked list
 * @number: number to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *my_node = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
	{
		return NULL;
	}
	new->n = number;

	if (my_node == NULL || my_node->n >= number)
	{
		new->next = my_node;
		*head = new;
		return (new);
	}
	
	while (my_node && my_node->next && my_node->next->n < number)
		my_node = my_node->next;

	new->next = my_node->next;
	my_node->next = new;

	return (new);
}
