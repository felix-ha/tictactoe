import numpy as np
import random
import os

from players import RandomPlayer, DefencePlayer, \
                    OffensivePlayer, OffensiveDefensivePlayer, \
                    ProbabilityPlayer, TemporalDifferenceTrainingPlayer, \
                    TemporalDifferencePlayer, HumanPlayer


class Game:
    def __init__ (self, player_one, player_two, ui='CLI'):
        self.player_one = player_one
        self.player_two = player_two
        self.ui = ui


        self.board =  self.get_empty_board()

    def get_empty_board(self):
        return np.array([[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])

    def get_empty_string_board(self):
        return np.array([[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]], dtype=str)

    def convert_bord_xo(self, A):
        result = self.get_empty_string_board()

        for i in range(3):
            for j in range(3):
                if A[i,j] == -1:
                    result[i,j] = 'O'
                elif A[i,j] == 1:
                    result[i,j] = 'X'
                else:
                    result[i,j] = ' '

        return result

    def print_bord(self):
        os.system('cls')
        board = self.convert_bord_xo(self.board)
        print(str(board[0,0]) + ' | ' + str(board[0,1]) + ' | ' + str(board[0,2]))
        print('----------')
        print(str(board[1,0]) + ' | ' + str(board[1,1]) + ' | ' + str(board[1,2]))
        print('----------')
        print(str(board[2,0]) + ' | ' + str(board[2,1]) + ' | ' + str(board[2,2]))
        print()

    def set_move(self, move, player):
        if self.board[move[0], move[1]] == 0:
            self.board[move[0], move[1]] = player
        else:
            raise Exception


    def start(self):
        self.player_one.set_value(1)
        self.player_two.set_value(-1)

        if self.ui == 'CLI':
            self.print_bord()
        turns = 0
        while True:
            board_prev = self.board.copy()
            pos = self.player_one.move(self.board)
            self.set_move(pos, self.player_one.value)
            turns += 1
            if self.ui == 'CLI':
                self.print_bord()


            game_status = self.check_game()
            if game_status == 1:
                if self.ui == 'CLI':
                    print('player one won!')
                self.player_one.update_final_board(self.board, board_prev, 1)
                self.player_two.update_final_board(self.board, board_prev, 0)
                return 1

            if game_status == -1:
                if self.ui == 'CLI':
                    print('player two won!')
                self.player_one.update_final_board(self.board, board_prev, 0)
                self.player_two.update_final_board(self.board, board_prev, 1)
                return -1

            if turns == 9:
                if self.ui == 'CLI':
                    print('draw')
                self.player_one.update_final_board(self.board, board_prev, 0)
                self.player_two.update_final_board(self.board, board_prev, 0)
                return 0

            board_prev = self.board.copy()
            pos = self.player_two.move(self.board)
            self.set_move(pos, self.player_two.value)
            turns += 1
            if self.ui == 'CLI':
                self.print_bord()

            game_status = self.check_game()
            if game_status == 1:
                if self.ui == 'CLI':
                    print('player one won!')
                self.player_one.update_final_board(self.board, board_prev, 1)
                self.player_two.update_final_board(self.board, board_prev, 0)
                return 1

            if game_status == -1:
                if self.ui == 'CLI':
                    print('player two won!')
                self.player_one.update_final_board(self.board, board_prev, 0)
                self.player_two.update_final_board(self.board, board_prev, 1)
                return -1

            if turns == 9:
                if self.ui == 'CLI':
                    print('draw')
                self.player_one.update_final_board(self.board, board_prev, 0)
                self.player_two.update_final_board(self.board, board_prev, 0)
                return 0


    def check_player_won(self, player):
        for i in range(3):
            if np.sum(self.board[:,i]) == player:
                return True

            if np.sum(self.board[i,:]) == player:
                return True

        if self.board[0,0] + self.board[1,1] + self.board[2,2] == player:
            return True

        if self.board[2,0] + self.board[1,1] + self.board[0,2] == player:
            return True

        return False


    def check_game(self):
        if self.check_player_won(3):
            return 1
        if self.check_player_won(-3):
            return -1
        return 0


def game_against_ai():
    player_one = HumanPlayer('human')
    # self.player_two = RandomPlayer('ai')
    # player_two = DefencePlayer('ai')
    # player_two = OffensivePlayer('ai')
    player_two = ProbabilityPlayer('ai_prob')
    game = Game(player_one, player_two)
    winner = game.start()
    print(winner)


def test_all_players():
    players = [RandomPlayer('ai'), OffensivePlayer('ai'),
               DefencePlayer('ai'), OffensiveDefensivePlayer('ai'),
               ProbabilityPlayer('ai'), TemporalDifferenceTrainingPlayer('ai')]

    for i in range(len(players)):
        for j in range(len(players)):
            game = Game(players[i], players[j], ui=None)
            game.start()

    print('test was successful')


import matplotlib.pyplot as plt
def simulate_games():
    player_one = TemporalDifferenceTrainingPlayer('td_random')
    # player_one = DefencePlayer('ai')
    # player_one = OffensiveDefensivePlayer('ai')
    # player_one = RandomPlayer('ai_random')
    # player_two = RandomPlayer('ai_random')
    player_two = RandomPlayer('ai')
    # player_one = TemporalDifferencePlayer('td')
    one = two = draw = 0
    number_of_trials = 1e3
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




    print()
    print('Player one won       : {}'.format(one))
    print('Player two won       : {}'.format(two))
    print('Draw                 : {}'.format(draw))
    print('Win ratio Player one : {}'.format(one / number_of_trials))

    x = np.arange(3)
    data = [one, draw, two]
    plt.bar(x, data)
    plt.xticks(x, ('One', 'Draw', 'Two'))
    plt.show()

if __name__ == '__main__':
    # game_against_ai()
    # simulate_games()


    test_all_players()

