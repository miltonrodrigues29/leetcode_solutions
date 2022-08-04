# [1,2,1,3,2,2,5]



def printRepeating(numbers):
    HashMap = {}
    for i in numbers:
        HashMap[i] = HashMap.get(i,0) + 1
    print(HashMap)


    for i in HashMap:
        if HashMap.get(i)>1:
            print(i)

printRepeating([1,2,1,3,2,2,5])

        
