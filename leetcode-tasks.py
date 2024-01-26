# 1. Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Создаем пустой словарь, в котором будем хранить числа и их индексы
        num_map = {}
        
        # Проходимся по элементам списка nums и их индексам, используя функцию enumerate
        for i, num in enumerate(nums):
            # Вычисляем разницу между целевым значением и текущим числом
            complement = target - num
            # Проверяем, есть ли разница в словаре num_map
            if complement in num_map:
                # Если разница уже есть в словаре, значит, мы нашли пару чисел,
                # сумма которых равна целевому значению, и возвращаем их индексы
                return [num_map[complement], i]
            # Добавляем текущее число в словарь num_map, используя число как ключ и индекс как значение
            num_map[num] = i
        
        # Если не найдено пар чисел, сумма которых равна целевому значению, возвращаем пустой список
        return []

# or

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)

        for i in range(len(x_str)):
            if x_str[i] != x_str[-i-1]:
                return False
        return True

# or

class Solution:
    def isPalindrome(self, x: int) -> bool:
        result = 0
        while x > 0:
            ostatok = x % 10
            x = x // 10
            result = result + ostatok
            return result
            
# 13. Roman to Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        result = 0
        i = 0

        while i < len(s):
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
                result += roman_map[s[i+1]] - roman_map[s[i]]
                i += 2
            else:
                result += roman_map[s[i]]
                i += 1

        return result

# 26. Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        unique = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[unique]:
                unique += 1
                nums[unique] = nums[i]
        return unique + 1

# 27. Remove Element

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
    
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return left

# 66. Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ''.join(str(num) for num in digits)
        result = int(digits_str)
        result += 1
        digits_list = [int(digit) for digit in str(result)]
        return digits_list

# 88. Merge Sorted Array

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()
        while 0 in nums1:
            nums1.remove(0)
        return nums1
    
# or
    
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()
        nums1 = [num for num in nums1 if num >= 0]
        return nums1

# 121. Best Time to Buy and Sell Stock
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
        
        return max_profit

# 2520. Count the Digits That Divide a Number

class Solution:
    def countDigits(self, num: int) -> int:
        num_str = str(num)
        count = 0
        for digit in num_str:
            digit_num = int(digit)

            if digit_num != 0 and num % digit_num == 0:
                count += 1
        return count
