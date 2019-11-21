#Andrew Worthley
#CSCI 102 - Section G
#Week 12 - Part b

def PrintOutput (output):
    print("OUTPUT", output)


def LoadFile (file):
    f = open (file , "r")
    old = []
   
    for line in f:
        old.append(line)
    return old
def UpdateString (word, letter, number):
    newstring=word[:number]+letter+ word[number+1:]
    return newstring
def main():
    PrintOutput("lol")
    print (LoadFile("a.txt"))
    print (UpdateString("Andrew", "bitch", 2))
main()
