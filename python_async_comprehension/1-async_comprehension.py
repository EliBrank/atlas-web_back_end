#!/usr/bin/env python3

"""Defines async_comprehension function"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Creates list of 10 random numbers (0-10) using async_generator

    Returns:
        List containing 10 random numbers (0-10)
    """
    return [i async for i in async_generator()]
