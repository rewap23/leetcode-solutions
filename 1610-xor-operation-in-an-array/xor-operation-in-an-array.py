class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        i = 0
        while n > 0:
            ans ^= (start + (2*i))
            i += 1
            n -= 1
        return ans