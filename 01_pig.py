import random
#https://youtu.be/21FnnGKSRZo?t=145
def roll():
    min_value=1
    max_value=6
    roll= random.randint(min_value,max_value)

    return roll

# value=roll()
# print(value)

while True:
    players= input('enter the number of players (2-4): ')
    if players.isdigit():
        players=int(players)
        if 2 <= players <= 4:
            break
        else:
                   print('Must be between 2 to 4 players')
    else:
        print('Invalid, try again.')


# print(players)
max_score=50
players_scores=[0 for _ in range(players)]
# print(players_score)

while max(players_scores )<max_score:
     for player_indx in range (players):
        print ('\nPlayer number: ',player_indx+1, " turn has just started!")
        print('Your total score is: ',players_scores[player_indx], "\n")
        current_score=0

        while True:
            should_roll=input('Would you like to roll (y): ')
            if should_roll.lower() !="y":
                break
            
            value=roll()
            if value == 1:
                print('You rolled a 1! Your turn is done')
                current_score=0
                break
            else:
                current_score+=value
            
            print('You rolled a ',value)
            print('Your score is: ',current_score)
        players_scores[player_indx]+=current_score 
        print('Your total score is: ',players_scores[player_indx])   

max_score= max(players_scores)    
winning_indx=players_scores.index(max_score)
print ("Player number: ",winning_indx," is the winner ")
