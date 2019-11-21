#Andrew Worthley
#CSCI 102 - Section G
#Week 12 - Part b

def PrintOutput (output):
    print("OUTPUT", output)


def LoadFile (file):
    f = open (file , "r")
    old = []
    new =[]
    for line in f:
        old.append(line)
    f.close()
    for i in old:
        if "\n" in i:
            length= len(i)-1
            new.append(i[:length])
        else:
            new.append(i)
    return new
def UpdateString (word, letter, number):
    newstring=word[:number]+letter+ word[number+1:]
    return newstring
def FindWordCount(a, findword):
    count=0
    for i in a:
        count+= i.count(findword)
    return count

