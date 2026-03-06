def remove_odds(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cut_down_list = remove_odds(original_list)

print(original_list)
print(cut_down_list)