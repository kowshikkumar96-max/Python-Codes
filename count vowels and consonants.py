text = input("Enter a string: ")
vowels = "aeiouAEIOU"
v = 0
c = 0

for ch in text:
    if ch in vowels:
        v += 1
    else:
        c += 1

print("Vowels:", v)
print("Consonants:", c)
