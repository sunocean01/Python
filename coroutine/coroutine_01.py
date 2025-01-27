import asyncio
import time


async def set_after(fut):
	await asyncio.sleep(1)
	fut.set_result("666")

async def main():
	# 获取当前事件循环：
	loop = asyncio.get_running_loop()
	
	# 创建一个任务(Future对象)，这个任务什么都不干：
	fut = loop.create_future()
	
	# 创建一个任务(Future对象),绑定了set_after函数，函数内部1s以后会给fut赋值。即手动设置future任务的最终结果，那么fut就可以结束了。
	await loop.create_task(set_after(fut))
			
	# 等待任务最终结果(Future对象),没有结果则一直等下去：
	data = await fut
	print(data)
	
asyncio.run(main())

