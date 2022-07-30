# leetcode 1114
# approach 1 using while and continue
# Suppose we have a class:

# public class Foo {
#   public void first() { print("first"); }
#   public void second() { print("second"); }
#   public void third() { print("third"); }
# }
# The same instance of Foo will be passed to three different threads. Thread A will call first(), thread B will call second(), and thread C will call third(). 
# Design a mechanism and modify the program to ensure that second() is executed after first(), and third() is executed after second().

class Foo:
    t1,t2,=False,False
    def __init__(self):
        pass

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        printFirst()
        self.t1=True

    def second(self, printSecond: 'Callable[[], None]') -> None:
        while not self.t1 :
            continue
        printSecond()
        self.t2=True
        
    def third(self, printThird: 'Callable[[], None]') -> None:
        while not self.t2:
            continue
        printThird()
        
        
#         approach 2 using threading events

from threading import Event
class Foo:
    def __init__(self):
        self.t1=Event()
        self.t2=Event()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        printFirst()
        self.t1.set()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.t1.wait()
        printSecond()
        self.t2.set()
        
    def third(self, printThird: 'Callable[[], None]') -> None:
        self.t2.wait()
        printThird()
