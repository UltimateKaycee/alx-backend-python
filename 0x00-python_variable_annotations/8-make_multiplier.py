#!/usr/bin/env python3
'''Module for Task 8.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Function to create a multiplier function.
    '''
    return lambda x: x * multiplier
