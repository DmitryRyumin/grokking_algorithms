#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Search Insert Position (Вставка числа в отсортированный список)
"""

# ######################################################################################################################
# Импорт необходимых инструментов
# ######################################################################################################################

# Подавление Warning
import warnings
for warn in [UserWarning, FutureWarning]: warnings.filterwarnings('ignore', category = warn)

from dataclasses import dataclass # Класс данных

from typing import List # Типы данных

@dataclass
class Solution:

    # ------------------------------------------------------------------------------------------------------------------
    # Конструктор
    # ------------------------------------------------------------------------------------------------------------------

    def __post_init__(self):
        pass

    # ------------------------------------------------------------------------------------------------------------------
    # Решение задачи (https://leetcode.com/problems/search-insert-position/
    # ------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
        """Вставка числа в отсортированный список

        Args:
            nums (List[int]): Список чисел
            target (int): Вставляемое число

        Returns:
            int: Индекс вставляемого числа
        """

        low = 0 # Старт поиска
        high = len(nums) - 1 # Конец поиска

        while low <= high:
            mid = int((high - low) / 2 + low) # Индекс среднего значения в списке

            guess = nums[mid] # Число

            if guess == target: return mid # Число соответствует искомому
            elif guess > target: high = mid - 1 # Число больше искомого
            else: low = mid + 1 # Число меньше искомого

        return low

# ######################################################################################################################
# Выполняем только в том случае, если файл запущен сам по себе
# ######################################################################################################################

if __name__ == "__main__":
    lists = [
        ([1, 2, 3, 4, 5, 6, 7, 8], 3),
        ([1, 2, 3, 4, 5, 6, 7, 8], 9),
        ([1, 2, 3, 4, 5, 6, 7, 8], 15),
        ([1, 2, 3, 4, 5, 6, 7, 8], 0),
        ([2, 3, 4, 5, 6, 7, 8], 0),
        ([2, 5], 0)
    ]

    for curr in lists: print(Solution.search_insert(curr[0], curr[1]))
