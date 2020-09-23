import os
import kivy

from kivy.app import App

from kivy.core.window import Window

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.metrics import dp, sp
from kivy.properties import ListProperty


class SummaryGrid(GridLayout):
    def __init__(self, **kwargs):
        super(SummaryGrid, self).__init__(**kwargs)
        self.cols = 2

        self.col1_width = dp(225)
        self.col2_width = dp(150)

        for x in range(0, 100, 1):
            accountx = Label(text=f'Target Retirement 2055',
                             size_hint_x=None,
                             size_hint_y=None,
                             width=self.col1_width,
                             height=dp(35),
                             color='#748b75')

            balancex = Label(text='$100,000.00',
                             size_hint_x=None,
                             size_hint_y=None,
                             width=self.col2_width,
                             height=dp(35))

            self.add_widget(accountx)
            self.add_widget(balancex)


# Links to the *.kv file named Homescreen.kv.
# the kv file will build the internal structure of the application
class Interface(BoxLayout):
    pass


class HomeScreenApp(App):
    def __init__(self):
        super(HomeScreenApp, self).__init__()

    def build(self):
        Window.size = (dp(375), dp(775))
        root_widget = Interface()
        return root_widget


if __name__ == "__main__":
    HomeScreenApp().run()
