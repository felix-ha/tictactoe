import numpy as np
import random
import os


class Player:
    def __init__(self, name):
        self.name = name
        self.value = None

    def move(self, board):
        raise Exception

    def set_value(self, value):
        self.value = value


class RandomPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        
    def move(self, board):
        while True:
            x = random.randint(0,2)
            y = random.randint(0,2)
            if board[x,y] == 0:
                return (x,y)


class DefencePlayer(Player):
    '''
    prevents opened from wining
    '''
    def __init__(self, name):
        Player.__init__(self, name)


    def get_empty_cell_row(self, row, board):
        for j in range(3):
            if board[row, j] == 0:
                return j

    def get_empty_cell_column(self, column, board):
        for i in range(3):
            if board[i, column] == 0:
                return i


    def move(self, board):
        if self.value == -1:
            self.opened_value = 1
        else:
            self.opened_value = -1

        # check rows
        for i in range(3):
            if np.sum(board[i,:]) == self.opened_value * 2:
                empty_cell_row = self.get_empty_cell_row(i, board)
                if board[i, empty_cell_row] == 0:
                    return i, empty_cell_row

        # check columns
        for j in range(3):
            if np.sum(board[:,j]) == self.opened_value * 2:
                empty_cell_column = self.get_empty_cell_column(j, board)
                if board[empty_cell_column, j] == 0:
                    return empty_cell_column, j

        # check diagonals
        if board[0,0] + board[1,1] + board[2,2] == self.opened_value * 2:
            for i in range(3):
                if board[i,i] == 0:
                    return i, i

        if board[2,0] + board[1,1] + board[0,2] == self.opened_value * 2:
            if board[2, 0] == 0:
                return 2, 0
            if board[1, 1] == 0:
                return 1, 1
            if board[0, 2] == 0:
                return 0, 2

        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if board[x, y] == 0:
                return (x, y)


class OffensivePlayer(Player):
    '''
    tries to win if it is possible on the next move
    '''
    def __init__(self, name):
        Player.__init__(self, name)

    def get_empty_cell_row(self, row, board):
        for j in range(3):
            if board[row, j] == 0:
                return j

    def get_empty_cell_column(self, column, board):
        for i in range(3):
            if board[i, column] == 0:
                return i

    def move(self, board):

        # check rows
        for i in range(3):
            if np.sum(board[i,:]) == self.value * 2:
                empty_cell_row = self.get_empty_cell_row(i, board)
                if board[i, empty_cell_row] == 0:
                    return i, empty_cell_row

        # check columns
        for j in range(3):
            if np.sum(board[:,j]) == self.value * 2:
                empty_cell_column = self.get_empty_cell_column(j, board)
                if board[empty_cell_column, j] == 0:
                    return empty_cell_column, j

        # check diagonals
        if board[0,0] + board[1,1] + board[2,2] == self.value * 2:
            for i in range(3):
                if board[i,i] == 0:
                    return i, i

        if board[2,0] + board[1,1] + board[0,2] == self.value * 2:
            if board[2, 0] == 0:
                return 2, 0
            if board[1, 1] == 0:
                return 1, 1
            if board[0, 2] == 0:
                return 0, 2

        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if board[x, y] == 0:
                return (x, y)


class OffensiveDefensivePlayer(Player):
    '''
    tries to win if it is possible on the next move
    '''
    def __init__(self, name):
        Player.__init__(self, name)


    def get_empty_cell_row(self, row, board):
        for j in range(3):
            if board[row, j] == 0:
                return j

    def get_empty_cell_column(self, column, board):
        for i in range(3):
            if board[i, column] == 0:
                return i

    def move(self, board):
        if self.value == -1:
            self.opened_value = 1
        else:
            self.opened_value = -1

        # check rows
        for i in range(3):
            if np.sum(board[i,:]) == self.value * 2:
                empty_cell_row = self.get_empty_cell_row(i, board)
                if board[i, empty_cell_row] == 0:
                    return i, empty_cell_row

        # check columns
        for j in range(3):
            if np.sum(board[:,j]) == self.value * 2:
                empty_cell_column = self.get_empty_cell_column(j, board)
                if board[empty_cell_column, j] == 0:
                    return empty_cell_column, j

        # check diagonals
        if board[0,0] + board[1,1] + board[2,2] == self.value * 2:
            for i in range(3):
                if board[i,i] == 0:
                    return i, i

        if board[2,0] + board[1,1] + board[0,2] == self.value * 2:
            if board[2, 0] == 0:
                return 2, 0
            if board[1, 1] == 0:
                return 1, 1
            if board[0, 2] == 0:
                return 0, 2

        # check rows defensive
        for i in range(3):
            if np.sum(board[i, :]) == self.opened_value * 2:
                empty_cell_row = self.get_empty_cell_row(i, board)
                if board[i, empty_cell_row] == 0:
                    return i, empty_cell_row

        # check columns defensive
        for j in range(3):
            if np.sum(board[:, j]) == self.opened_value * 2:
                empty_cell_column = self.get_empty_cell_column(j, board)
                if board[empty_cell_column, j] == 0:
                    return empty_cell_column, j

        # check diagonals defensive
        if board[0, 0] + board[1, 1] + board[2, 2] == self.opened_value * 2:
            for i in range(3):
                if board[i, i] == 0:
                    return i, i

        if board[2, 0] + board[1, 1] + board[0, 2] == self.opened_value * 2:
            if board[2, 0] == 0:
                return 2, 0
            if board[1, 1] == 0:
                return 1, 1
            if board[0, 2] == 0:
                return 0, 2

        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if board[x, y] == 0:
                return (x, y)


