import base64
import sys
import argparse

def convert_string(input_string, is_input_hex):

	if(is_input_hex == False):
			string_to_convert = input_string.encode("hex")
	else:
		string_to_convert = input_string

	try:
		string_in_bytes = bytearray.fromhex(string_to_convert)
	except ValueError as e:
		print "The input hex string is invalid: %s" % str(e)
	else: 
		return base64.b64encode(string_in_bytes)

def main():

	parser = argparse.ArgumentParser(description='Convert input string to base64.')
	parser.add_argument('input_string', metavar='STR',
						help='the input string to be converted to base 64')
	parser.add_argument('--hex', dest='is_input_hex', action='store_true',
						help='explicitly specify that the input is a hex string')

	args = parser.parse_args()
	
	print convert_string(args.input_string, args.is_input_hex)


if __name__ == "__main__": main()