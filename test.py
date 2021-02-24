"""Test file."""
from multiprocessing import Process
import time

p1 = Process()
p2 = Process()


def func1():
    """Test function 1."""
    for numb in range(10):
        time.sleep(1)
        print("text")
        print(numb)


def func2():
    """Test function 2."""
    inner = input()
    print(inner)


if __name__ == '__main__':
    p1 = Process(target=func1)
    print(p1)
    p2 = Process(target=func2)
    print(p2)
    p1.start()
    p2.start()
