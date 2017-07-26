from numpy import random as rd
import matplotlib.pyplot as plt
import numpy as np

class Player:
    def __init__(self, player_ID, init_money=100):
        self.money = int(init_money)
        self.player_ID = player_ID


    def __str__(self):
        return "%d" % self.money

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


class GameBoard:
    def __init__(self, player_num=100, init_money=100):
        self.player_num = player_num
        self.players = [Player(id, init_money) for id in range(player_num)]



    def show_players(self):
        for i in range(self.player_num):
            print("ID:", i, "money", self.players[i])

    def show_statistics(self):
        print("############")
        print("total money:", sum([p.money for p in self.players]))

    def transfer(self, id_from, id_to, amount=1):
        assert id_from in range(self.player_num)
        assert id_to in range(self.player_num)
        assert id_to != id_from
        wd = self.players[id_from].withdraw(amount)
        if wd >= 0:
            self.players[id_to].deposit(wd)

    def run_once(self):
        for pl in self.players:
            id_to = pl.make_move(self.player_num)
            self.transfer(pl.player_ID, id_to, 1)

    def plot_hist(self, data):
        n, bins, patches = plt.hist(data, 50, normed=1, facecolor='green', alpha=0.75)
        plt.xlabel('money')
        plt.ylabel('Probability')
        #plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=100,\ \sigma=15$')
        #plt.axis([0, 300, 0, 0.03])
        plt.grid(True)
        plt.show()

    def run_and_plot(self, times=500, plt_step=20):
        for i in range(times):
            self.run_once()
            if i % plt_step == 0:
                data = [pl.money for pl in self.players]
                self.plot_hist(data)

gb =GameBoard(player_num=500)

#for i in range(1000):
#    gb.run_once()
#gb.show_players()
#gb.show_statistics()
gb.run_and_plot(100000, 500)

