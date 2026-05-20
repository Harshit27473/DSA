class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        a = set()
        b = set()
        result = []
        count = 0
        for i in range(len(A)):
            a.add(A[i])
            b.add(B[i])

            if A[i] in b:
                count += 1
            if B[i] in a and A[i]!=B[i]:
                count += 1
            result.append(count)
        return result
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        