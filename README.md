# Engineering_4_Notebook
My Engineering 4 Repository 

## Get Your Pi Online ##
**Description:** The goal of this assignment was to get your pi connected to the internet and then use that connection to send some code to github. 

**Reflection:** This assignment took me a very long time, as I kept running into issue after issue. My takeaway from the work on this assignment is that there is always more than one way to do something, so if the common/easy way doesn't work, look to see how you can work around it, and when in doubt, go as close to the heart of the issue as possible. 

## Hello Python ##
**Description:** The goal of this assignment was simply to create a system that would roll a die (provide a random number from 1-6) when the enter key was pressed and exit the program when x and enter were pressed. 

**Reflection:** This program ended up being very simple-less than 15 lines of code-but it took a while to figure out the correct syntax and logic to make it run properly. I learned that it is super helpful to take a break every so often and just talk yourself through the code. There were times were I was so frustrated because the code didn't seem to be working properly and I would read through it and realize that the logic was out of order. I get caught up in syntax and forget to zoom out a bit and make sure my process is correct. I will be using this process with future code before jumping into syntaxland. 

[Replit Code Link](https://repl.it/join/wmpjgxqi-escharf72) 

```
# Automatic Dice Roller
# Written by Elisabeth Scharf 
from random import randint 
#including this library gave me access to the functions that provided the random number for the dice roll 
import time

print ("Automatic Dice Roller") 
#Using the print function makes it easier to troubleshoot code and more straightforward for the user 

while(True):
  time.sleep(.25) #Just so the loop isn't running too fast
 
  text = input("Press enter to roll or x and enter to exit") #This establishes instructions for the input that I will check for later in the code 

  if text == (""): #The quotes indicate the user pressing the enter key on the keyboard
    print(randint(1,6))

  if text == ("x"): 
    exit() 
    
 ``` 
 
 ## Calculator ##
 **Description:** Create a program that find the sum, difference, product, quotient, and modulo of two numbers entered by the user. The two numbers will go through one function five times and print the proper numbers. 
 **Reflection:** Troubleshooting is a universally helpful skill. This code required a lot of troubleshooting and simplifying to make sure that we weren't tackling too many variables at the same time. Printing is the best way to get feedback and figure out where the disconnect is within the code and simplifying (commenting out) your code can help you isolate the issue. Learning these skills on simpler and shorter codes will serve us well in the future when we encounter problems in our code.
 
 [Replit Code Link](https://repl.it/join/kkywjvjm-escharf72) 
 ```
#Calculator Code
#Written by: Abigail Paquette and Elisabeth Scharf

num = 1 #num is a simple variable that we use to determine when the calculator cycle has run its course and it is time to prompt the user for more numbers

#this is the aptly named doMath function. We send it three values that it needs in order to perform its tasks: the two numbers and a number corresponding to the opperation it is supposed to perform 
def doMath(a,b,c):   
  int1 = int(a)
  int2 = int(b)
  rep = int(c)
  
  if rep == 1:
    return("The sum is: " + str(int1 + int2))
  if rep ==2:
    return("The difference is:" + str(int1-int2))
  if rep == 3:
    return("The product is:" + str(int1*int2))
  if rep == 4:
    div = round((int1/int2),2)   
    return("The quotient is:" + (str(div)))
  if rep == 5:
    return("The modulo is:" + str(int1%int2))


while True:
  if num == 1:
    a = input("Please enter you first number:")
    b = input("Please enter your second number:")
    num = 2
  print(doMath(a,b,1))
  print(doMath(a,b,2))
  print(doMath(a,b,3))
  print(doMath(a,b,4))
  print(doMath(a,b,5))
  num = 1
  
  ``` 
  
  ## Quadratic Solver ##
  **Description:**
  **Reflection:**
  
  
[Replit Code Link](https://repl.it/join/kppoeevc-apaquet37)  
  ```
  #Quadratic Solver
#Written by: Elisabeth Scharf and Abigail Paquette

def quadCalc(a,b,c):
  intA = int(a)
  intB = int(b)
  intC = int(c)
  disc = ((intB*intB)-(4*intA*intC))
  Q1 = (-intB / (2*intA))
  if disc < 0:
    return("The function {0}x^2 + {1}x + {2} has no real roots.".format(intA, intB, intC))
  if disc == 0:
    return("The root is: {0}".format(Q1))
  if disc > 0:
    pos = ((disc**0.5)/(2*intA))
    w = round((Q1 - pos),5)
    x = round((Q1 + pos),5)
    return([w,x])


while True:
    print("Enter the coefficients for ax^2 + bx + c = 0")
    a = input("Enter the first coefficient: ")
    b = input("Enter the second coefficient: ")
    c = input("Enter the third coefficient: ")
    returnVal = quadCalc(a,b,c)
    if isinstance(returnVal,list):
      print("Two roots:")
      for root in returnVal:
        print(root)
    else:
      print(returnVal)  
      
``` 
## Strings and Loops ## 
**Description:**

**Reflection:** 

[Replit Code Link](https://repl.it/join/lwjzafvj-escharf72) 

```
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
    
``` 

## Hangman ## 
**Description:**  

**Reflection:** 

[Replit Code Link](https://repl.it/join/hhhiyscw-escharf72) 
```
# Hangman code
# Written by Abby Paquette and Elisabeth Scharf

#So technically we have a function and everything that we need I think for this code. We might be done?? 

from time import sleep
import os
from numpy import array
import numpy as np
wrong = 0
right = 0
point = 0
  
# Player 1 word request 
word = input("Player 1, type in the secret word: ")
length = len(word)
secret = list(word)
sleep(2)
os.system('clear') 
val = word
spaces = ['_'] * length
# spaces = np.array(repr('_ '*len(val)))

#printing the msp
def msp (x):
  msp = [" 0 ","\\|/ "," |","/ \\ "]
  if x == 2:
    print(msp[0])
  if x == 3:
    print(msp[0])
    print(msp[1])
  if x == 4:
    print(msp[0])
    print(msp[1])
    print(msp[2])
  print(msp[x-1])

while "_" in spaces and wrong < 4:
  print(spaces)
  cue2 = input("Player 2, please guess a letter: ") 
  try: 
    pos = secret.index(cue2)
    pos2 = [i for i in range(len(secret)) if secret[i] == cue2]
    print(pos2)
    
    val4 = len(pos2)
    while val4 > 1 and val4 != point:
      spaces[pos2[point]] = cue2
      point = point + 1
    spaces[pos] = cue2

  
  except: 
    print("You are incorrect")
    wrong = wrong+1
    msp(wrong)
else:
 print(spaces)
 if wrong < 4:
   print("Congratulations!")
 print("Game over")
 
 ``` 
