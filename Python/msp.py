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

      spaces[pos[point]] = cue2  # cue2 is an array that replaces a space in the spaces array with pos (the guess) in the first location (position 0 of the pos array is the first number that shows the position of the guess in the secret array, which lines up with the spaces array) 

      point = point + 1 #We add one to point so now we are going to replace a space in the spaces array with the guess in the position described with the second number in the pos array. It then repeats because val4 isn't 1. If val4 is more than 2 numbers long, then it will repeat again. It goes until there aren't any numbers left in the val4 array. 
    
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
