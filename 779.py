class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        reverse = True
        n = 2**(n-1)
        while n!=1:
            n = n//2
            if k>n:
                k -=n
                reverse = not reverse
        return 0 if reverse else 1
