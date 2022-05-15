# -*- coding: utf-8 -*-

from lispparser import parse, parse_multiple, unparse
from core import eval

def interpret(exp, env=None):
    """Interpret a single Lisp expression"""
    exp = eval(parse(exp), env if env is not None else [])
    return unparse(exp)

def interpret_file(filename, env):
    """Interpret a list source file, returning the value of the last expression"""
    with open(filename, 'r') as f:
        source = f.read()
    results = [eval(ast, env) for ast in 
                parse_multiple(source)]
    results = [ast for ast in 
                parse_multiple(source)]
    return results[-1]

def repl(env=None):
    """A very simple REPL"""
    env = [] if env is None else env
    while True:
        try:
            print(interpret(input("> "), env))
        except (EOFError, KeyboardInterrupt):
            return
        except Exception as e:
            print("! %s" % e)
