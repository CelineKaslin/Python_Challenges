# Roman numerals come from the ancient Roman numbering system. They are based on specific letters of the alphabet which are combined to signify the sum (or, in some cases, the difference) of their values. 
# The first ten Roman numerals are:
# I, II, III, IV, V, VI, VII, VIII, IX, and X.
# The Roman numeral system is decimal based but not directly positional and does not include a zero. Roman numerals are based on combinations of these seven symbols:
# I = 1 (unus)
# V = 5 (quinque)
# X = 10 (decem)
# L = 50 (quinquaginta)
# C = 100 (centum)
# D = 500 (quingenti)
# M = 1000 (mile)

# For this task, you should return a roman numeral using the specified integer value ranging from 1 to 3999.
# Input: A number as an integer.
# Output: The Roman numeral as a string.
# ** Example:
# ** checkio(6) == 'VI'
# ** checkio(76) == 'LXXVI'
# Precondition: 0 < number < 4000

# How it is used: This is an educational task that allows you to explore different numbering systems. Since roman numerals are often used in the typography, it can alternatively be used for text generation.
# The year of construction on building faces and cornerstones is most often written by Roman numerals. These numerals have many other uses in the modern world.

def checkio(data):

    answer = ""
    Roman = {1000:"M",
             900 :"CM",
             500 :"D",
             400:"CD",
             100:"C",
             90:"XC",
             50:"L",
             40:"XL",
             10:"X",
             9:"IX",
             5:"V",
             4:"IV",
             1:"I"}
    
    while data > 0 :
        for key in Roman.keys() :
            if data / key >= 1 :
                answer += Roman[key]
                data -= key
                break
            
    return answer