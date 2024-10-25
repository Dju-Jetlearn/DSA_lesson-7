vowels = ["a","e","i","o","u"]
userlist = input("Please enter a message, whether random characters of grammatical sentence. ")

for i in userlist:
    if i in vowels:
        print("A vowel is present.")