class ProbabilityPlayer(Player):
    '''
    simulates moves and takes move with highest probability to win
    '''
    def __init__(self, name):
        Player.__init__(self, name)
        self.N = 10


    def check_player_won(self, player, board):
        for i in range(3):
            if np.sum(board[:,i]) == player:
                return True

            if np.sum(board[i,:]) == player:
                return True

        if board[0,0] + board[1,1] + board[2,2] == player:
            return True

        if board[2,0] + board[1,1] + board[0,2] == player:
            return True

        return False


    def check_game(self, board):
        if self.check_player_won(3, board):
            return 1
        if self.check_player_won(-3, board):
            return -1
        return 0


    def set_move(self, board, move, value):
        if board[move[0], move[1]] == 0:
            board[move[0], move[1]] = value
        else:
            raise Exception

    def simulate_game(self, board):
        player = RandomPlayer('rand1')
        player.set_value(self.value)
        opened = RandomPlayer('rand2')
        opened.set_value(self.value*-1)

        game_status = self.check_game(board)

        if game_status == self.value:
            return self.value
        if game_status == self.value * -1:
            return self.value * -1
        if len(np.argwhere(board == 0)) == 0:
            return 0

        while True:

            pos = opened.move(board)
            self.set_move(board, pos, self.value * -1)
            game_status = self.check_game(board)

            if game_status == self.value:
                return self.value
            if game_status == self.value * -1:
                return self.value * -1
            if len(np.argwhere(board == 0)) == 0:
                return 0


            pos = player.move(board)
            self.set_move(board, pos, self.value)
            game_status = self.check_game(board)

            if game_status == self.value:
                return self.value
            if game_status == self.value * -1:
                return self.value * -1
            if len(np.argwhere(board == 0)) == 0:
                return 0



    def get_probability(self, board):
        win = loss = draw = 0
        for i in range(self.N):
            result = self.simulate_game(board.copy())
            if result == self.value:
                win +=1
            if result == self.value * -1:
                loss +=1
            if result == 0:
                draw += 1

        # print('win  {}'.format(win/self.N))
        # print('loss {}'.format(loss/self.N))
        # print('draw {}'.format(draw/self.N))
        # print('sum  {}'.format(win/self.N+loss/self.N+draw/self.N))

        if win == self.N:
            return 1
        return win / self.N





    def get_probability_board(self, board):
        board_probability = np.array([[0., 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])
        player_one = RandomPlayer('rand1')
        player_two = RandomPlayer('rand2')
        player_one.set_value(1)
        player_two.set_value(-1)

        for i in range(3):
            for j in range(3):
                if board[i,j] != 0:
                    continue

                board_to_simulate = board.copy()
                board_to_simulate[i,j] = self.value
                probability = self.get_probability(board_to_simulate)
                board_probability[i,j] = probability

        return board_probability



    def move(self, board):
        probability_board = self.get_probability_board(board)

        if np.sum(probability_board) > 0.000000001:
            return np.argwhere(probability_board == np.max(probability_board))[0]

        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if board[x, y] == 0:
                return (x, y)






class HumanPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        
    def move(self, board):
        while True:
            move = input("move ")
            x = int(move[0])-1
            y = int(move[1])-1
            if board[x,y] == 0:
                return (x,y)
            else:
                print('not vaild, please retry')


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
            pos = self.player_one.move(self.board)
            self.set_move(pos, self.player_one.value)
            turns += 1
            if self.ui == 'CLI':
                self.print_bord()


            game_status = self.check_game()
            if game_status == 1:
                if self.ui == 'CLI':
                    print('player one won!')
                return 1

            if game_status == -1:
                if self.ui == 'CLI':
                    print('player two won!')
                return -1

            if turns == 9:
                if self.ui == 'CLI':
                    print('draw')
                return 0

            pos = self.player_two.move(self.board)
            self.set_move(pos, self.player_two.value)
            turns += 1
            if self.ui == 'CLI':
                self.print_bord()



            game_status = self.check_game()
            if game_status == 1:
                if self.ui == 'CLI':
                    print('player one won!')
                return 1

            if game_status == -1:
                if self.ui == 'CLI':
                    print('player two won!')
                return -1
            
            if turns == 9:
                if self.ui == 'CLI':
                    print('draw')
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
               ProbabilityPlayer('ai')]

    for i in range(len(players)):
        for j in range(len(players)):
            game = Game(players[i], players[j], ui=None)
            game.start()

    print('test was successful')


import matplotlib.pyplot as plt
def simulate_games():
    player_one = OffensivePlayer('ai')
    # player_one = DefencePlayer('ai')
    # player_one = OffensiveDefensivePlayer('ai')
    # player_one = RandomPlayer('ai_random')
    # player_two = RandomPlayer('ai_random')
    player_two = ProbabilityPlayer('ai_prob')
    one = two = draw = 0
    number_of_trials = 5e1
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
            print('winner : {} game {}'.format(winner,i))

        else:
            game = Game(player_two, player_one, ui=None)
            winner = game.start()
            if winner == 1:
                two += 1
            if winner == -1:
                one += 1
            if winner == 0:
                draw += 1
            print('winner : {} game {}'.format(winner,i))




    print()
    print('Player one won : {}'.format(one))
    print('Player two won : {}'.format(two))
    print('Draw           : {}'.format(draw))

    x = np.arange(3)
    data = [one, draw, two]
    plt.bar(x, data)
    plt.xticks(x, ('One', 'Draw', 'Two'))
    plt.show()

if __name__ == '__main__':
    # game_against_ai()
    # simulate_games()
    test_all_players()

