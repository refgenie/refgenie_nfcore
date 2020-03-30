# Refgenie plugin

This is a demo refgenie plugin. Refgenie plugins are Python packages that provide functions that are configured to run during specific refgenie actions.

## Hooks

The plugin system can run functions at these hooks: 

- "post_update"
- "pre_pull"
- "pre_tag"
- "pre_list"

A refgenie plugin has 3 requirements:

## 1. Add entry_points to setup.py

The [setup.py](setup.py) file uses `entry_points` to specify a mapping of refgenie hooks to functions to call.

```
    entry_points={
        'refgenie.hooks.post_update': 'myplugin=refgenie_myplugin:my_post_update_func',
        'refgenie.hooks.pre_pull': 'myplugin=refgenie_myplugin:my_pre_pull_func',
        }
```

The format is: `'refgenie.hooks.HOOK': 'PLUGIN_NAME=PLUGIN_PACKAGE_NAME:FUNCTION_NAME'`.

- "HOOK" must be one of the list provided above.
- "PLUGIN_NAME" can be any unique identifier for your plugin
- "PLUGIN_PACKAGE_NAME" must be the name of python package the holds your plugin.
- "FUNCTION_NAME" must match the name of the function in your package

## 2. Write functions to call

The module [refgenie_myplugin/refgenie_myplugin.py](refgenie_myplugin/refgenie_myplugin.py) contains the functions, with names corresponding to the `FUNCTION_NAME` in the entry points above. These functions **must take a RefGenConf object as sole parameter**.

```
import refgenconf

def my_post_update_func(rgc):
	print("You have successfully run refgenie_myplugin:my_post_update_func()")

def my_pre_pull_func(rgc):
	print("You have successfully run refgenie_myplugin:my_pre_pull_func().")
```

That's it! Install the package and it should run your functions at the specified hook entry points.