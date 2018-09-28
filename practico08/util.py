import random
import string


def getRandomsString():
    return "".join([random.choice(string.ascii_letters) for _ in range(10)])


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Pepe(Singleton):
    pass

if __name__ == '__main__':
    a = Pepe()
    b = Pepe()
    print(a is b)