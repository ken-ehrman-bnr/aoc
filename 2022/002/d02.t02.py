FILE_NAME = './strategy.dat'
#FILE_NAME = './test.dat'

THEIR_ROCK = 'A'
THEIR_PAPER = 'B'
THEIR_SCISSORS = 'C'

MY_ROCK = 'X'
MY_PAPER = 'Y'
MY_SCISSORS = 'Z'

LOSE = 'X'
DRAW = 'Y'
WIN = 'Z'

WIN_SCORE = 6
LOSE_SCORE = 0
DRAW_SCORE = 3

move_choice_selection = {
    THEIR_ROCK: {LOSE: MY_SCISSORS, DRAW: MY_ROCK, WIN: MY_PAPER },
    THEIR_PAPER: { LOSE: MY_ROCK, DRAW: MY_PAPER, WIN: MY_SCISSORS },
    THEIR_SCISSORS: { LOSE: MY_PAPER, DRAW: MY_SCISSORS, WIN: MY_ROCK }
}

move_choice_scores = { MY_ROCK: 1, MY_PAPER: 2, MY_SCISSORS: 3 }

match_outcomes = {
    THEIR_ROCK: { MY_ROCK: DRAW_SCORE, MY_PAPER: WIN_SCORE, MY_SCISSORS: LOSE_SCORE },
    THEIR_PAPER: { MY_ROCK: LOSE_SCORE, MY_PAPER: DRAW_SCORE, MY_SCISSORS: WIN_SCORE },
    THEIR_SCISSORS: { MY_ROCK: WIN_SCORE, MY_PAPER: LOSE_SCORE, MY_SCISSORS: DRAW_SCORE } 
}

with open(FILE_NAME, 'r') as f:
    score = 0
    for line in f:
        (their_move, my_desired_outcome) = line.strip().split()

        my_move = move_choice_selection[their_move][my_desired_outcome]

        outcome = match_outcomes[their_move][my_move] + move_choice_scores[my_move]

        score += outcome

        print(their_move, my_move, outcome, score)
    
    print (score)