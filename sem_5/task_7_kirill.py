def gen_simple(num: int):
    yield 2
    count = 1
    number = 3
    while count < num:
        for dev in range(3, int(number ** 0.5) + 1, 2):
            if not number % dev:
                break
        else:
            yield number
            count += 1
        number += 2


print(*gen_simple(100))