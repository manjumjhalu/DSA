
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow case
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine result sign
        negative = (dividend < 0) != (divisor < 0)

        # Convert to positive numbers
        a = abs(dividend)
        b = abs(divisor)

        result = 0

        # Repeatedly subtract the largest doubled divisor
        while a >= b:

            temp = b
            multiple = 1

            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            a -= temp
            result += multiple

        if negative:
            result = -result

        return result
