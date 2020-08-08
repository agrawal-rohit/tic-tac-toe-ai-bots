# A Tic Tac Toe Bot 

![tictactoe](https://user-images.githubusercontent.com/29514438/89706167-c3120200-d980-11ea-8fdc-b3593c004ea4.png)

This is the code repository for my article on Medium - [Playing Games with Python - Tic Tac Toe](https://towardsdatascience.com/lets-beat-games-using-a-bunch-of-code-part-1-tic-tac-toe-1543e981fec1), where I have tried to take the famous Tic-Tac-Toe game and create a bot proficient enough to beat human players, if not the game itself.

## What's inside this repo?
- A fully playable Tic-Tac-Toe environment.
- A bot trained using Temporal Difference learning (A technique in Reinforcement learning). 
- A bot trained using the Minimax Algorithm.

## How to use

### Play against the RL bot
run ``` python testing_(HumanvsAI)_ReinforcementLearning.py```

### Play against the Minimax bot
run ``` python HumanvsAI_Minimax.py```

### Play against another human player (Regular tic tac toe)
run ``` python HumanvsHuman.py```

## Training the RL Bot
Out of the two implementations, only the RL bot needs to train in order to reach proficiency. It does so by play 1v1 with another RL bot sharing the same state values in order to learn to beat itself and eventually become better. The `num_iterations` parameter controls the number of games that will be played among the bots.

run ```python training_(AIvsAI)_ReinforcementLearning.py```

## Testing the two bots by making them play among themselves
I wrote anotherr script in order to see which bot performed better in very brutal 1v1 fashion. The `num_iterations` parameter controls the number of games that will be played among both the bots.

run ```python Showdown_Minimax_vs_RL.py```

## To Try
- [x] Minimax Algorithm
- [x] Temporal Difference Learning
- [ ] Q Learning
- [ ] Genetic Algorithms
