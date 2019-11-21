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
"""def main():
    PrintOutput("lol")
    print (LoadFile("a.txt"))
main()"""
