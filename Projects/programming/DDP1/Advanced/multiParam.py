def even_sum(*args):
    sum = 0
    for i in args:
        if not i % 2:
            sum += i
    return sum


print(even_sum(5, 3, 2, 4, 9, 8))

def func(p1, p2, **args):
    print(p1, p2, args)
func(p2=5, p1="saya", what=13094)
