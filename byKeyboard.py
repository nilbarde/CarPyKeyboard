try:
    import kivy

    from kivy.app import App

    from kivy.uix.screenmanager import ScreenManager, Screen
    from kivy.uix.button import Button
    from kivy.clock import Clock

    from kivy.uix.gridlayout import GridLayout
    from kivy.core.window import Window

except:
    print("*******************************")
    print("  error in importing packages  ")
    print("*******************************")

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super(HomeScreen, self).__init__(**kwargs)
        self.NowWindow = "HomeWindow"
        self.drawGUI()

        self.keysPressed = set()
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        self._keyboard.bind(on_key_up=self._on_key_up)

        self.acc = 0
        self.brake = 0
        self.steer = 0
        Clock.schedule_interval(self.checkMoves, 0)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self, keyboard, keycode, text, modifiers):
        self.keysPressed.add(keycode[1])

    def _on_key_up(self, keyboard, keycode):
        text = keycode[1]
        if text in self.keysPressed:
            self.keysPressed.remove(text)

    def checkMoves(self, dt):
        if "down" in self.keysPressed:
            self.acc = 0
            self.brake += dt * 60
        elif "up" in self.keysPressed:
            self.acc += dt * 25
            self.brake = 0
        else:
            self.acc *= 0.9
            self.brake = 0
        if "left" in self.keysPressed:
            self.steer -= dt * 15
        elif "right" in self.keysPressed:
            self.steer += dt * 15
        else:
            self.steer *= 0.9
        steer = int(round(140 + self.steer))
        steer = min(180, steer)
        steer = max(100, steer)
        acc = int(round(100 + self.acc))
        acc = min(200, acc)
        acc = max(100, acc)
        brake = int(round(100 + self.brake))
        brake = min(200, brake)
        brake = max(100, brake)
        self.btnSteer.text = "steer : " + str(steer)
        self.btnAcc.text = "acc : " + str(acc)
        self.btnBrake.text = "brake : " + str(brake)
        line = "/200"
        line += str(steer)
        line += str(brake)
        line += str(acc)
        line += "00\\n"
        file = open("kivyCar.txt", "w")
        file.write(line)
        file.close()

    def drawGUI(self):
        grid = GridLayout(cols=1, size_hint=(1.0, 1.0), pos_hint={"center_x": 0.5, "center_y": 0.5})
        self.add_widget(grid)

        self.btnSteer = Button(text="steer : ", font_size=30)
        grid.add_widget(self.btnSteer)
        self.btnAcc = Button(text="acc : ", font_size=30)
        grid.add_widget(self.btnAcc)
        self.btnBrake = Button(text="brake : ", font_size=30)
        grid.add_widget(self.btnBrake)

class MainClass(App):
    def build(self):
        ScreenMan = ScreenManagerbuild()
        ScreenMan.add_widget(HomeScreen(name='HomeWindow'))

        return ScreenMan

class ScreenManagerbuild(ScreenManager):
    pass


if __name__ == '__main__':
    MainClass().run()
