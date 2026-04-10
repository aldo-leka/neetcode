# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        # in: 4, 3, 2, 1
        # 3, 4, 2, 1 -> 3, 2, 4, 1
        # 2, 3, 4, 1 -> 2, 3, 1, 4 -> 2, 1, 3, 4
        # 1, 2, 3, 4
        if not pairs:
            return []
        states = [pairs[:]]
        for i in range(1, len(pairs)):
            j = i - 1
            while j >= 0 and pairs[j + 1].key < pairs[j].key:
                tmp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = tmp
                j -= 1
            states.append(pairs[:])
        return states