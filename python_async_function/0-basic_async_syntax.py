#!/usr/bin/env python3

"""Defines wait_random async function"""

import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Waits between 0 and a number of seconds (specified by max_delay)

    Args:
        max_delay: upper bound for number of seconds to wait

    Returns:
        number of seconds waited (float)
    """

    time_to_wait: float = uniform(0, max_delay)

    await asyncio.sleep(time_to_wait)

    return time_to_wait
