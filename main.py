from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.core.window import Window

# Set the window to be transparent (Note: Only works on some Android versions natively)
Window.clearcolor = (0, 0, 0, 0) 

class GuidelineWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0, 1, 0, 0.8)  # Bright Green Line
            self.line = Line(points=[100, 100, 500, 500], width=2)
            
            Color(1, 0, 0, 0.8)  # Red Circle for the target ball
            self.target = Line(circle=(500, 500, 25), width=2)

    def on_touch_move(self, touch):
        # Update line to follow your finger
        # touch.x and touch.y is where you are pressing
        self.line.points = [touch.x, touch.y, touch.x + 300, touch.y + 300]
        self.target.circle = (touch.x + 300, touch.y + 300, 25)

class PoolHelperApp(App):
    def build(self):
        return GuidelineWidget()

if __name__ == "__main__":
    PoolHelperApp().run()