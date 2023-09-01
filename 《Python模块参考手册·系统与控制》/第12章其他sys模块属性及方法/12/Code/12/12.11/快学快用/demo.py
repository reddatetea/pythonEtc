def breakpointhook(*args, **kws):
    import importlib, os, warnings
    hookname = os.getenv('PYTHONBREAKPOINT')
    if hookname is None or len(hookname) == 0:
        hookname = 'pdb.set_trace'
    elif hookname == '0':
        return None
    modname, dot, funcname = hookname.rpartition('.')
    if dot == '':
        modname = 'builtins'
    try:
        # 模块导入失败，或funcname不可调用都会引发RuntimeWarning
        module = importlib.import_module(modname)
        hook = getattr(module, funcname)
    except:
        # 如果抛出异常，则不会执行hook(*args, **kws)
        warnings.warn(
            'Ignoring unimportable $PYTHONBREAKPOINT: {}'.format(
                hookname),RuntimeWarning)
    # 如果实参与函数签名中的参数不匹配，则会抛出TypeError
    return hook(*args, **kws)
__breakpointhook__ = breakpointhook
import sys
print(sys.breakpointhook())