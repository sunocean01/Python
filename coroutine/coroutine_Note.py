

实现协程的方法：
	1. greenlet, 早期模块
	2. yield 关键字
	3. asyncio： python3.4以后引入的
	4. async, await 关键字 python3.5以后

3.1 事件循环：

	任务列表 = [任务1,任务2,任务3,...]
	while True:
		可执行任务列表,已完成任务列表 = 去任务列表里检查所有的任务，将'可执行'和'已完成'的任务返回
		
		for 就绪任务 in 可执行任务列表：
			执行已就绪任务
			
		for 已完成任务 in 已完成任务列表：
			在任务列表中移除已完成的任务
			
		如果 任务列表 中的任务都已完成，则终止循环
	
	# 生成或获取一个事件循环
	loop = asyncio.get_event_loop()
	
	# 将任务放到任务列表
	loop.run_until_complete(任务1)

3.2 快速上手
	协程函数：
	async def coro():
		print('Come on !')
	
	协程对象：
	cor = coro()     #协程内部代码不会运行

	运行协程函数：
		老版本的写法：
			loop = asyncio.get_event_loop()
			loop.run_until_complete(cor)
		
		python3.7以后：
			asyncio.run(result)
	
3.3 await:
	await + 可等待的对象(协程对象，Future，Task对象-->IO等待)
	await 就是等待对象的值得到结果之后继续往下走
	
	示例1：
		async def func():
			print("Come on!")
			response = await asyncio.sleep(2)
			print(f"End:{response}")

		asyncio.run(func())
	
	示例2：
		async def others():
			print("Start...")
			await asyncio.sleep(1)
			print("End!")
			return 'result'
			
		async def func():
			print("Run Coroutine code")
			# 遇到IO操作，挂起当前协程(任务)，等IO操作完成之后再往下执行。当前协程挂起时，事件循环可以执行其他协程(任务)。
			response = await others()
			print("IO结束，结果：{response}")
			
		asyncio.run(func())
		
	示例3：
		async def others():
			print("Start...")
			await asyncio.sleep(1)
			print("End!")
			return 'return'
			
		async def func():
			print("Run Coroutine code")
			# 遇到IO操作，挂起当前协程(任务)，等IO操作完成之后再往下执行。当前协程挂起时，事件循环可以执行其他协程(任务)。
			response1 = await others()
			response2 = await others()
			print(f"IO结束，结果：{response1},{response2}")
			
			
3.4 Task对象：
	在事件循环中添加多个任务的。
	Task: 用于并发调度协程，通过 asyncio.create_task(协程对象) 的方式创建Task对象，这样可以让协程加入事件循环中等待调度执行。除了使用asyncio.create_task()函数以外，还可以使用低层级的loop.create_task()或ensure_future()函数，不建议手动实例化Task对象。
	
	示例1：
		async def func():
			print(1)
			await asyncio.sleep(1)
			print(2)
			
			return 'return'
			
		async def main():
			print("Main...")
			task1 = asyncio.create_task(func())
			task2 = asyncio.create_task(func())
			print("End!")
			
			ret1 = await task1
			ret2 = await task2
			print(ret1,ret2)
			
		asyncio.run(main())
		
	示例2：
		async def func():
			print(1)
			await asyncio.sleep(1)
			print(2)
			
			return 'return'
			
		async def main():
			print("Main...")
			
			task_list = [
							asyncio.create_task(func(),name='N1')
							asyncio.create_task(func(),name='N2')
							]
			print("End!")
			
			# await task_list   不能这些写
			done,pending = await asyncio.wait(task_list,timeout=None)
			print(done)
			
		asyncio.run(main())	

	示例3：

		async def func():
			print(1)
			await asyncio.sleep(1)
			print(2)
			
			return 'return'
		
		# 下面这种写法会报错：
		task1 = asyncio.create_task(func(),name='N1')
		task2 = asyncio.create_task(func(),name='N2')
		
		task_list = [task1,task2]
		done,pending = asyncio.run(asyncio.wait(task_list))
		print(done)	
		
		
		# 可以的写法：
		task_list = [func(),func()]
		done,pending = asyncio.run(asyncio.wait(task_list))
		print(done)			

3.5 asyncio.Future对象
	它是Task类的基类
	
	示例1：
	
	async def main():
		# 获取当前事件循环：
		loop = asyncio.get_running_loop()
		
		# 创建一个任务(Future对象)，这个任务什么都不干：
		fut = loop.create_future()
		
		# 等待任务最终结果(Future对象),没有结果则一直等下去：
		await fut
		
		
	示例2：
	
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

3.6 concurrent.futures.Future对象

	使用线程池、进程池实现异步操作时用到的对象
	
	import time
	from concurrent.futures import Future
	from concurrent.futures.thread import ThreadPoolExecutor
	from concurrent.futures.process import ProcessPoolExecutor
	
	def func(value):
		time.sleep(1)
		print(value)
		return 123
		
	# 创建线程池：
	pool = ThreadPoolExecutor(max_workers=5)
	
	# 或创建进程池：
	# pool = ProcessPoolExecutor(max_workers5)
	
	for i in range(10):
		fut = pool.submit(func,i)
		print(fut)