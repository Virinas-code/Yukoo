# -*- coding: utf-8 -*-
from __future__ import print_function
"""Test file."""
import sys
err_code = 0

try:
    import my_engine
    print("\033[32mImport du module\033[0m")
except Exception as exception:
    print("\033[31mImport du module :", exception, "\033[0m")
    err_code -= 1

try:
    test_engine = my_engine.EngineBase("Test", "Yukoo test")
    print("\033[32mEngineBase\033[0m")
except Exception as exception:
    print("\033[31mEngineBase :", exception, "\033[0m")
    err_code -= 1


def test(cmd, name):
    global err_code
    try:
        exec(cmd, globals(), locals())
        print("\033[32m", name, "\033[0m")
    except Exception as exception:
        print("\033[31m" + name + ":", exception, "\033[0m")
        err_code -= 1


test("uci = my_engine.UCI(test_engine)", "Create UCI")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"isready\")", "isready")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"debug\")", "debug")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"debug bruh\")", "debug bruh")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"debug on off\")", "debug on off")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"debug on\")", "debug on")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"debug off\")", "debug off")



sys.exit(err_code)
