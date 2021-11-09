import json


class Menus:
    def __init__(self):
        with open('./assets/menus.json', 'r') as menus:
            self.__menu_list = json.load(menus)

    def printMenu(self, stage):
        for item in self.__menu_list[stage]:
            print(item)
