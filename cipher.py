def cipher(num_shift, string):
	mod_10 = num_shift%10
	mod_26 = num_shift%26
	chars = list(string)
	for i in range(len(chars)):
		if chars[i].isupper():
			chars[i] = chr(ord('A') + (ord(chars[i]) - ord('A') + mod_26)%26)
		elif chars[i].islower():
			chars[i] = chr(ord('a') + (ord(chars[i]) - ord('a') + mod_26)%26)
		elif chars[i].isdigit():
			chars[i] = chr(ord('0') + (ord(chars[i]) - ord('0') + mod_10)%10)
	return "".join(chars)

print cipher(-1, "abc")
print cipher(1,"XYZ")
print cipher(100001, "123")