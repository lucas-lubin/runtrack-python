def listAlphabet():
    return [chr(i) for i in range(ord("a"), ord("z") + 1)]

result = "".join(reversed(listAlphabet()))
print(result)