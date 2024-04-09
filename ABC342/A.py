s = input()

if (s[0] != s[1]):
  if (s[0] != s[2]):
    print("1")
  if (s[0] == s[2]):
    print("2")
else:
  for i in range(len(s)):
    if (s[0] != s[i]):
      print(i+1)
