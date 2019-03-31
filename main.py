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
        self.player_two = RandomPlayer('ai', -1)

        self.board =  self.get_empty_board()

    def get_empty_board(self):
        return np.array([[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])

    def print_bord(self):
        os.system('cls')
        print(str(self.board[0,0]) + ' | ' + str(self.board[0,1]) + ' | ' + str(self.board[0,2]))
        print('----------')
        print(str(self.board[1,0]) + ' | ' + str(self.board[1,1]) + ' | ' + str(self.board[1,2]))
        print('----------')
        print(str(self.board[2,0]) + ' | ' + str(self.board[2,1]) + ' | ' + str(self.board[2,2]))
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
