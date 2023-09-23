# site_checker_v0.py

import aiohttp
import asyncio

async def check(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            print(f"{url}: status -> {response.status}")
            html = await response.text()
            print(f"'{url}: type -> {html[:17].strip()}")

async def main ():
    await asyncio.gather(
        check("https://www.sunmi.com/en-US/80-kitchen-cloud-printer/"),
        check("https://pycoders.com"),
    )

asyncio.run(main())