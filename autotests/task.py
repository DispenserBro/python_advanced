def fibonacci(stop = 1_000_000_000):
    current_fib = 0
    fib_lst = [current_fib, 1]
    
    while(current_fib < stop if stop is not None else True):
        yield current_fib
        fib_lst[0], fib_lst[1] = fib_lst[1], fib_lst[0]
        current_fib = fib_lst[0]
        fib_lst[1] = sum(fib_lst)

f = fibonacci(None)

for i in range(1000):
    print(next(f))