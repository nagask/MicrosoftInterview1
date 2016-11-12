def cipher(num_shift, string):
	mod_10 = num_shift%10
	mod_26 = num_shift%26
	chars = list(string)
	for i in range(len(chars)):
		#to increase readablitily I used python's isupper, islower, and isdigit string functions instead of bounds checking the ascii char.
		#Also, again to increase readability, I used python's ord function to get the ascii starting point of the three sequences
		if chars[i].isupper():
			chars[i] = chr(ord('A') + (ord(chars[i]) - ord('A') + mod_26)%26)
		elif chars[i].islower():
			chars[i] = chr(ord('a') + (ord(chars[i]) - ord('a') + mod_26)%26)
		elif chars[i].isdigit():
			chars[i] = chr(ord('0') + (ord(chars[i]) - ord('0') + mod_10)%10)
	#the proper method to combine a list of characters is to use "".join
	return "".join(chars)

print cipher(-1, "abc")#prints zab
print cipher(1,"XYZ")#prints YZA
print cipher(100001, "123")#prints 234