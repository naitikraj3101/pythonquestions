# Q program to find the largest among three numbers

x = int(input('enter your first number : '))
y = int(input('enter your second number : '))
z = int(input('enter your third number : '))

nums = [x,y,z]
nums.sort()
print(nums[len(nums)-1])