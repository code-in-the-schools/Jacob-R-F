V = ("a","e","i","o","u")

I = str(input("The word is..."))

uI = I.lower()

print(uI)

for i in range(len(I)):
  if I[i] in V:
    print(I[i], " : Vowel")
  else:
    print(I[i], " : Consonant")

