from modules.base_module import base_module

@base_module.deco
def hello(command):
    if command == '1':
        return "hello1"
    return ''

@base_module.deco
def hello2(command):
    if command == '2':
        return "hello2"
    return ''


