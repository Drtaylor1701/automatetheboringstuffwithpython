#! python3
#detects strong passwords

def pwlength(pw):
    if len(pw) > 8:
        return True
    else:
        return False

def pwcaps(pw):
    if (any(x.isupper() for x in pw)) and (any(x.islower() for x in pw)):
        return True
    else:
        return False
    
def pwnum(pw):
    if (any(x.isdigit() for x in pw)):
        return True
    else:
        return False

def main():
    pwlength()
    pwcaps()
    pwnum()


print(pwlength("TctJxk0H5TJoYLSPuo4C"))
print(pwlength("111111"))
print(pwlength("aaaaaa"))

print(pwcaps("TctJxk0H5TJoYLSPuo4C"))
print(pwcaps("111111"))
print(pwcaps("aaaaaa"))

print(pwnum("TctJxk0H5TJoYLSPuo4C"))
print(pwnum("111111"))
print(pwnum("aaaaaa"))