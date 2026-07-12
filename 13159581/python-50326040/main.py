import threading
import asyncio
import aiohttp
import random
import time
import sys
import os

try:
    os.mkdir('C:\\cat_images')
except:
    pass

start = time.time()
semaphore = asyncio.Semaphore(5)
session = None
numlist = [int(i) for i in range(100,2101)]

async def request(num):
    async with semaphore:
        x = num
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9'
        }
        try:
            async with session.get("https://placekitten.com/"+x+'/'+x,headers=headers) as res:
                await asyncio.sleep(5)
                cat_img = await res.read()
                print(type(cat_img))
                with open('C://images/'+x+'x'+x+'.jpg','wb') as f:
                    f.write(cat_img)
        except asyncio.exceptions.TimeoutError:
            print('Time out')
            threading.Thread(target=request,args=(num,)).start()
            #await request(num)

async def main():
    global session
    timeout = aiohttp.ClientTimeout(total=5)
    connector = aiohttp.TCPConnector(ssl=False)
    session = aiohttp.ClientSession(timeout=timeout,connector=connector)
    index_tasks = [asyncio.ensure_future(request(str(i))) for i in numlist]
    await asyncio.gather(*index_tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
end = time.time()
print("Cost time:", end - start)
