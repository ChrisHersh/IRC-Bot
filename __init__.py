import imp
import os
import importlib
MODULE_EXTENSIONS = ('.py')


## Get all modules


def package_contents():
    package_name = 'modules'
    file, pathname, description = imp.find_module(package_name)
    if file:
        raise ImportError('Not a package: %r', package_name)
    # Use a set because some may be both source and compiled.
    return list(set([os.path.splitext(module)[0]
        for module in os.listdir(pathname)
        if module.endswith(MODULE_EXTENSIONS) 
            and module != '__init__.py'
            and module != 'base_module.py']))

found_modules = package_contents()


## Load all modules and store a reference


def load_modules():
    loaded_modules = []
    for x in found_modules:
        loaded_modules.append(importlib.import_module('modules.' + x))
    return loaded_modules

loaded_modules = load_modules()

def reload_():
    for x in loaded_modules:
        importlib.reload(x)
    
## Run a given command


def run_command(command):
    return base_module.run(command)

