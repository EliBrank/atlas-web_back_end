#!/usr/bin/env python3

"""Defines async_generator function"""

import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields 10 random numbers between 0 and 10 with 1 second delay

    Returns:
        Random float between 0 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
