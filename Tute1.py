# list1=[['ramesh',4],['suresh',5],['bihari',7],['jaggu',90]]
# dict1=dict(list1)
# print(dict1)

# for ramu,pappu in dict1.ramu():
#     print(ramu,pappu)
items=['ramesh','jaggu',4,5,6,4,34,67]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)

