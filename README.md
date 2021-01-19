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
  **Description:** Create a program that prints the roots of a quadratic equation whose coefficients are entered by a user. (If there are no roots it will print none)
  
  **Reflection:** Math concepts can actually be helpful outside of math class. ;) Again, splitting a task into smaller steps is the way to go, especially when layers of math could potenetially obscure the issue, making it hard to know what to fix. By startin small and layering on various aspects, you have a much more straightforward troubleshooting process because you aren't dealing with too many variables at one time. Pseudocoding is a great way to break it down into small steps and not get lost in or confused by the jargon. You take each step in bite-sized pieces and are able to do specific research if you don't know the jargon but do know the logic behind the task. 
  
  
[Replit Code Link](https://repl.it/join/kppoeevc-apaquet37)  
  ```
  #Quadratic Solver
#Written by: Elisabeth Scharf and Abigail Paquette

def quadCalc(a,b,c): #We use input to receive the coefficients from the user and then send them to this function in the form of variables a,b, and c
  intA = int(a)
  intB = int(b)
  intC = int(c)
  disc = ((intB*intB)-(4*intA*intC))  #Disc stands for discriminant 
  Q1 = (-intB / (2*intA))
  if disc < 0:   #If statements move the quadratic equation in question into one of 3 buckets that determines the next steps 
    return("The function {0}x^2 + {1}x + {2} has no real roots.".format(intA, intB, intC))
  if disc == 0:
    return("The root is: {0}".format(Q1)) 
  if disc > 0:
    pos = ((disc**0.5)/(2*intA)) 
    w = round((Q1 - pos),5) # From the center, we move a certain amount in the pos and neg directions to find the roots
    x = round((Q1 + pos),5)
    return([w,x])  # Return an array of those values


while True:
    print("Enter the coefficients for ax^2 + bx + c = 0")
    a = input("Enter the first coefficient: ")
    b = input("Enter the second coefficient: ")
    c = input("Enter the third coefficient: ")
    returnVal = quadCalc(a,b,c)   # Calling the function! 
    if isinstance(returnVal,list): 
      print("Two roots:")
      for root in returnVal:
        print(root)
    else:
      print(returnVal)  
      
``` 
## Strings and Loops ## 
**Description:** Take a simple sentence and print it in a vertical orientation wtih dashes in place of spaces

**Reflection:** This code ended up being fairly simple and short, but there was a lot of research and learning that went on behind it. Length of code does not necessarily determine complexity. I learned that I need to do some more research and practice more with lists and arrays in order to be able to use them in my own projects-I see the practicality of arrays but still struggle to understand quite how to use them and make them work in a variety of contexts. 

[Replit Code Link](https://repl.it/join/lwjzafvj-escharf72) 

```
#Strings and Loops
#Written by Abby Paquette and Elisabeth Scharf

# This is the library that allows us to use arrays, which are much more efficient in storing large amounts of information than lists are
# Also I learned that you can import a library as a different word which helps keep the code clean and readable
import numpy as np 

txt = input("Type a simple sentence: ") #Prompting the user... 

letters = list(txt) # input to list 


array1 = np.array(letters) # list to array

for i in letters:
    newStr = i.replace(' ', '-') #replacing the spaces with - 
    print(newStr) #printing the modified sequence
    
``` 

## Hangman (Or Man-Shaped Piñata) ##
**Description:** Design a program that allows two users to play hangman. 

**Reflection:** This was quite a project, but it was a fun goal to work towards. This code is an excellent example of the necessity of planning and pseudocoding before sitting down to code.
This code taught me many lessons:
1. Pseudocode first and split the code into small tasks:

We did our best to split the task into small, acheivable steps (see below). This made troubleshooting easier and (maybe more importantly) kept us motivated with small victories rather than wading through a chunk of error-filled code. You can't make a tower of blocks all at once-you have to add one block at a time and make sure that each is stacked properly so it can support the ones that will be on top of it. 

2. Coding is 10% skill, 50% logic, and 40% motivation/mindset

In my years of taking engineering I have never really enjoyed the coding aspect of the class. I'm not naturally a very logical person so it requires more work for me to think through the process. But while working on the coding assignements this year, I have realized that a mindset shift is really what I need in order to begin to grow in my coding skills. I may not be the most logical person in the world, but coding helps me to build my logical reasoning and in turn the logical reasoning skills will make me a better coder. (A cycles of increasing benefits!) This assignment also taught me that I enjoy the process a lot more if I approach it as a challenge or a game that I want to do my best on. 

3. Collaborative coding is the way to go (when possible)

For this assignment I worked with a classmate and though we were occasionally treading on eachothers' toes and trying to run the code at the same time, the benefits of this collaboration made the inconveniences worth it. We were able to provide each other with motivation when the other was feeling frustrated, be a second pair of eyes to catch mistakes in the code, and be another person with whom they could verbally process the logic of a piece of code they were writing. Sometimes, if we were fed up with the specific task we were working on, we would switch assignments in order to 1. be a fresh pair of eyes on the task and 2. not go crazy or do more damage.

4.Google is your friend

I know I say this in nearly every reflection, but it is very true. There are so, so, so, so many resources out there and there is a 99% chance that someone else has experienced the same problem (or a similar problem) before. Collaboration is a crucial part of engineering- we aren't meant to create in bubble. Google is an excellent resource, especially when in-person collaboration and contact is harder. 

[Replit Code Link](https://repl.it/join/hhhiyscw-escharf72)


<img src="Media/Screenshot%202021-01-05%20at%202.00.20%20PM.png" width="500">


<img src="Media/Screenshot%202021-01-05%20at%202.00.51%20PM.png" width="500">


**Pseudocode & Planning**
```
Ok, so the small tasks:
1. Player 1 gives the word and then the screen clears
  os.system(clear) Apparently this clears the screen
  We'll probably use an input just like normal 

2. Prompt player 2 to guess a letter
  Again I think just input
  Maybe we add a "Nope!" or a "Good Job!" in as a response
  The validation/response could be part of early step 3

3. It figures out whether the letter is in the word or not
  Do we need to turn the original word input into a list, str, array, or other? (probably array because it is heavily based on position in the word?)
  It also has to recognize if it's in the word more than once
4. Find the length of the word and turn it into spaces
  Wasn't there a function for that? Yeah I think there was, maybe i? yeah, and len(i) or something like that
  Should we do this at the beginning and just store it as an array or something like that to make it easier later? Maybe yeah, I think info gathering at the start is always good

5. Fill in those spaces with the correct guesses
  It seems like we'll really need to figure out how to use arrays to access positions of values stored in the array

6. If it's incorrect, print a message and add to the image
  Sub-task: how to draw the image
  Should we make a function for this?

7. Guess counter? 
  Should we have something that keeps track of player 2's guesses (This could be one of those var = var-1 in the loop or something like that)

8. Exit if guesses = 0 OR player 2 guesses the word 

Anything else we should include in the pseudocode?
This will be a good thing to put in github 

Notes: 
  Arrays can do math, lists can't
  [square brackets create a list]
  array.sort()
  list.sort()
  for i,j in enumerate(myList):
    print(i, end_"  --  ")
    print(j)

  pop-takes off the last
  apend - add one 
  print(myList[2]) (this will print just the third element) 
```

**Final code** 
```
# Hangman code
# Written by Abby Paquette and Elisabeth Scharf

from time import sleep
import os
#from numpy import array
#import numpy as np
wrong = 0
#right = 0

  
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
  #msp = [" 0 ","\\|/ "," |","/ \\ "]
  msp = [" 0 "]
  if x >= 2:
    msp.append(" |")
  if x >= 3:
    msp.append(" |")
    #print(*msp, sep='\n')
  if x >= 4:
    msp.append("/")
  if x >= 5:
    msp.pop()
    msp.append("/ \\")
  if x >= 6:
    msp.pop(1)
    msp.insert(1, "\\|")
  if x == 7:
    msp.pop(1)
    msp.insert(1, "\\|/")
  print(*msp, sep="\n")

while "_" in spaces and wrong < 7:
  print(spaces)
  cue2 = input("Player 2, please guess a letter: ") 
 
  try: 
    
    pos = [i for i in range(len(secret)) if secret[i] == cue2] #This looks to see if it can be found more than once in the array and returns an array if so
    
    point = 0

    val4 = len(pos)  #val4 is a variable that is the length of the array (we are trying to figure out how many times the letter that was guessed is in the word)

    while val4 > 1 and val4 != point: #If there is more that one instance of the guessed letter and it is in the word, do this:
      
      spaces[pos[point]] = cue2  # cue2 is an array that replaces a space in the spaces array with pos (the guess) in the first location (position 0 of the pos array is                                   the first number that shows the position of the guess in the secret array, which lines up with the spaces array) 
      
      point = point + 1    #We add one to point so now we are going to replace a space in the spaces array with the guess in the position                                                             described with the second number in the pos array. It then repeats because val4 isn't 1. If val4 is more than 2 numbers long, then it                                      will repeat again. It goes until there aren't any numbers left in the val4 array. 
  
  spaces[pos[0]] = cue2

  
  except: 
    print("You are incorrect")
    wrong = wrong+1
    msp(wrong)
else:
 print(spaces)
 if wrong < 7:
   print("Congratulations!")
 print("Game over")
 print("The correct word was: " + word)
 
 ``` 
## GPIO Pins - SSH ##
**Description:** The goal of this assignment was to learn how to connect to your Pi via wifi instead of a cord. This opens up endless possibilities for where the Pi can go and what it can do. 

**Reflection:** This assignment wasn't long or complicated on paper, but in practice it was a seemingly endless series of issues to troubleshoot. Needless to say, patience and perseverence were necessary ingredients in this recipe. :) 

Troubleshooting tips (most are chromebook-specific): 
- Make sure that your t-cobbler is properly plugged into the Pi. Mine was backwards for a while and, needless to say, it wasn't working. 
- When detaching your Pi from the computer after enabling SSH on BeagleTerm, plug in the battery before you pull the usb cable out of the computer. I was unsuccessful in connecting a few times because my Pi turned off when I unplugged it from the computer. 
- A troubleshooting standby: if your LED isn't turning on and it seems like it should: 1. Do you have a resistor? 2. Is your wiring correct? (Look up a quick Fritzing diagram to check) 3. Could the LED be fried? (Check with a button battery or simple circuit) 4. Try another pin! Quite often pins will be broken or will only be able to be used for certain things and you just didn't know. 5. If not any of these things, then go back and check your code again. 
- The password that it asks you for in the SSH app is raspberry, not your wifi password. (It took me a very long time to figure this out :) 

<img src="Media/GPIO-SSH-CODE.png" width="500">

<img src="Media/Running-SSH-Code.png" width="500">

<img src="Media/t-cobbler.png" width="500">


## GPIO Pins - BASH ##
**Description:** As in the previous assignment, connect to the Pi over wifi through SSH but this time make two LEDs blink 10 times using BASH script.

**Reflection:** This assignment seemed easy at first, but I quickly discovered that there are layers of challenges in this simple task. It was kind of like being told to speak a simple sentence in Japanese without the aid of a Japanese speaker or Google Translate. In English you would just say it without any thought. But in order to commuicate the same thing in Japanese you need to study the characters, the pronunciation, the grammar rules, conjugation, etc. Turning on an led is about the most basic assignment one can give in the engineering world, but to do so in a new language took a lot of work to get us from the ground up to this task. 

(Hopefully) Helpful Advice:
* This task isn't simply making an LED blink, it is learning the basics of a new programming language. So approach it as such. If you were trying to say "The pink house is down the street." in Japanese, just looking up the individual words in the dictionary wouldn't be enough. You need context: How do you conjugate the verb to be? Do adjectives go before or after nouns? Is this the right word in the context? How do you do punctuation? Do I even write from left to right? I approached the task by trying to look up the "definitions" of fragmented parts and that method did not serve me well. In the end it forced me to do some research and attempt to understand the format and the context of the language. For example, I may have had all the right commands and characters, but I had incorrect spacing and so nothing was happening. I would recommend looking up websites that teach you the basics of coding in Bash script, like [this one](https://www.taniarascia.com/how-to-create-and-use-bash-scripts/) or [this one.](https://www.teknotut.com/en/first-raspberry-pi-project-blink-led/#Blink_Project)
* One step at a time. I notice that I often try to make everything happen in my first draft of code. Bad idea. For one, it makes troubleshooting a nightmare. But it's also not a good habit to build. It's so much better to start small and work your way up to the final product. For example, just see if you can turn on an LED. (That proved one of the harder tasks for me ;) Then see if you can make it blink. Then maybe comment that part out and use printing (echo in the case of bash) to figure out how to make a functioning if, for, or while loop. Then work with getting a variable or counter working. Then add the LED back in. etc. It will simplify things and help you to identify problems much more quickly. 
* I would highly recommend using the command **man gpio**. It pulls up a list of gpio commands and further down the list gives explanations of what each does and some examples. This really helped me when I knew what I wanted to do but didn't know the words to use to make it happen. 

Final code:

<img src="Media/ledBASHcode.png" width="500">

Rough Drafts and Experimental Code: 

<img src="Media/ledBASHroughDrafts.png" width="500">

## GPIO Pins - Python##
**Description:** Make two LEDs blink using Python instead of Bash. 

**Reflections:** After writing a whole paragraph for the previous assignment (see above) about how you should take things one step at a time and not try to do everything at first, I ignored my own advice, and... nothing worked. (Go figure ;) But hey, I proved that the steps that I theorized from the past assignment were correct! 
Once I learned my lesson, I began from the beginning, just trying to make one LED turn on. I used the print() function, which is invaluable when it comes to troubleshooting code. It showed me that it was entering the while true loop and there weren't errors, but still my LED wouldn't turn on. So I backtracked even more. I went back to my bash assignment and ran it to make sure that my led wasn't dead or anything like that. It turned out that my t-cobbler was attached to the Pi backwards, so nothing happened. Once I got that sorted out and knew that the LED was functioning, I went back to my Python code. From the bash asssignment, I knew that there was something funky about calling pins and which numbers actually meant which physical pins. And I had solved that with a -g in bash. So I looked, and found a command, but I guess it wasn't what I thought it was. So finally, I looked up a diagram **see below** and realized that my code was working fine but I was just wired to the wrong pin. After that, adding a second LED was super quick. I decided to make them alternate flashing, just because. 

Final code:

<img src="Media/gpioPythonCode.png" width="500">

Gpio pin diagram:

<img src="Media/gpioPinDiagram.png" width="500">




