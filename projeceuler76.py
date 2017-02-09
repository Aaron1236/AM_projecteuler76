#STATUS: READY!
#ANSWER: 190,569,291

"""
It ia possible to write five as a sum in exactly six different ways:
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers
"""
###############################
def leftloc(cow):
#returns position of right most number greater than 1
    for i in range(len(cow)):
        if cow[i] is 1:
            return i - 1
        if i is len(cow)-1:
            return i

###############################
#INITIALLIZATIONS
n = 0
limit = 100
prevS = [limit]
i = 0 #counts the number of different combinations
#n = left most position that is greater than 1
while prevS[0] != 1:
#loop for each combination
    n = leftloc(prevS)
    #Subtract 1 from the left most position that is greater than 1
    prevS[n] -= 1
    #Clear all numbers right of n
    del prevS[n+1:]
    #Find sum of all positions
    while sum(prevS) < limit:
        if limit - sum(prevS) < prevS[n]:
            prevS.append(limit - sum(prevS))
        if limit - sum(prevS) >= prevS[n]:
            prevS.append(prevS[n])
        n += 1
    i += 1
print("i  ", i)




