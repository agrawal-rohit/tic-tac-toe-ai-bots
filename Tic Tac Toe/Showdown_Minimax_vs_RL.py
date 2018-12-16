import numpy as np
from math import inf as infinity
import itertools
import random

game_state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
players = ['X','O']

def play_move(state, player, block_num):
    if state[int((block_num-1)/3)][(block_num-1)%3] is ' ':
        state[int((block_num-1)/3)][(block_num-1)%3] = player
    else:
        block_num = int(input("Block is not empty, ya blockhead! Choose again: "))
        play_move(state, player, block_num)
    
def copy_game_state(state):
    new_state = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
    for i in range(3):
        for j in range(3):
            new_state[i][j] = state[i][j]
    return new_state
    
def check_current_state(game_state):    
    # Check horizontals
    if (game_state[0][0] == game_state[0][1] and game_state[0][1] == game_state[0][2] and game_state[0][0] is not ' '):
        return game_state[0][0], "Done"
    if (game_state[1][0] == game_state[1][1] and game_state[1][1] == game_state[1][2] and game_state[1][0] is not ' '):
        return game_state[1][0], "Done"
    if (game_state[2][0] == game_state[2][1] and game_state[2][1] == game_state[2][2] and game_state[2][0] is not ' '):
        return game_state[2][0], "Done"
    
    # Check verticals
    if (game_state[0][0] == game_state[1][0] and game_state[1][0] == game_state[2][0] and game_state[0][0] is not ' '):
        return game_state[0][0], "Done"
    if (game_state[0][1] == game_state[1][1] and game_state[1][1] == game_state[2][1] and game_state[0][1] is not ' '):
        return game_state[0][1], "Done"
    if (game_state[0][2] == game_state[1][2] and game_state[1][2] == game_state[2][2] and game_state[0][2] is not ' '):
        return game_state[0][2], "Done"
    
    # Check diagonals
    if (game_state[0][0] == game_state[1][1] and game_state[1][1] == game_state[2][2] and game_state[0][0] is not ' '):
        return game_state[1][1], "Done"
    if (game_state[2][0] == game_state[1][1] and game_state[1][1] == game_state[0][2] and game_state[2][0] is not ' '):
        return game_state[1][1], "Done"
    
    # Check if draw
    draw_flag = 0
    for i in range(3):
        for j in range(3):
            if game_state[i][j] is ' ':
                draw_flag = 1
    if draw_flag is 0:
        return None, "Draw"
    
    return None, "Not Done"

