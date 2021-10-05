from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.icon_definitions import md_icons

from utils import check_temparatures
from kivy.properties import StringProperty, Clock



class MainApp(MDApp):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.update, 1)

    def update(self, dt):
        _, _, temps = check_temparatures()
        
        boiler_status = MainApp.get_running_app().root.ids['boiler_status']

        boiler_status.text = temps
    
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'LightGreen'
        return Builder.load_file('lcpproject.kv')

MainApp().run() 