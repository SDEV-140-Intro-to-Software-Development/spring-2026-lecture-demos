def square_even_numbers(numbers):
	return [num ** 2 for num in numbers if num % 2 == 0]
    # new_nums = []
    # for num in numbers:
    #     if num % 2 == 0:
    #         new_nums.append(num ** 2)
    
    # return new_nums

squares = square_even_numbers([1, 2, 3, 4, 5, 6])
print(squares)