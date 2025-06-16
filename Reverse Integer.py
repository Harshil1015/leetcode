class Solution:
    def reverse(self, x: int) -> int:
        string_number = str(abs(x))        # Convert number to string, use abs to ignore sign
        total = 0
        length = len(string_number)

        for i in range(length):
            digit = int(string_number[i])  # Convert each character back to integer
            total += digit * (10 ** i)     # Rebuild the reversed number manually

        # Apply sign
        if x < 0:
            total = -total

        # Handle 32-bit integer overflow
        if total < -2**31 or total > 2**31 - 1:
            return 0

        return total
