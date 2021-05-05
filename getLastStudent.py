def getLastStudent(numberOfStudents,treats,startingChair):
    #calculating the lastStudent position using startingChair and number of treats
    lastStudent=startingChair+(treats-1)
    #ReCalculating the correct lastStudent position if the lastStudent position is greater than numberOfStudents
    if lastStudent>numberOfStudents:
        lastStudent=lastStudent-(numberOfStudents*(lastStudent//numberOfStudents))
    #returning the last student position if the obtained student position is zero
    if lastStudent==0:
        return numberOfStudents
    return lastStudent