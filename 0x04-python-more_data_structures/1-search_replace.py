#!/usr/bin/python3
def search_replace(my_list, search, replace):
    list_cpy = []
    for i in my_list:
        if i == search:
            list_cpy.append(replace)
        else:
            list_cpy.append(i)
    return (list_cpy)