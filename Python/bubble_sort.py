# TODO: Zeitmessung mittels Zeitstempel

input_list = [10, 2, 5, 4, 80, 43]
print("Unsortierte Liste:", input_list)

for i in range (len(input_list) - 1): # -1 weil wir ja bei 0 beginnen
    for j in range(len(input_list) - (1 + i)):
        if input_list[j] > input_list[j + 1]:
            temp = input_list.pop(j)
            input_list.insert(j + 1, temp)

print("Sortierte Liste:", input_list)


# alternative
input_list = [10, 2, 5, 4, 80, 43]
print("Unsortierte Liste:", input_list)

for i in range(len(input_list) - 1): # -1 weil wir ja bei 0 beginnen
    for j in range(len(input_list) - (1 + i)):
        if input_list[j] > input_list[j + 1]:
            temp = input_list[j +1]
            input_list[j + 1] = input_list[j]
            input_list[j] = temp
print("Sortierte Liste:", input_list)