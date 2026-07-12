import asyncio
import aiohttp
import random
import time
import sys

start = time.time()
semaphore = asyncio.Semaphore(100)
session = None

async def request(num):
    async with semaphore:
        x = str(random.randint(100,2100))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        try:
            async with session.get("https://placekitten.com/"+x+'/'+x,headers=headers) as res:
                await asyncio.sleep(1)
                cat_img = await res.read()
                print(type(cat_img))
                with open('./images/cat'+num+'.jpg','wb') as f:
                    f.write(cat_img)
        except asyncio.exceptions.TimeoutError:
            print('Time out')
            await request(num)

async def main():
    global session
    timeout = aiohttp.ClientTimeout(total=3)
    connector = aiohttp.TCPConnector(ssl=False)
    session = aiohttp.ClientSession(timeout=timeout,connector=connector)
    index_tasks = [asyncio.ensure_future(request(str(i))) for i in range(2000)]
    await asyncio.gather(*index_tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end = time.time()
print("Cost time:", end - start)
