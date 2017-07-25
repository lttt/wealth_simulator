from numpy import random as rd
import matplotlib.pyplot as plt


class GameBoard:
    def __init__(self, player_num=100, init_money=100):
        self.player_num = player_num
        for i in range(player_num):
            print(i)



class Player:
    def __init__(self, player_ID, init_money=100):
        self.money = int(init_money)
        self.player_ID = player_ID


    def make_move(self, player_num):
        """
        make a choice
        :param player_num:  the number of all players
        :return:
        """
        while True:
            new_ID = rd.randint(0, player_num)
            if new_ID != self.player_ID:
                break

        return new_ID

    def withdraw(self, amount=1):
        if self.money >= amount:
            self.money -= amount
            return amount
        else:
            return 0

    def deposit(self, amount=1):
        self.money += amount

gb =GameBoard()