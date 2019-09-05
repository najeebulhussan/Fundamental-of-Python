title=input ("enter some string fot title")

while not title.istitle():
    title = input("Enter a title: ")
    if title.istitle():
        print("\""+title+"\"", "is a proper title")
    else:
        print("Try again:","\""+title+"\"", "is not a proper title")
