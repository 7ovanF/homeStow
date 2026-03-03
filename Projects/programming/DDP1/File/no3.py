file_name = input("Nama file data microblogs = ")
print('Nama-nama dengan follower paling banyak: ')

accs = {}
with open(file_name, 'r') as file:
    for line in file:
        acc = line.split()[-1]
        if acc not in accs:
            accs[acc] = 0
        accs[acc] += 1 

max_followers = 0
for acc, followers in accs.items():
    if followers > max_followers:
        max_followers = followers

for acc, followers in accs.items():
    if followers == max_followers:
        print(acc)