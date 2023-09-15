#include "hash_tables.h"

/**
 * hash_table_create - Write a function that creates a hash table.
 *
 * @size: size of the array
 *
 * Returns: a pointer to the newly created hash table
 * NULL, If something went wrong, your function
 */

hash_table_t *hash_table_create(unsigned long int size)
{
	hash_table_t *table;

	table = malloc(sizeof(hash_table_t));

	table->size = size;

	return (table);
}
