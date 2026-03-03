# a = 5

# def funct1():
#     a = a + 1 # why error?
#     print(a)

# def funct2():
#     a = 1
#     funct1()
#     print(a)

# funct1()

def funct1():
    a = 5
    def funct2():
        print(a)
    funct2()
funct1()