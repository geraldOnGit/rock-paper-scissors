import random

def makeChoice():
    player_choice = input("pick one: 'rock', 'paper', 'scissors'\n")
    options = ['rock', 'paper', 'scissors']
    computer_choice = options[random.randint(0,2)]
    choices = {'player': player_choice, 'computer': computer_choice}
    print(f"you chose {player_choice}, computer chose {computer_choice}.")
    return choices

def check(player, computer):
    if player == computer:
        return "it's a tie!"
    if player == 'rock':
        if computer == 'paper':
            return "paper covers rock! you lose."
        return "rock smashes scissors! you win."
    if player == 'paper':
        if computer == 'scissors':
            return "scissors cut paper! you lose."
        return "paper covers rock! you win."
    if computer == 'rock':
        return "rock smashes scissors! you lose."
    return "scissors cut paper! you win."

game = makeChoice()
print(check(game['player'], game['computer']))
    