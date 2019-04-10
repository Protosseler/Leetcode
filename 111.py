from __future__ import print_function
import sys
from numpy import sqrt

#data = sys.stdin.read().splitlines()

for line in data :
    print(line)

target = 100

def ssc(target):
    nums = [ii**2 for ii in xrange(1, sqrt(3000000))]
    result = []
    length = len(nums)
    for i in range(0, length - 2):
        target -= nums[i]
        left, right = i + 1, length - 1
        while left <= right:
            if nums[left] + nums[right] == target:
                result.append([nums[i], nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                    left += 1
    print result
    return sum([sum(ii) for ii in result])

ssc(target)
#print xx


