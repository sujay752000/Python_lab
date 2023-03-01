dict1 = {"sujay": 1, "lijo": 400, "hari": 50, "ashik": 200, "amal": 10}
ascending_dict = {}
desending_dict = {}

lst = list(dict1.values())
lst.sort()

for i in lst:
    for j in dict1.keys():
        if dict1[j] == i:
            ascending_dict.update({j: i})

print(ascending_dict)

lst.sort(reverse=True)

for i in lst:
    for j in dict1.keys():
        if dict1[j] == i:
            desending_dict.update({j: i})

print(desending_dict)
