

class Player:
    x = 10
    y = 10
    speed = 1

    def move_player_right(self):
        self.x = self.x + self.speed

    def move_player_left(self):
        self.x = self.x - self.speed

    def move_player_up(self):
        self.y = self.y + self.speed
    def move_player_down(self):
        self.y = self.y - self.speed

