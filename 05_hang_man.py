#https://youtu.be/4TZ1K8EHT2M?t=589

import random

words =['python','java','kotlin','javascript','ruby','swift']

#randomly choose a word from the list

chosen_word = random.choice(words)
word_display = ['_' for  _ in chosen_word]# create a list of underscore
attempts= len(chosen_word)+2 # number of allowed attempts

print('Welcome to Hangman')
while attempts > 0 and '_' in word_display:
    print('\n'+ ' '.join(word_display))
    guess = input ('Guess a letter: ').lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter==guess:
                word_display[index]=guess #reveal letter
    else:
        print("That letter doesn't appear in the word")
        attempts-=1


 #Game conclusion
if '_' not in word_display:
    print("You guess the word!")
    print(' '.join(word_display))
    print('You survived!')
else:
    print('You ran out of attempts. The word was: '+ chosen_word)
    print('You lost!')      
