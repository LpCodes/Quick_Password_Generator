import string
import random

c = string.ascii_uppercase
b = string.digits
a = string.ascii_lowercase
d = string.punctuation


def genpass(limit):
    x = []
    for i in range(limit):
        data = "".join(random.choices(c + b + a + d))
        x.append(data)

    finalpass = "".join(x)
    return finalpass


print(genpass(8))


input()