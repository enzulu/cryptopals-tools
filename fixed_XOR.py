import sys

#2 inputs only
if len(sys.argv) != 3:
	raise TypeError("incorrect number of inputs")

if len(sys.argv[1]) != len(sys.argv[2]):
	raise TypeError("length of two inputs are not the same")
	
stringA = sys.argv[1]
stringB = sys.argv[2]
print("HEX STRING A: " + stringA)
print("HEX STRING B: " + stringB + "\n")

bytestringA = bytearray.fromhex(stringA)
bytestringB = bytearray.fromhex(stringB)
print("BYTE STRING A: " + bytestringA)
print("BYTE STRING B: " + bytestringB + "\n")

hexintA = int(stringA, 16)
hexintB = int(stringB, 16)

XOR_result = hexintA ^ hexintB
print("A xor B: " + str(hex(XOR_result)))

