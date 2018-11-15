# You are given an expression with numbers, brackets and operators. For this task only the brackets matter.
# Brackets come in three flavors: "{}" "()" or "[]". Brackets are used to determine scope or to restrict some expression.
# If a bracket is open, then it must be closed with a closing bracket of the same type. The scope of a bracket must not intersected by another bracket.
# In this task you should make a decision, whether to correct an expression or not based on the brackets. Do not worry about operators and operands.
# Input: An expression with different of types brackets as a string (unicode).
# Output: A verdict on the correctness of the expression in boolean (True or False).
# ** Example :
# ** checkio("((5+3)*2+1)") == True
# ** checkio("{[(3+1)+2]+}") == True
# Precondition: 
# There are only brackets ("{}" "()" or "[]"), digits or operators ("+" "-" "*" "/").
# 0 < len(expression) < 103
# How it is used: When you write code or complex expressions in a mathematical package, you can get a huge headache when it comes to excess or missing brackets. This concept can be useful for your own IDE.

def checkio(expression):
    
    opening = ("(", "[", "{")
    closing = (")", "]", "}")
    opening_list = []
    matching = {"(" : ")",
                "[" : "]",
                "{" : "}"}
    
    for i in expression :
        if i in opening :
            opening_list.append(i)
        if i in closing :
            if len(opening_list) == 0 :
                return False
            x = opening_list.pop()
            if matching[x] != i :
                return False
    if len(opening_list) > 0 :
        return False
        
    return True
