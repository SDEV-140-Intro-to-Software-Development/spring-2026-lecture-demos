nums = [1, 1, 2, 2, 3, 3, 4, 4]

# for index,num in enumerate(nums):
#     nums[index] = num + 5

# odd_nums=[]
# for num in nums:
#     if num % 2 != 0:
#         odd_nums.append(num)

# print(odd_nums)

for num in nums[:]:
    nums.append(num * 2)

print(nums)