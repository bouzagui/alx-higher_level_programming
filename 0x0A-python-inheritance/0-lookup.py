#!/usr/bin/python3
""" show the list of available commands """


def lookup(opj):
    """
    Return the list of available commands
    """
    return (dir(opj))
