"""Contact two lists."""

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
solution = []

for f_item in list1:
    for s_item in list2:
        solution.append(f'{f_item} {s_item}')

print(f'Solution: {solution}')
