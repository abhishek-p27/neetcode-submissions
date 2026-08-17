class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_1 = 0
        index_2 = len(numbers) - 1
        while index_1 < index_2:
            if (numbers[index_1] + numbers[index_2]) == target:
                return [(index_1 + 1), (index_2 + 1)]
            elif (numbers[index_1] + numbers[index_2]) > target: 
                index_2 -= 1
            else: 
                index_1 += 1
    