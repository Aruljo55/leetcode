class Solution:
    def minimizeXor(self, num1, num2):
        # Count the number of set bits in num2
        set_bits_num2 = bin(num2).count('1')
        
        # Initialize x to 0 and determine how many set bits we need
        x = 0
        set_bits_needed = set_bits_num2
        
        # Traverse the bits of num1 from MSB to LSB
        for i in range(31, -1, -1):  # For 32-bit integers
            if set_bits_needed == 0:
                break
            if num1 & (1 << i):  # Check if the i-th bit of num1 is set
                x |= (1 << i)  # Set the i-th bit of x
                set_bits_needed -= 1
        
        # If more set bits are needed, set them from LSB upwards
        for i in range(32):
            if set_bits_needed == 0:
                break
            if not (x & (1 << i)):  # Check if the i-th bit of x is not set
                x |= (1 << i)  # Set the i-th bit of x
                set_bits_needed -= 1
        
        return x
