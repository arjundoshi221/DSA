class Solution:
    def reverse(self, x: int) -> int:

        MIN, MAX = -2**31, 2**31 - 1

        sign = -1 if x < 0 else 1
        
        reversed_x = 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            reversed_x = reversed_x * 10 + digit

        if reversed_x < MIN or reversed_x > MAX:
            return 0
        
        return int(reversed_x*sign)

    
        