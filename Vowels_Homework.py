userlist = input("Please enter a message, whether random characters or grammatical sentence. ")

def vowelcount(userlist):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    count = 0
    for i in userlist:
        if i in vowels:
            count += 1
    print("There are",count,"vowels in the sequence!")

vowelcount(userlist)