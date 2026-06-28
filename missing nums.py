nums = [0, 2, 3, 1, 4]

n = len(nums)

formela = n *(n+1)//2

missing_nums = formela -sum (nums)

nums.append(missing_nums)
nums.sort()

print(nums)