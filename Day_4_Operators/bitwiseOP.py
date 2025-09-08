# bitwise operators perform operations on binary representations of integers.
# They operate at the bit level, manipulating individual bits of the numbers.
# Here are the common bitwise operators in Python:
# types of bitwise operators:
# & : bitwise AND - sets each bit to 1 if both bits are 1
a = 5  # binary: 0101
b = 3  # binary: 0011
print("a & b:", a & b)  # Output: 1 (binary: 0001)
# | : bitwise OR - sets each bit to 1 if one of the bits is 1
print("a | b:", a | b)  # Output: 7 (binary: 0111)
# ^ : bitwise XOR - sets each bit to 1 if only one of the bits is 1
print("a ^ b:", a ^ b)  # Output: 6 (binary: 0110)
# ~ : bitwise NOT - inverts all the bits
print("~a:", ~a)  # Output: -6 (binary: ...11111010)
print("~b:", ~b)  # Output: -4 (binary: ...11111100)
# << : left shift - shifts the bits to the left, adding zeros on the right
print("a << 1:", a << 1)  # Output: 10 (binary: 1010)
print("b << 2:", b << 2)  # Output: 12 (binary: 1100)
# >> : right shift - shifts the bits to the right, discarding bits on the right
print("a >> 1:", a >> 1)  # Output: 2 (binary: 0010)
print("b >> 1:", b >> 1)  # Output: 1 (binary: 0001)
# Example with larger numbers:
x = 29  # binary: 0001 1101
y = 15  # binary: 0000 1111
print("x & y:", x & y)  # Output: 13 (binary: 0000 1101)
print("x | y:", x | y)  # Output: 31 (binary: 0001 1111)
print("x ^ y:", x ^ y)  # Output: 18 (binary: 0001 0010)
print("~x:", ~x)        # Output: -30 (binary: ...11100010)
print("x << 2:", x << 2)  # Output: 116 (binary: 0111 0100) a*n
print("y >> 1:", y >> 1)  # Output: 7 (binary: 0000 0111)  a**n/n
# Note: Bitwise operators are primarily used in low-level programming, cryptography, and performance-critical applications.