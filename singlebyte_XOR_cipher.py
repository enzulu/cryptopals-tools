import sys
import binascii

def etaoin_scorer(plaintext):
	# determine the score of text based on letter freq
	# higher score = more readable
	common_letters = "etaoinshrdlucmfwypvbgkqjxz"
	common_len = len(common_letters)
	score = 0
	for letter in plaintext:
		for i in range(common_len):
			if (common_letters[i] == letter): 
				score += common_len - i
	
	return score

def encode_with_XOR(byte_string, byte_key):
	encoded_array = bytearray()
	
	for byte in byte_string:
		encoded_array.append(byte ^ byte_key)
		
	return encoded_array
	
def brute_force_encode(hex_text):
	byte_array_for_encoding = bytearray.fromhex(hex_text)
	score_array = []
	byte_key_array = range(0,255)
	top_key = 0
	for brute_byte_key in byte_key_array:
		encoded_byte_array = encode_with_XOR(byte_array_for_encoding,brute_byte_key)
		score = etaoin_scorer(encoded_byte_array.decode("cp437"))
		score_array.append(score)
	
	max_score = max(score_array)
	max_score_index = score_array.index(max_score)
	best_key = byte_key_array[max_score_index]
	
	#print("MAX SCORE: " + str(max_score))
	#print("BEST KEY: " + str(best_key))
	
	return [best_key, max_score]
	
	
def main():
	filename = sys.argv[1]
	file_object = open(filename, 'r')
	text_list = file_object.readlines()
	
	result_scores = []
	result_keys = []
	
	for index, string in enumerate(text_list):
		print("encoding string number " + str(index))
		if '\n' in string:
			string = string[:-1]
		current_best_key, current_best_score = brute_force_encode(string)
		
		result_keys.append(current_best_key)
		result_scores.append(current_best_score)
	
	max_score = max(result_scores)
	best_translation_index = result_scores.index(max_score)
	translation = encode_with_XOR( bytearray.fromhex(text_list[best_translation_index][:-1]), result_keys[best_translation_index] )
	print("HIDDEN MSG: " + str(translation.decode("cp437")))
if __name__ == "__main__": main()