"""Test file."""
try:
    import my_engine
    print("✅ Import du module")
except Exception as e:
    print(f"❎ Import du module : {e}")

try:
    test_engine = my_engine.EngineBase("Test", "Yukoo test")
    print("✅ EngineBase")
except Exception as e:
    print(f"❎ EngineBase : {e}")
