import re


def real_len(text):
    a = len(text)
    num = re.findall("\s", text)
    b = len(num)
    c = a - b
    return c
