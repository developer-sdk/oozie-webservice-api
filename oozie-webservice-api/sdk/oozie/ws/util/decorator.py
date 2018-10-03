#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018. 9. 19.

@author: whitebeard
'''
import inspect

def check_param_name_values(param_name, param_value_check_list):
    ''' restricted param value in check list by param name '''
    
    def wrapper(func):
        param_index = inspect.getargspec(func).args.index(param_name)
        
        def decorator(*args, **kwargs):
            if args[param_index] not in param_value_check_list:
                raise ValueError("Argument value error {0} not in [{1}]".format(param_name, ", ".join(param_value_check_list)))
            
            return func(*args, **kwargs)
        return decorator
    return wrapper

def check_param_index_values(param_index, param_value_check_list):
    ''' restricted param value in check list by param index '''
    
    def wrapper(func):
        def decorator(*args, **kwargs):
            if args[param_index] not in param_value_check_list:
                raise ValueError("args error {0} not in [{1}]".format(args[param_index], ",".join(param_value_check_list)))
            
            return func(*args, **kwargs)
        return decorator
    return wrapper