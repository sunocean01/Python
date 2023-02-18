#!python
"""
reloadall.py: transitively reload nested modules(2.x + 3.x).
Call reload_all with one or more improted module module objects.
此脚本实现传递导入
"""

import types
from imp import reload                          #3.x中的要求

def status(module):
    print('reloading:' + module.__name__)

def tryreload(module):
    try:
        reload(module)
    except:
        print('Failed:{}'.format(module))

def transitive_reload(module,visited):
    if not module in visited:
        status(module)
        tryreload(module)
        visited[module] = True
        for attrobj in module.__dict__.values():
            if type(attrobj) == types.ModuleType:
                transitive_reload(attrobj,visited)
                
def reload_all(*args):
    visited = {}
    for arg in args:
        if type(arg) == types.ModuleType:
            transitive_reload(arg,visited)
        
def tester(reloader,modname):
    import importlib, sys
    if len(sys.argv) > 1: modname = sys.argv[1]
    module = importlib.import_module(modname)
    reloader(module)

if __name__ == '__main__':
    tester(reload_all,'reloadall')


r"""三种使用方式:
1. 只运行自己:
    C:\..\library\reload_all>python reloadall.py
    reloading:reloadall
    reloading:types
    reloading:functools
    reloading:collections.abc
2. 使用命令行参数,指定重载模块
    C:\..\library\reload_all>python reloadall.py reloading_parent
    Test2: child
    --------------------------------------------------------------------------------
    Test1: parent
    --------------------------------------------------------------------------------
    reloading:reloading_parent
    Test1: parent
    --------------------------------------------------------------------------------
    reloading:reloading_child
    Test2: child
    --------------------------------------------------------------------------------
    reloading:sys
    reloading:re
    ...
3. 交互式命令行下应用这一模块
    >>> from reloadall import reload_all
    >>> import reloading_parent
    Test2: child
    --------------------------------------------------------------------------------
    Test1: parent
    --------------------------------------------------------------------------------
    >>> reload_all(reloading_parent)
    reloading:reloading_parent
    Test1: parent
    --------------------------------------------------------------------------------
    reloading:glob
    reloading:re
    reloading:copyreg
    reloading:_locale
    ...
    Test2: child
    --------------------------------------------------------------------------------
"""









    