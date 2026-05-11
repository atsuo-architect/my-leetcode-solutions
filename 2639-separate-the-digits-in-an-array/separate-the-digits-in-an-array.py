class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            for char in list(str(num)):
                result.append(int(char))
        return result