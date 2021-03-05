"""YUKOO. Simple chess engine."""
import my_engine

yukoo = my_engine.EngineBase("Yukoo", "Virinas-code")
e = my_engine.UCI(yukoo)
e.run()
