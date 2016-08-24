class base_module(object):
    
    def makeDeco():
        registry = {}
        def registrar(func):
            registry[func.__name__] = func
            return func
        registrar.all = registry
        return registrar

    deco = makeDeco()

def run(command):
        res = ''
        for method in base_module.deco.all:
            res = base_module.deco.all[method](command)
            if res != '':
                return res
        return 'nada'
