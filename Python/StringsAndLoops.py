#Strings and Loops
#Written by Abby Paquette and Elisabeth Scharf

# This is the library that allows us to use arrays, which are much more efficient in storing large amounts of information than lists are
import numpy as np 

txt = input("Type a simple sentence: ") #Prompting the user... 

letters = list(txt) # input to list


array1 = np.array(letters) # list to array

for i in letters:
    #str(i).replace((array1[2]), '-')
    #txt.split(" ") # splitting it up at the spaces
    newStr = i.replace(' ', '-') #replacing the spaces with - 
    print(newStr) #printing the modified sequence
