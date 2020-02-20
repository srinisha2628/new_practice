s = "azcbobobegghakl"
s1 = "bob"
count = 0
for i in range(0,len(s)):
    if s1 in s[i:i+3]:
        count = count +1
print(count)
