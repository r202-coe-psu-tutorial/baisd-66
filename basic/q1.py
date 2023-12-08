
# method 1
# num_str = input("Input: ")
# nums = [int(n) for n in num_str.split(',')]

# print("Output: ", nums.count(len(nums)))

# method 2
# nums = [int(n) for n in input("Input: ").split(',')]
# print("Output: ", nums.count(len(nums)))


# method 3

num_str = input("Input: ")
nums = [int(n) for n in num_str.split(',')]
counter = 0
nums_len = len(nums)
for i in nums:
    if i == nums_len:
        counter += 1

print("Output: ", counter)