#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: Python list object
 */
void print_python_list_info(PyObject *p)
{
	int alloc, list_size, i = 0;
	PyObject *item;

	list_size = PyList_Size(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %d\n", alloc);

	while (i < list_size)
	{
		item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, Py_TYPE(item)->tp_name);
		i++;
	}
}
