# moves = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
#          'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors'}

moves = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
         'X': 'lose', 'Y': 'draw', 'Z': 'win'}

def get_win(move):
    if move == 'Rock':
        return 'Paper'
    elif move == 'Paper':
        return 'Scissors'
    else:
        return 'Rock'

def get_lose(move):
    if move == 'Rock':
        return 'Scissors'
    elif move == 'Paper':
        return 'Rock'
    else:
        return 'Paper'

def get_result(result, player_one):
    if result == 'win':
        return get_win(player_one)
    elif result == 'draw':
        return player_one
    else:
        return get_lose(player_one)


def get_score(player_one, player_two):
    player_two = get_result(player_two, player_one)
    if (player_one == player_two):
        return 3
    else:
        winner = play_game(player_one, player_two)
        if winner == 'player_two':
            return 6
        else:
            return 0

def get_move_points(player_one, player_two):
    move = get_result(player_two, player_one)
    if (move == 'Rock'):
        return 1
    elif (move == 'Paper'):
        return 2
    else:
        return 3

def play_game(player_one, player_two):
    if (player_one == 'Rock'):
        if (player_two == 'Paper'):
            return 'player_two'
        else:
            return 'player_one'
    elif (player_one == 'Paper'):
        if (player_two == 'Rock'):
            return 'player_one'
        else:
            return  'player_two'
    else:
        if (player_two == 'Rock'):
            return 'player_two'
        else:
            return 'player_one'

def process_line(line):
    round_outcome = get_score(moves[line[0]], moves[line[2]])
    move_score = get_move_points(moves[line[0]], moves[line[2]])
    return round_outcome + move_score

def main():
    score = 0
    with open('day_2_input.txt') as file:
        for line in file:
            score += process_line(line)
    print(f'Final score: {score}')


# get_score('Rock', 'Rock')
# get_score('Rock', 'Paper')
# get_score('Paper', 'Scissors')
# get_score('Rock', 'Scissors')

# with open('demo.txt') as file:
#     for line in file:
        #print(f'player one: {moves[line[0]]} | player two: {moves[line[2]]}')

main()

############################
# PART 1
# 05/12/2022
# ANSWER: 13924
# TOTAL TIME: 46m 21s
#
# PART 2
# 11/12/2022
# ANSWER: 13448
# TOTAL TIME: ~10m