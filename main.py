import numpy as np
import random
import os


class Player:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def move(self, board):
        raise Exception


class RandomPlayer(Player):
    def __init__(self, name, value):
        Player.__init__(self, name, value)
        
    def move(self, board):
        while True:
            x = random.randint(0,2)
            y = random.randint(0,2)
            if board[x,y] == 0:
                return (x,y)


class DefencePlayerWOD(Player):
    '''
    prevents opened from wining, does not check diagonals
    '''
    def __init__(self, name, value):
        Player.__init__(self, name, value)
        if self.value == -1:
            self.opened_value = 1
        else:
            self.opened_value = -1


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


        while True:
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if board[x, y] == 0:
                return (x, y)


class HumanPlayer(Player):
    def __init__(self, name, value):
        Player.__init__(self, name, value)
        
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
    def __init__ (self):
        self.player_one = HumanPlayer('human', 1)
        #self.player_two = RandomPlayer('ai', -1)
        self.player_two = DefencePlayerWOD('ai', -1)


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
        self.print_bord()
        turns = 0
        while True:
            pos = self.player_one.move(self.board)
            self.set_move(pos, 1)
            turns += 1
            self.print_bord()


            game_status = self.check_game()
            if game_status == 1:
                print('player one won!')
                break

            if game_status == -1:
                print('player two won!')
                break

            if turns == 9:
                print('draw')
                break

            pos = self.player_two.move(self.board)
            self.set_move(pos, -1)
            turns += 1
            self.print_bord()



            game_status = self.check_game()
            if game_status == 1:
                print('player one won!')
                break

            if game_status == -1:
                print('player two won!')
                break
            
            if turns == 9:
                print('draw')
                break


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


game = Game()
game.start()
