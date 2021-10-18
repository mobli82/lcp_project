from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.icon_definitions import md_icons

from utils import check_temparatures
from kivy.properties import StringProperty, Clock

from functools import partial

import requests

import time

class RRalgorythmView(MDBoxLayout):
    pass

class CwuCycleView(MDBoxLayout):
    pass

class BoilerMonitorView(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_temps, 1)

    def update_temps(self, dt):
        bolier_temp, boiler_return_temp, feeder_temp, cwu_temp, co_temp = check_temparatures()
        
        print(BoilerMonitorView().ids)
        boiler_temperature = self.ids.BOILER_TEMPERATURE
        boiler_return = self.ids.BOILERS_RETURN
        feeder = self.ids.FEEDER
        cwu = self.ids.CWU
        co = self.ids.CO
        
        boiler_temperature.text = str(bolier_temp)
        boiler_return.text = str(boiler_return_temp)
        feeder.text = str(feeder_temp)
        cwu.text = str(cwu_temp)
        co.text = str(co_temp)

class MainView(MDBoxLayout):
    
    def upgrade_value(self, widget_input, widget_label):
        value = widget_input.text
        key = widget_label.text
        
        server_response = self.ids.server_response

        print(f'Key: {key}, value: {value}')
        
        if key and value:
            r = requests.get(f'http://192.168.1.2/set{key}={value}')

        server_response.text = 'Record Upgraded'

        Clock.schedule_once(self.hide_server_record_label, 2)
    
    def hide_server_record_label(self, dt):
        server_response = self.ids.server_response
        server_response.text = " "

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'LightGreen'
        # self.theme_font_styles = 'H2'
        return Builder.load_file('lcpproject.kv')

MainApp().run() 