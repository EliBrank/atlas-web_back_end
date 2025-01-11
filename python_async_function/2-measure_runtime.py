#!/usr/bin/env python3

"""Defines measure_time async function"""

import asyncio
from time import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Measures time taken to execute wait_n

    Args:
        n: number of wait_random calls for wait_n
        max_delay: maximum delay passed to wait_n

    Returns:
        Time taken to execute wait_n, averaged per number of wait_random calls
    """

    start_time = time()

    asyncio.run(wait_n(n, max_delay))

    end_time = time()

    return (end_time - start_time) / n
