# A trio of friend dug around a treasure chest and pulled it out of the hole and wiped the dirt off. Sofia tried grabbing the lid but it was locked. They studied the locking mechanism.
# “I’ve seen this type of lock before. It’s pretty simple. We just need to check whether there is a sequence of 4 or more matching numbers and output a bool.”
# You are given a matrix of NxN (4≤N≤10). You should check if there is a sequence of 4 or more matching digits. 
# The sequence may be positioned horizontally, vertically or diagonally (NW-SE or NE-SW diagonals).
# Input: A matrix as a list of lists with integers.
# Output: Whether or not a sequence exists as a boolean.
# ** Example : 
# ** checkio([[1, 2, 1, 1], [1, 1, 4, 1], [1, 3, 1, 6], [1, 7, 2, 5]]) == True
# Precondition:
# 0 ≤ len(matrix) ≤ 10
# all(all(0 < x < 10 for x in row) for row in matrix)
# How it is used: This concept is useful for games where you need to detect various lines of the same elements (match 3 games for example). This algorithm can be used for basic pattern recognition.

def checkPos(x,y,matrix):

    myNumber = matrix[y][x]
    if ((len(matrix[y]) - x) >= 4):
        horizontalMatch = True
        for count in range(1,4):
            if (matrix[y][x + count] != myNumber):
                horizontalMatch = False
                break
        if (horizontalMatch == True):
            return True        
    if ((len(matrix[y]) - x) >= 4 and len(matrix) - y >= 4):
        diagonalMatch = True
        for count in range(1,4):
            if (matrix[y + count][x + count] != myNumber):
                diagonalMatch = False
                break
        if (diagonalMatch == True):
            return True  
    
    if ((x) >= 3 and len(matrix) - y >= 4):
        diagonalMatch = True
        for count in range(1,4):
            if (matrix[y + count][x - count] != myNumber):
                diagonalMatch = False
                break
        if (diagonalMatch == True):
            return True   
            
            
    if ((len(matrix) - y) >= 4):
        verticalMatch = True
        for count in range(1,4):
            if (matrix[y + count][x] != myNumber):
                verticalMatch = False
                break
        if (verticalMatch == True):
            return True
    return False

def checkio(matrix):

    length = len(matrix)
    for y in range(0,length):
        for x in range(0,length):
             if (checkPos(x,y,matrix) == True):
                return True
    return False
   