pythStr = bytearray(b"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.")

# "chr" will convert a number to a character ord will get the number

i = 1
output = ''

for letter in pythStr[:]: # you use [:] to make a copy so you don't fk around making the thing longer or whatever in your loop if you operate on it
	if letter in range(97, 123):
		newletter = (((letter - 97) + 2)%26) + 97
	else:
		newletter = letter
	output = output + chr(newletter)


print(output)

