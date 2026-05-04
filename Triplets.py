def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    for i in range (len(nums)-2):

        # skip the duplicate values
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # Set 2 pointers (left & right)
        left = i + 1
        right = len(nums) - 1

        # The left & right pointer moves until
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i],nums[left],nums[right]])

                # skip duplicate values between left and right pointer

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                    
                # move pointers

                left += 1
                right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1
    return result