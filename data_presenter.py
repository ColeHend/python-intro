cupcake_file = open('CupcakeInvoices.csv')
import matplotlib as  mpl
import matplotlib.pyplot as plt
import numpy as np

# for row in cupcake_file:
#       print(row)  

# for row in cupcake_file:
#     split = row.split(',')
#     print(split[2])

# for row in cupcake_file:
#     split = row.split(',')
#     print(float(split[3])*float(split[4]))

total = 0
# for row in cupcake_file:
#     split = row.split(',')
#     invoice = float(split[3])*float(split[4])
#     total += invoice
# print(round(total,2))

chocolate = 0
strawberry = 0
vanilla = 0
for row in cupcake_file:
    split = row.split(',')
    invoice = float(split[3])*float(split[4])
    if split[2] == 'Chocolate':
        chocolate += invoice
    elif split[2] == 'Strawberry':
        strawberry += invoice
    elif split[2] == 'Vanilla':
        vanilla += invoice
names = ['Strawberry','Chocolate','Vanilla']
y = [strawberry,chocolate,vanilla]

plt.bar(names,y)
plt.title('Ice Cream')
plt.ylabel('Sales')
plt.show()



cupcake_file.close()