def print_board(game_state):
    print('----------------')
    print('| ' + str(game_state[0][0]) + ' || ' + str(game_state[0][1]) + ' || ' + str(game_state[0][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[1][0]) + ' || ' + str(game_state[1][1]) + ' || ' + str(game_state[1][2]) + ' |')
    print('----------------')
    print('| ' + str(game_state[2][0]) + ' || ' + str(game_state[2][1]) + ' || ' + str(game_state[2][2]) + ' |')
    print('----------------')
    
  
# Initialize state values
player = ['X','O',' ']
states_dict = {}
all_possible_states = [[list(i[0:3]),list(i[3:6]),list(i[6:10])] for i in itertools.product(player, repeat = 9)]
n_states = len(all_possible_states) # 2 players, 9 spaces
n_actions = 9   # 9 spaces
state_values_for_AI = np.full((n_states),0.0)
print("n_states = %i \nn_actions = %i"%(n_states, n_actions))

for i in range(n_states):
    states_dict[i] = all_possible_states[i]
    winner, _ = check_current_state(states_dict[i])
    if winner == 'O':   # AI won
        state_values_for_AI[i] = 1
    elif winner == 'X':   # AI lost
        state_values_for_AI[i] = -1

def update_state_value(curr_state_idx, next_state_idx, learning_rate):
    new_value = state_values_for_AI[curr_state_idx] + learning_rate*(state_values_for_AI[next_state_idx]  - state_values_for_AI[curr_state_idx])
    state_values_for_AI[curr_state_idx] = new_value

def getBestMove_RL(state, player):
    '''
    Reinforcement Learning Algorithm
    '''    
    moves = []
    curr_state_values = []
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if state[i][j] is ' ':
                empty_cells.append(i*3 + (j+1))
    
    for empty_cell in empty_cells:
        moves.append(empty_cell)
        new_state = copy_game_state(state)
        play_move(new_state, player, empty_cell)
        next_state_idx = list(states_dict.keys())[list(states_dict.values()).index(new_state)]
        curr_state_values.append(state_values_for_AI[next_state_idx])
        
    print('Possible moves = ' + str(moves))
    print('Move values = ' + str(curr_state_values))    
    best_move_idx = np.argmax(curr_state_values)
    best_move = moves[best_move_idx]
    return best_move

def getBestMove_Minimax(state, player):
    '''
    Minimax Algorithm
    '''
    winner_loser , done = check_current_state(state)
    if done == "Done" and winner_loser == 'O': # If AI won
        return 1
    elif done == "Done" and winner_loser == 'X': # If Human won
        return -1
    elif done == "Draw":    # Draw condition
        return 0
        
    moves = []
    empty_cells = []
    for i in range(3):
        for j in range(3):
            if state[i][j] is ' ':
                empty_cells.append(i*3 + (j+1))
    
    for empty_cell in empty_cells:
        move = {}
        move['index'] = empty_cell
        new_state = copy_game_state(state)
        play_move(new_state, player, empty_cell)
        
        if player == 'O':    # If AI
            result = getBestMove_Minimax(new_state, 'X')    # make more depth tree for human
            move['score'] = result
        else:
            result = getBestMove_Minimax(new_state, 'O')    # make more depth tree for AI
            move['score'] = result
        
        moves.append(move)

    # Find best move
    best_move = None
    if player == 'O':   # If AI player
        best = -infinity
        for move in moves:
            if move['score'] > best:
                best = move['score']
                best_move = move['index']
    else:
        best = infinity
        for move in moves:
            if move['score'] < best:
                best = move['score']
                best_move = move['index']
                
    return best_move
# PLaying
    
#LOAD TRAINED STATE VALUES
state_values_for_AI = np.loadtxt('trained_state_values_X.txt', dtype=np.float64)
minimax_wins = 0
rl_wins = 0
num_iterations = 10
for iteration in range(num_iterations):
    game_state = [[' ',' ',' '],
              [' ',' ',' '],
              [' ',' ',' ']]
    current_state = "Not Done"
    print("\nNew Game! (X = RL Agent, O = Minimax Agent)")
    print_board(game_state)
    current_player_idx = random.choice([0,1])
        
    while current_state == "Not Done":
        curr_state_idx = list(states_dict.keys())[list(states_dict.values()).index(game_state)]
        if current_player_idx == 0: # RL Agent's turn
            block_choice = getBestMove_RL(game_state, players[current_player_idx])
            play_move(game_state ,players[current_player_idx], block_choice)
            print("RL Agent plays move: " + str(block_choice))
            
        else:   # Minimax Agent's turn
            block_choice = getBestMove_Minimax(game_state, players[current_player_idx])
            play_move(game_state ,players[current_player_idx], block_choice)
            print("Minimax Agent plays move: " + str(block_choice))
        
        print_board(game_state)
        winner, current_state = check_current_state(game_state)
        if winner is not None:
            if winner == 'X':
                print("RL Agent Won!")
                rl_wins += 1
            else:
                print("Minimax Agent Won!")
                minimax_wins += 1
        else:
            current_player_idx = (current_player_idx + 1)%2
        
        if current_state is "Draw":
            print("Draw!")
            
print('\nResults(' + str(num_iterations) + ' games):')
print('Minimax Wins = ' + str(minimax_wins))        
print('RL Agent Wins = ' + str(rl_wins) + '\n')        
    
