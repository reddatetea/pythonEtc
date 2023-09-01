import sys
print('默认包装器',sys.get_coroutine_wrapper())
def wrapper(coro):
    async def wrap(coro): # 异步函数
        return await coro # 程序挂起
    return wrap(coro)
sys.set_coroutine_wrapper(wrapper) # 设置包装器
print('设置的包装器',sys.get_coroutine_wrapper())