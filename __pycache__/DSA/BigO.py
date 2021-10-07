'''
Big O notation will give us a framework for officiall defining which code is better
why it is important - when dealing with petabyte of data efficiency matter
gives you a way help you when making trade offs b/w space & time
Used to formalize counting, allow us to express how the runtime of an algo grows with the input


nums = [1,2,3,4]

n = len(nums)
sum = 0

for i in range (0,n):
     sum+=nums[i]  # here we've N (addition,assignment) for each iteration, so 3 N assignment (comparision)

print("sum of array: ", sum)


# What is better these 2
1. Take less time & less space (machine take diff time to run code)
'''
'''
nums = [1,2,3,4] # assignment
n = len(nums) # assignment operation
print("sum of array: ", n*(n+1)/2) # here number of operation use (add,multi,assignment)

So number of operation use is not related to N here
n remains constant whether it's 10 or million we get the length and apply this inside the formulae. So time Complexity : O(1) - BigO 1

'''

'''


'''

