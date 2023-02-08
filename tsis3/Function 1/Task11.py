def palindrome(sentence):
    if sentence == sentence[::-1]:
        print("Yes")
    else:
        print("No")

snt = input()

palindrome(snt)
