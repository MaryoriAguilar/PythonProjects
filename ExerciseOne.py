import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True: 
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if players >= 1 and players <= 4 :
            break
        else:
            print("Must be between 1 - 4 players")
            
    else:
        print ("Invalid, insert a number. Try again.")

max_score = 10
players_scores = [0 for _ in range(players)]

while max(players_scores) < max_score:
    
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!\n")
        print("Your total score is:", players_scores[player_idx], "\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                break
            else:
                current_score += value
                print("You rolled a:", value)
                if current_score > max_score:
                    print("You have passed the max score. salupue")
                    current_score = 0
                    players_scores[player_idx] = 0
                    
                    break
            
            print("Your score is:", current_score)
        
        players_scores[player_idx] += current_score
        print("Your total score is:", players_scores[player_idx])
        
max_score = max(players_scores)
winning_idx = players_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner whit a score of:", max_score)

        