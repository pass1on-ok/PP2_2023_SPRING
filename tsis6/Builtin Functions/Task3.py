def Palindrome(string):
    rev_str = string[::-1]
    if string.lower() == rev_str.lower():
        return True

    else:
        return False

string = input()
print(Palindrome(string))
