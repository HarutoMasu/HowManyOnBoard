import pyxel

class TrainGame:
    def __init__(self):
        pyxel.init(200, 200)
        self.state = "title"  # ゲームの状態を管理

        # ゲームの初期化
        self.reset_game()

        pyxel.run(self.update, self.draw)

    def reset_game(self):
        self.passenger_count = 0
        self.train_speed = 0
        self.timer = 0
        self.answer = 0
        self.state = "title"

    def update(self):
        if self.state == "title":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = "countdown"
                self.timer = 180  # カウントダウンの初期値（3秒）

        elif self.state == "countdown":
            self.timer -= 1
            if self.timer == 0:
                self.state = "game"
                self.timer = 660  # ゲームの制限時間（11秒）
                self.train_speed = 3  # 固定の電車の速さ
                self.answer = self.generate_answer()  # 乗っている人数の正解

        elif self.state == "game":
            self.timer -= 1
            if self.timer == 0:
                self.state = "finish"

            # 電車の描画と効果音（未完成）
            self.draw_train()
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.passenger_count += 1
                pyxel.play(0, 1)  # カウントしたときの音

        elif self.state == "finish":
            if pyxel.btnp(pyxel.KEY_SPACE):
                self.state = "result"

        elif self.state == "result":
            if pyxel.btnp(pyxel.KEY_SPACE):
                if self.passenger_count == self.answer:
                    self.state = "correct"
                else:
                    self.state = "incorrect"
                self.reset_game()

    def draw(self):
        pyxel.cls(6)

        if self.state == "title":
            pyxel.text(60, 90, "How Many On Board?", 7)
            pyxel.text(60, 120, "Press SPACE to start", 7)

        elif self.state == "countdown":
            pyxel.text(95, 80, str(self.timer // 60 + 1), 7)

        elif self.state == "game":
            pyxel.text(10, 10, f"Passengers: {self.passenger_count}", 7)
            pyxel.text(10, 20, f"Time: {self.timer // 60}", 7)

        elif self.state == "finish":
            pyxel.text(80, 80, "Finish!", 7)
            pyxel.text(70, 120, "Press SPACE to see the result", 7)

        elif self.state == "result":
            pyxel.text(80, 80, f"Correct Answer: {self.answer}", 7)
            pyxel.text(70, 120, "Press SPACE to continue", 7)

        elif self.state == "correct":
            pyxel.text(80, 80, "Correct!", 7)
            pyxel.text(70, 120, "Press SPACE to play again", 7)

        elif self.state == "incorrect":
            pyxel.text(80, 80, "Incorrect!", 7)
            pyxel.text(70, 120, "Press SPACE to play again", 7)

    def draw_train(self):
        # 電車の描画（未完成）
        pass

    def generate_answer(self):
        # 1から20までのランダムな整数を生成
        return pyxel.frame_count % 20 + 1

TrainGame()