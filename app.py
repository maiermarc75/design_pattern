from abc import ABC


class Default(ABC):
    def print_str():
        pass


class A:
    def print_str():
        print("a")


class B:
    def print_str():
        print("b")


class C:
    def __init__(self, flag):
        self.flag = flag

    def get_class(self):
        if self.flag == "a":
            A.print_str()
        if self.flag == "b":
            B.print_str()

    def temp():
        print("temp")


obj = C("a")
obj.get_class()
