def filter(list, filter_func):
    new_list = []
    for item in list:
        if filter_func(item) == True:
            new_list.append(item)

    return new_list

def is_even(item):
    return item % 2 == 0

nums = [1,2,3,4,5]

evens = [num for num in nums if is_even(num)]

events = filter(nums, is_even)
print()