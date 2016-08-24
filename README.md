# IRC-Bot
This bot will sit on an irc channel and respond depending on the given commands. The commands are created by adding a file in the style:

``` python
from base_module import base_module  # import the base module which holds most of the logic

@base_module.deco  # This decorator is what registers the command
def hello4(command):  # the string passed in is the command in question
    if command == '4':  # determine if this command should handle what the other person said or not
        return "hello4"
    return ''  # Must return a string, empty string means there was no match for the input string
```

Note: there can be any number of commands in one file

To reload the commands simply call the reload method on the modules package. 
This will pick up any changed commands, any new commands, and any new files within the modules directory

To see if the bot should respond to something someone said pass the string into the run_command() method. If it was run the output will be returned, if not an empty string will be returned.

## IRC part is still under construction
