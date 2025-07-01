class Solution:
    def validUtf8(self, data) -> bool:
        count = 0  # Number of bytes to validate

        for num in data:
            byte = num & 0xFF  # Only least significant 8 bits

            if count == 0:
                # Count the number of leading 1s
                mask = 0x80  # 10000000
                while mask & byte:
                    count += 1
                    mask >>= 1

                if count == 0:
                    continue

                if count == 1 or count > 4:
                    return False
                count -= 1  # For the first byte already processed
            else:
                # Check if it starts with '10'
                if not (byte & 0x80 and not (byte & 0x40)):
                    return False
                count -= 1

        return count == 0