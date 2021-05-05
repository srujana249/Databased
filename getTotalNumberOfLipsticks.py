def getTotalNumberOfLipsticks(numberOfLipsticks,numberOfLeftoversNeeded):
    #initializing the result variable res to zero
    res=0
    #this variable stores the leftovers which are remaining after making the lipstick with leftovers
    leftoversRemaining=0
    #Repeating the process till the numberOfLipsticks is more than 0
    while numberOfLipsticks:
        #calculating the number of lipsticks which can be created with the leftovers
        lipsticksCreated=(numberOfLipsticks+leftoversRemaining)//(numberOfLeftoversNeeded)
        #calculating the number of leftovers remaining
        leftoversRemaining=leftoversRemaining+(numberOfLipsticks-(lipsticksCreated*numberOfLeftoversNeeded))
        #adding the numberOfLipsticks sold to the res
        res+=numberOfLipsticks
        #assigning number of new lipsticks created to the variable numberOfLipsticks
        numberOfLipsticks=lipsticksCreated
    return res