#!/usr/bin/python3
"""Definition of class LockedClass"""


class LockedClass:
    """
    Prevents instantiation of new LockedClass except with
    the firstname attribute
    """

    __slots__ = ["first_name"]
