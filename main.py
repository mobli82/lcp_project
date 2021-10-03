from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.graphics.context_instructions import Color
from kivy.properties import StringProperty, Clock

from utils import check_temparatures

import time
from kivy.graphics.vertex_instructions import Rectangle

class MainBoxLayout(Widget):
    boiler_status = StringProperty("")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        
        Clock.schedule_interval(self.update, 1)

        self.bind(
            size = self._update_rectangle,
            pos = self._update_rectangle
        )

        with self.canvas.before:
            Color(.21, .05, .30, 1)

            self.rect = Rectangle(
                pos = self.pos,
                size = self.size
            )

    def _update_rectangle(self, insatnce, value):
        self.rect.size = insatnce.size
        self.rect.pos = insatnce.pos


    def update(self, dt):
        _, _, rest_tem = check_temparatures()

        self.boiler_status = rest_tem

    pass
   
class LcpProject(App):
    pass



LcpProject().run()