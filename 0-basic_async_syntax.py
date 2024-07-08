#!/usr/bin/env python3
"""Define async function"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for random delay number"""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number
