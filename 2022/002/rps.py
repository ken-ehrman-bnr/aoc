FILE_NAME = './strategy.dat'
#FILE_NAME = './test.dat'

THEIR_ROCK = 'A'
THEIR_PAPER = 'B'
THEIR_SCISSORS = 'C'

MY_ROCK = 'X'
MY_PAPER = 'Y'
MY_SCISSORS = 'Z'

WIN = 6
LOSE = 0
DRAW = 3

move_choice_scores = {MY_ROCK: 1, MY_PAPER: 2, MY_SCISSORS: 3}


match_outcomes = {
    THEIR_ROCK: { MY_ROCK: DRAW, MY_PAPER: WIN, MY_SCISSORS: LOSE },
    THEIR_PAPER: { MY_ROCK: LOSE, MY_PAPER: DRAW, MY_SCISSORS: WIN },
    THEIR_SCISSORS: { MY_ROCK: WIN, MY_PAPER: LOSE, MY_SCISSORS: DRAW } 
}

with open(FILE_NAME, 'r') as f:
    score = 0
    for line in f:
        (their_move, my_move) = line.strip().split()
        outcome = match_outcomes[their_move][my_move] + move_choice_scores[my_move]
        score += outcome
        print(their_move, my_move, outcome, score)
    
    print (score)