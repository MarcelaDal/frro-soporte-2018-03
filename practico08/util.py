import random
import string

def getRandomsString():
    return "".join([random.choice(string.ascii_letters) for _ in range(10)])