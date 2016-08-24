from modules.base_module import base_module

@base_module.deco
def hello4(command):
    if command == '4':
        return "hello4"
    return ''