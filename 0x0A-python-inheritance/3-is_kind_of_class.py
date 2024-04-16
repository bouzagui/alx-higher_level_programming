#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    try:
        if isinstance(obj, a_class):
            return True
        elif not isinstance(obj, a_class):
            return False
    except TypeError:
        pass
