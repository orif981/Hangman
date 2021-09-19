import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)
print()
print()
display=[]
lives=6
word_list=["bibi","benett","lapid","ganz","shaked","smotrich","ben_gvir"]
chosen_word=random.choice(word_list)
for letter in chosen_word:
    display.append('_')
while '_' in display and lives>0:
    guess=input("Guess a letter\n")
    guess=guess.lower()
    if guess not in chosen_word or guess in display:
        print(stages[lives-1])
        print("{} is not in the word".format(guess))
        print(display)
        lives-=1
        continue
    ans=[True if letter==guess else False for letter in chosen_word]
    for i in range(len(chosen_word)):
        if ans[i]:
            display[i]=guess
    print(display)
if lives>0: print('You won!')
else: print("You lost.")


