def fibo_gen():
    first, second = 0, 1
    while True:
        yield first
        first, second = second, first + second


fibo_sequence = fibo_gen()
for i in range(10):
    print(next(fibo_sequence))
