from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.icon_definitions import md_icons

from utils import check_temparatures
from kivy.properties import StringProperty, Clock

RR_ALGO_BUTTON_UID = {
            536: 'RR_PRACA_PODANIE',
            605: 'RR_PRACA_POSTOJ',
            674: 'RR_PRACA_MOC',
            830: 'RR_PRACA_PODANIE',
            899: 'RR_PRACA_POSTOJ',
            968: 'RR_PRACA_MOC'
        }

class MainView(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        Clock.schedule_interval(self.update, 1)


    def update(self, dt):
        _, _, temps = check_temparatures()
        
        boiler_status = MDApp.get_running_app().root.ids['boiler_status']

        # print(type(temps))

        boiler_status.text = temps
    
    def upgrade_value(self, widget):
        
        rr_value = MDApp.get_running_app().root.ids[RR_ALGO_BUTTON_UID[widget.uid]]
        foo = int(rr_value.text)
        
        if widget.uid in(536,605,674):
            foo -= 1
        else:
            foo += 1

        rr_value.text = str(foo)

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'LightGreen'
        return Builder.load_file('lcpproject.kv')

MainApp().run() 