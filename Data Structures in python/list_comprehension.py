# here we try to print the table of 5 in a list.

n = 5 # no use on n here , only for understanding purpose that we will store the table of 5 here.

table = []

for i in range(1,11):
    table.append(5*i)

print(table)

# one liner
table = [5*i for i in range(1,11)]
print(table)