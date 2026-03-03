import time
start = time.perf_counter()

def funct(header_row, table):
    for row in table:
        dict_row = dict()
        for i in range(len(header_row)):
            if i >= len(row):
                value = None
            else:
                value = row[i]
            dict_row[header_row[i]] = value
        yield dict_row

header_row = ["nama", "npm"]
table = [["bambang", '2505'], ['safira']]

# user_input = input('input:')
# print(funct(header_row, table))
gen = funct(header_row, table)
print(next(gen))
print(next(gen))

end = time.perf_counter()
print(end - start)
