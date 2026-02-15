import asyncio

async def delay(seconds: int):
    await asyncio.sleep(seconds)