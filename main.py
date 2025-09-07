# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.core.window import Window

# צבע רקע בהיר (לא חובה)
Window.clearcolor = (1, 1, 1, 1)

# חשוב: ודא שקובץ הפונט נמצא ליד main.py בשם הזה.
# אם יש לך שם אחר – שנה כאן וב-buildozer.spec (ראו למטה).
LabelBase.register(name="Hebrew", fn_regular="NotoSansHebrew-Regular.ttf")

KV = """
<Root>:
    orientation: "vertical"
    padding: dp(24)
    spacing: dp(16)

    Label:
        text: "ברוך הבא"
        font_name: "Hebrew"
        color: 0, 0, 0, 1
        font_size: "28sp"
        halign: "center"
        text_size: self.width, None
        size_hint_y: None
        height: self.texture_size[1]

    Button:
        text: "סגור"
        font_name: "Hebrew"
        size_hint_y: None
        height: dp(48)
        on_release: app.stop()
"""

Builder.load_string(KV)

class Root(BoxLayout):
    pass

class HelloApp(App):
    def build(self):
        return Root()

if __name__ == "__main__":
    HelloApp().run()
