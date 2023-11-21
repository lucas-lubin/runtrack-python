def premier(nmb):
    if nmb < 2:
        return False
    for i in range(2, int(nmb**0.5) + 1):
        if nmb % i == 0:
            return False
    return True

for num in range(2, 1001):
    if premier(num):
        print(num)