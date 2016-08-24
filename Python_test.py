import modules
import importlib

class Test:

    def makeDeco():
        registry = {}
        def registrar(func):
            registry[func.__name__] = func
            return func
        registrar.all = registry
        return registrar

    deco = makeDeco()

    @deco
    def test1():
        pass

    @deco
    def test2():
        pass

    @deco
    def test3():
        pass

#print(Test.deco.all)

print(modules.package_contents())
print(modules.run_command(''))
print(modules.run_command('1'))
print(modules.run_command('2'))
print(modules.run_command('3'))
input()
importlib.invalidate_caches()
importlib.reload(modules)
importlib.invalidate_caches()
modules.reload_()
print(modules.run_command('3'))
print(modules.run_command('4'))