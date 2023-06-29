



#---------------------------------------------------------------------------------
#----------------- Function Recursion--------------------------------------------
#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#----- To Understand Recursion, You need to First Understand Recursion------------
#-----------------------------------


# Test Woed [wwwoooooooorldd] # 

# x = "wwwoooooooorrrldd"

# # print(x[1:]) # wwoooooooorrrldd



def cleanWord(word) :
    if len(word) == 1 :
        return word
    print(f"Print Start Function {word}") # Print Start Function wwwoooooooorldd

    if word[0] == word[1] : 
        print(f"Print before Condition {word}")  # Print Start Function wwwoooooooorldd  # Print before Condition wwwoooooooorldd

    #     return cleanWord(word[1:]) # Print Start Function woooooooorldd
    # print(f"Print before Return {word}") # Print before Return woooooooorldd
    # return word[0] + cleanWord(word[1:]) #
    
# Print Start Function wwwoooooooorldd
# Print before Condition wwwoooooooorldd
# Print Start Function wwoooooooorldd
# Print before Condition wwoooooooorldd
# Print Start Function woooooooorldd
# Print before Return woooooooorldd
# Print Start Function oooooooorldd
# Print before Condition oooooooorldd
# Print Start Function ooooooorldd
# Print before Condition ooooooorldd
# Print Start Function oooooorldd
# Print before Condition oooooorldd
# Print Start Function ooooorldd
# Print before Condition ooooorldd
# Print Start Function oooorldd
# Print before Condition oooorldd
# Print Start Function ooorldd
# Print before Condition ooorldd
# Print Start Function oorldd
# Print before Condition oorldd
# Print Start Function orldd
# Print before Return orldd
# Print Start Function rldd
# Print before Return rldd
# Print Start Function ldd
# Print before Return ldd
# Print Start Function dd
# Print before Condition dd
# world

print(cleanWord("wwwoooooooorldd")) # woooooooorldd # world






