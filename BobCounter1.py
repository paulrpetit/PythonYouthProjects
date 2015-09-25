bob = 0
s = "azcbobobegghakl"
for i in range(1, len(s)):
	if s[i] == "b":
		if s[i + 1] == "o":
			if s[i + 2] == "b":
				bob += 1
	else:
		continue
print bob

			
				