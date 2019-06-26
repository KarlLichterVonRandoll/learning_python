from bll import *
import os


class GameManagerView:
    def __init__(self, map_list):
        self.__manager = GameCoreController(map_list)
        self.map_list = map_list

    def __print_map(self):
        os.system("clear")
        for item in self.map_list:
            for i in item:
                print(i, end=" ")
            print()

    def __select_menu(self):
        order = input("输入w(上)s(下)a(左)d(右):")
        self.__manager.move(order)

    def main(self):
        while True:
            if self.__manager.is_game_over():
                self.__print_map()
                print("游戏失败，游戏结束")
                break
            if self.__exist_2048():
                self.__print_map()
                print("恭喜通关")
                break
            self.__print_map()
            self.__select_menu()
            self.__manager.generate_random()

    def __zero_exist(self):
        leap = False
        for row in self.map_list:
            if 0 in row:
                leap = True
        return leap

    def __exist_2048(self):
        leap = False
        for row in self.map_list:
            if 2048 in row:
                leap = True
        return leap
