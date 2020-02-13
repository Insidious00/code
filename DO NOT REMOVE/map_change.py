import time

class MapChange:
    def __init__(self, game, Map):
        self.game = game

    def change(self, newMap):
        if newMap == "inner_house1":
            self.inner_house1()
            time.sleep(0.2)
            self.game.newplayer = True
            self.game.new()
            time.sleep(0.2)
        if newMap == "inner_house2":
            self.inner_house2()
            time.sleep(0.2)
            self.game.newplayer = True
            self.game.new()
            time.sleep(0.2)
        if newMap == "outside_town1":
            self.outside_town1()
            time.sleep(0.2)
            self.game.newplayer = True
            self.game.new()
            self.game.player.pos = (self.game.backtrack.x + 0.5*(self.game.backtrack.w), self.game.backtrack.y+75)
            time.sleep(0.2)
            
    def inner_house1(self):
        self.game.map = self.game.map2
        self.game.map_img = self.game.map_img2
        self.game.map_rect = self.game.map2_rect
        self.game.new()

    def outside_town1(self):
        self.game.map = self.game.map1
        self.game.map_img = self.game.map_img1
        self.game.map_rect = self.game.map1_rect
        self.game.new()

    def inner_house2(self):
        self.game.map = self.game.map3
        self.game.map_img = self.game.map_img3
        self.game.map_rect = self.game.map3_rect
        self.game.new()

