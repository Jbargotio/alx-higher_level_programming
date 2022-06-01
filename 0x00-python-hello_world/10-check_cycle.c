#include "lists.h"

/**
 * check_cycle:Check if a linked list has a cycle
 * @list: a linked list
 * Return: 0(Fail),1(Success)
 */
int check_cycle(listint_t *list)
{
	listint_t *it = list;
	listint_t *l_list = it;

	while (it && l_list && it->next)
	{
		l_list = l_list->next;
		it = it->next->next;
		if(l_list == it)
			return (1);
	}
	return (0);
}
