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
        
