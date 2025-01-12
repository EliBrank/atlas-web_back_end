#!/usr/bin/env python3

"""Defines async_comprehension function"""

import asyncio
from time import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures time taken to execute async_comprehension 4 times

    Returns:
        Time taken to execute async_comprehension 4 times (in parallel)
    """
    start_time: float = time()

    coros = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coros)

    end_time: float = time()

    return end_time - start_time
