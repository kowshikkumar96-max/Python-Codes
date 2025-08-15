#reverse the given sring
def rev_str(s):
    if len(s) == 0:
        return s
    return rev_str(s[1:]) + s[0]

string=input()
print(rev_str(string))
    
