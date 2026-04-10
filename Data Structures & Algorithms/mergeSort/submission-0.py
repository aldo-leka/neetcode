# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    #3,2,3
    #3 | 2,3
    #3 | 2 | 3
    #3

    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        m = len(pairs) // 2
        print(pairs)
        l = self.mergeSort(pairs[0:m])
        r = self.mergeSort(pairs[m:len(pairs)])
        print(f"l: {l}, r: {r}")

        return self.merge(l, r)

    def merge(self, l: List[Pair], r: List[Pair]) -> List[Pair]:
        li, ri = 0, 0
        n = len(l) + len(r)
        list = []

        for i in range(0, n):
            if li > len(l) - 1:
                list.append(r[ri])
                ri += 1
                continue
            
            if ri > len(r) - 1:
                list.append(l[li])
                li += 1
                continue

            if l[li].key <= r[ri].key:
                list.append(l[li])
                li += 1
            else:
                list.append(r[ri])
                ri += 1

        return list