# Hangman code
# Written by Abby Paquette and Elisabeth Scharf

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
 print("The correct word was: " + word)
