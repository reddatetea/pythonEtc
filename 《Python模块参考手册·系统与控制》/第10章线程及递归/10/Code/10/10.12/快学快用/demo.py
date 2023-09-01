class BaseEventLoop:
    def run_forever(self):
        ...
        old_agen_hooks = sys.get_asyncgen_hooks()  # 获取默认的异步生成器函数
        # 设置新的异步生成器终结器和拦截迭代器
        sys.set_asyncgen_hooks(firstiter=self._asyncgen_firstiter_hook,
                               finalizer=self._asyncgen_finalizer_hook)
        try:
            ...
        finally:
            ...
            sys.set_asyncgen_hooks(*old_agen_hooks) # 如果出现异常，设置默认的异步生成器
    # 定义异步生成器即将被垃圾回收时调用的函数
    def _asyncgen_finalizer_hook(self, agen):
        self._asyncgens.discard(agen)
        if not self.is_closed():
            self.call_soon_threadsafe(self.create_task, agen.aclose())
    # 定义异步生成器第一次迭代时使用的函数
    def _asyncgen_firstiter_hook(self, agen):
        if self._asyncgens_shutdown_called:
            ...