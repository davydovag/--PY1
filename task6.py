list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
a = list_numbers.index(max(list_numbers))
max_ = list_numbers[0]
for current_number in list_numbers:
    if current_number > max_:
        max_ = current_number
max_number_index = None
for current_index, current_number in enumerate(list_numbers):
    if current_number == max_:
        max_number_index = current_index
        break

list_numbers[max_number_index], list_numbers[-1] = list_numbers[-1], list_numbers[max_number_index]
print(list_numbers)
