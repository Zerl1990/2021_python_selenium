"""List comprehension example."""

list1 = [5, 10, 15, 20, 25, 50, 20]

for index, value in enumerate(list1):
    if value == 20:
        list1[index] = 200
print(f'Solution: {list1[2:6]}')
