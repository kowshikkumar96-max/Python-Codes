#check string is palindrom or not
def is_pal(s):
    return s == s[::1]
string = input()
print(is_pal(string))
