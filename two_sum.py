# https://leetcode.com/problems/two-sum/description/


class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)

        for i in range(length - 1):
            for j in range(i + 1, length):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]


class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        num_dict = {nums[i]: i for i in range(length)}

        for i in range(length):
            other = target - nums[i]
            if other in num_dict and num_dict[other] != i:
                return [i, num_dict[other]]

        return [-1, -1]


# someone else solution
class Solution3:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        num_dict = {}

        for i in range(length):
            complement = target - nums[i]
            if complement in num_dict:
                return [num_dict[complement], i]
                # better than above cause we don't have to check if indices are same
                # cause we don't have same element until we add it below
                # other thing is the reason num_dict[complement] is back cause
                # it occured first in loop
            num_dict[nums[i]] = i

        return [-1, -1]


if __name__ == "__main__":
    nums = [-1, -2, -3, -4, -5]
    target = -8
    soln = [2, 4]
    fnc = Solution3()
    output = fnc.twoSum(nums, target)
    print(output)
    print(soln == output)
