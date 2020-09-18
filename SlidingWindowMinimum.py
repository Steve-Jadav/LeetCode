# This is question from Citrix Hackerrank Coding Challenge
# The solution requirment was to find the maximum from all the minimums found from all the subarrays of size k

from collections import deque

def calculateDiskSpace(nums: list, k: int) -> int:
    """ Based on the sliding window algorithm. """

    maxSpace = float("-inf")
    deck = deque()

    for i in range(0, len(nums)):

        if deck and deck[0] == i - k:
            deck.popleft()

        while deck and nums[deck[-1]] >= nums[i]:
            deck.pop()

        deck.append(i)

        if i >= k - 1:
            maxSpace = max(maxSpace, nums[deck[0]])

    return maxSpace


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = calculateDiskSpace(nums, k)
    print (result)
