#!/usr/bin/env python3

"""Defines wait_n async function"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Executes wait_random n times and compiles returned values in list

    Args:
        n: number of times to run wait_random
        max_delay: maximum delay passed to wait_random

    Returns:
        List of wait_random return values in ascending order
    """

    wait_list = []

    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        wait_list.append(delay)

    return wait_list
