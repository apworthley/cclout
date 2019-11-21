#Andrew Worthley
#CSCI 102 - Section G
#Week 12 - Part b


##############################################################################
##############################################################################

def PrintOutput (output):
    print("OUTPUT", output)

##############################################################################
##############################################################################

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

##############################################################################
##############################################################################

def UpdateString (word, letter, number):
    newstring=word[:number]+letter+ word[number+1:]
    return newstring

##############################################################################
##############################################################################

def FindWordCount(a, findword):
    count=0
    for i in a:
        count+= i.count(findword)
    return count

##############################################################################
##############################################################################

def ScoreFinder( players, scores, name):
    name.lower()
    lplayers=[]
    for i in players:
        lol=i.lower()
        lplayers.append(lol)
    if name not in lplayers:
        return "player not found"
    else:
        index = lplayers.index(name)
        fscore= scores[index]
        output = name +" got a score of "+ str(fscore)
        return output

##############################################################################
##############################################################################

def Union (list1, list2):
    list3 = list1 + list2
    return list3

       

