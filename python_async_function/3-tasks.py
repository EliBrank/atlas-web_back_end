#!/usr/bin/env python3

"""Defines task_wait_random function"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    """Creates wait_random task

    Args:
        max_delay: maximum delay for wait_random task

    Returns:
        New wait_random task with specified max delay
    """

    return asyncio.create_task(wait_random(max_delay))
