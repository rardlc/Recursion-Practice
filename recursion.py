"""
Made by: Roberto A. Ruiz
Made on: 2017-03-25
The programs here all use recursive thinking. We call the functions over and over again until the problem has been completely narrowed down and returns each step with the appropriate function of each step completed.
"""

def main():
    
    #INPUT: The string we want to manipulate. The character we want to replace, and the character we want to replace it with.
    #OUTPUT:The last character of string, if its sep1 then it'll be replaced with sep2
    def replaceSep(string,sep1,sep2):
        
        #The base case. The program will cut down the sentence with each iteration. Once the sentence has length 0, then the string that was built up is returned
        if len(string) <= 0:
            return string
        
        #The program cuts from right to left. The last character ([-1]) acts as a pointer for the recursion
        #If the string finds sep1 in its last character then the string we'll return once the base case is fulfilled will have sep2 instead of sep1.
        if string[-1] == sep1:
            #Recall the function but not including the last character. That character will be joined will be returned and added to the string on the sepFunction that called it. 
            return replaceSep(string[:-1],sep1,sep2) + sep2
        return replaceSep(string[:-1],sep1,sep2) + string[-1]

    #INPUT: Number
    #OUTPUT: Following the rules, another number.
    def countSiblings(numberElves):
        
        #The base case. We follow a similar logic to that of strings by 'cutting' down the numbers after each run.
        if numberElves <= 0:
            return numberElves
        
        #Check to see if it divides evenly by two. If it does, its an even number and only gets 1+ to the overall recursion.
        if numberElves % 2 == 0:
            return 1 + countSiblings(numberElves-1)
        
        #If its not even, its odd. Add 3.
        return 3 + countSiblings(numberElves - 1)

    #INPUT: The string that will be worked on. This function is only triggered when '(' is found in
    #OUTPUT: The contents of the brackets
    def extract(string):
        
        #We're using the last character [-1] as the index once more. Once it finds the initial bracket, end the recursion.
        if string[-1] == "(":
            return "This is the string in brackets: "
        
        #Write everything until the above condition is true.
        return extract(string[:-1])+ string[-1]

    #INPUT:The string with brackets.
    #OUTPUT: The contents of the brackets
    def extractor(string):
        
        #The base case. Writing on brackets will only stop once every bracket has been found
        if len(string) <= 0:
            return string
        
        #This will start the function above which will write everything it sees until it finds the opening bracket ['(']
        if string[-1] == ")":
            return extract(string[:-1]) + " " + extractor(string[:-1])
        
        #If it doesn't find it, keep parsing.
        return extractor(string[:-1])
        
    #INPUT: The string you want to check if its a palindrome or not
    #OUTPUT: True if its a palindrome. False if it isn't.
    def palindrome(string):
        
        if len(string) <= 0:
            return True
        
        #If it sees a space then it will skip it depending on which side it comes from
        if string[0] == " ":
            return palindrome(string[1::])
        if string[-1] == " ":
            return palindrome(string[0:-1])
        
        #If there is only one character, it doesn't matter what it is.
        if len(string) <= 1:
            return True
        
        #If letters at the end and the beginning are the same then skip those values and check for the next pair of beginning and ends
        elif string[0] == string[-1]: 
            return True and palindrome(string[1:-1])
        
        #If at any point string[0] == string[-1] and no spaces, then just return False and make the whole recursion False.
        return False

    #INPUT: NOne
    #OUTPUT: Print all that stuff
    def tester():
        
       print(replaceSep("hope*you*are*enjoying*the*course", "*", " "))
       
       print(replaceSep("Hi.  I am having fun.  Are you?", ".", "!!"))
       
       print(replaceSep("popopopopo", "p", "x"))
       
       print(replaceSep("xxxxx", "o", "b"))
       
       print(countSiblings(0))
       
       print(countSiblings(100))
       
       print(countSiblings(2))
       
       print(countSiblings(5))
       
       print(countSiblings(-9))
       
       print(extractor("(hello world)"))
       
       print(extractor("My country (of origin) is Canada"))
       
       print(extractor("I do not have any parenthesis"))
       
       print(palindrome("racecar"))
       
       print(palindrome("abba"))
       
       print(palindrome("hello"))
       
       print(palindrome("redrumsirismurder"))
       
    tester()
    
main()

