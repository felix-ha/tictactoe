import numpy as np
import random
import os

from players import RandomPlayer, DefencePlayer, \
                    OffensivePlayer, OffensiveDefensivePlayer, \
                    ProbabilityPlayer, TemporalDifferenceTrainingPlayer, \
                    TemporalDifferencePlayer, HumanPlayer
from main import Game


def train_td_player(player, number_of_trials):
    player_one = TemporalDifferenceTrainingPlayer('td_random')
    player_two = player
    one = two = draw = 0
    for i in range(int(number_of_trials)):
        if random.random() < 0.5:
            game = Game(player_one, player_two, ui=None)
            winner = game.start()
            if winner == 1:
                one += 1
            if winner == -1:
                two += 1
            if winner == 0:
                draw += 1
            # print('winner : {} game {}'.format(winner,i))
            print('{}'.format(i/number_of_trials))

        else:
            game = Game(player_two, player_one, ui=None)
            winner = game.start()
            if winner == 1:
                two += 1
            if winner == -1:
                one += 1
            if winner == 0:
                draw += 1
            # print('winner : {} game {}'.format(winner,i))




    print('\nTraining:')
    print('Player one won       : {}'.format(one))
    print('Player two won       : {}'.format(two))
    print('Draw                 : {}'.format(draw))
    print('Win ratio Player one : {}'.format(one / number_of_trials))

    player_one.plot_alpha()

    # x = np.arange(3)
    # data = [one, draw, two]
    # plt.bar(x, data)
    # plt.xticks(x, ('One', 'Draw', 'Two'))
    # plt.show()

def test_td_player(player, number_of_trials):
    player_one = TemporalDifferencePlayer('td_random')
    player_two = player
    one = two = draw = 0
    for i in range(int(number_of_trials)):
        if random.random() < 0.5:
            game = Game(player_one, player_two, ui=None)
            winner = game.start()
            if winner == 1:
                one += 1
            if winner == -1:
                two += 1
            if winner == 0:
                draw += 1
            # print('winner : {} game {}'.format(winner,i))
            # print('{}'.format(i/number_of_trials))

        else:
            game = Game(player_two, player_one, ui=None)
            winner = game.start()
            if winner == 1:
                two += 1
            if winner == -1:
                one += 1
            if winner == 0:
                draw += 1
            # print('winner : {} game {}'.format(winner,i))

    print('\nTesting:')
    print('Player one won       : {}'.format(one))
    print('Player two won       : {}'.format(two))
    print('Draw                 : {}'.format(draw))
    print('Win ratio Player one : {}'.format(one / number_of_trials))


if __name__ == '__main__':
    number_of_trials = 1e5
    player = RandomPlayer('ai')
    train_td_player(player, number_of_trials)
    test_td_player(player, 1e3)

