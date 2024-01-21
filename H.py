import pyxel
import random

class Train:
    def __init__(self):
        self.x = -200
        self.y = 50
        self.passengers = []

    def move(self):
        self.x += 15

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 0, 200, 96)
        for passenger in self.passengers:
            passenger.draw()

class Passenger:
    def __init__(self, x=None):
        self.x = random.randint(-168, -32)
        self.y = 82

    def move(self):
        self.x += 15

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 0, 96, 16, 32)

class App:
    def __init__(self):
        pyxel.init(200, 200)
        pyxel.load("assets/my_resource.pyxres")
        pyxel.sound(0).set("a3e2c2", "p", "7", "s", 3)

        self.trains = [Train()]
        self.player_count = 0
        self.remaining_time = 600
        self.is_game_over = False

        pyxel.run(self.update, self.draw)

    def update(self):
        if not self.is_game_over:
            for train in self.trains:
                train.move()
                for passenger in train.passengers:
                    passenger.move()

            if pyxel.btnp(pyxel.KEY_SPACE):
                self.player_count += 1
                pyxel.play(0, 0)  

            if self.remaining_time > 0:
                self.remaining_time -= 1
            else:
                self.is_game_over = True

            if self.trains[-1].x > 0:
                new_train = Train()
                new_train.x = -200

                for _ in range(random.randint(0, 3)):
                    new_train.passengers.append(Passenger(new_train.x))

                self.trains.append(new_train)

        if self.is_game_over and pyxel.btnp(pyxel.KEY_R):  
            self.restart_game()

    def draw(self):
        pyxel.cls(7)
        pyxel.blt(0, 0, 1, 0, 0, 200, 200)

        for train in self.trains:
            train.draw()
            pyxel.text(5, 5, f"Player Count: {self.player_count}", 7)
            pyxel.text(5, 15, f"Time: {self.remaining_time}", 7)

        if self.is_game_over:
            if self.player_count == sum(len(train.passengers) for train in self.trains):
                pyxel.text(55, 60, "Correct!", 10)
            else:
                pyxel.text(55, 60, "Incorrect!", 8)
            pyxel.text(50, 85, "Correct Count: " + str(sum(len(train.passengers) for train in self.trains)), 7)
            pyxel.text(50, 95, "Your Count: " + str(self.player_count), 7)
            pyxel.text(50, 105, "Press R to play again", 7)

    def restart_game(self):
        self.player_count = 0
        self.remaining_time = 600
        self.is_game_over = False
        self.trains = [Train()]

App()
