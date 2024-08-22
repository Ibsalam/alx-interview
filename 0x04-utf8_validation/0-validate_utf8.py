#!/usr/bin/python3
"""UTF-8 validation module.
"""
def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check for the leading 1 bits in the byte
    mask1 = 1 << 7   # 10000000
    mask2 = 1 << 6   # 01000000

    # Iterate through each byte in the data
    for byte in data:
        # Get the 8 least significant bits
        byte = byte & 0xFF

        # If we are starting a new character
        if num_bytes == 0:
            # Count the number of leading 1's to determine the number of bytes in this character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # 1 byte character (ASCII)
            if num_bytes == 0:
                continue

            # UTF-8 characters are 1 to 4 bytes long, so if it's outside this range, it's invalid
            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Continuation bytes must start with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrement the number of bytes left to process in the current character
        num_bytes -= 1

    # If we've processed all bytes and ended with num_bytes being 0, it's valid
    return num_bytes == 0

