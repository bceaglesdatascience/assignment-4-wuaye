purchases = int(input("Number of purchases: "))
salesTax = float(input("Sales tax: "))

customerList = []
costList = []
for i in range(purchases):
    name = input("Customer: ")
    customerList.append(name)
    cost = int(input("Cost: "))
    costList.append(cost)

def add_tax(list, tax):
    newCostList = []
    for i in range(len(list)):
        newCostList.append(list[i] * (1+tax))
    return newCostList

newList = add_tax(costList, salesTax)

dict = {}

for i in range(len(customerList)):
    customerName = customerList[i]
    afterTax = newList[i]
    
    if customerName in dict:
        dict[customerName] += afterTax
    else:
        dict[customerName] = afterTax

print(dict)
