class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        
        reversed_x = 0
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            reversed_x = reversed_x * 10 + digit

        return int(reversed_x*sign)

    
        