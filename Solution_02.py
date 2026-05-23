def is_palindrome(s):
    tolower = s.replace(" ", "").lower()

    res = tolower
    rev = tolower[::-1]

    return res == rev 

s= "A man a plan a canal Panma"
res = is_palindrome(s)
print(res)  