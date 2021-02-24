# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""Test file."""
import sys
err_code = 0

try:
    import my_engine
    print("✅ Import du module")
except Exception as exception:
    print(f"❎ Import du module : {exception}")
    err_code -= 1

try:
    test_engine = my_engine.EngineBase("Test", "Yukoo test")
    print("✅ EngineBase")
except Exception as exception:
    print(f"❎ EngineBase : {exception}")
    err_code -= 1

sys.exit(err_code)
