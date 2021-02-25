# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Test file."""
import sys
err_code = 0

try:
    import my_engine
    print("✅ Import du module")
except Exception as exception:
    print("❎ Import du module :", exception)
    err_code -= 1

try:
    test_engine = my_engine.EngineBase("Test", "Yukoo test")
    print("✅ EngineBase")
except Exception as exception:
    print("❎ EngineBase :", exception)
    err_code -= 1


def test(cmd, name):
    global err_code
    try:
        exec(cmd, globals(), locals())
        print("✅", name)
    except Exception as exception:
        print("❎", name, ":", exception)
        err_code -= 1


test("uci = my_engine.UCI(test_engine)", "Create UCI")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"isready\")", "isready")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"debug\")", "debug")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"debug bruh\")", "debug bruh")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"debug on off\")", "debug on off")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"debug on\")", "debug on")
test("uci = my_engine.UCI(test_engine);uci.evaluate_uci(\"debug off\")", "debug off")



sys.exit(err_code)
