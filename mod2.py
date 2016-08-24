from modules.base_module import base_module

@base_module.deco
def hello3(command):
    if command == '3':
        return "hello3.5"
    return ''

