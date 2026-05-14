# 导入Kivy核心库
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.core.text import LabelBase

# 注册中文字体（Windows系统自带微软雅黑）
LabelBase.register(name="zh_font", fn_regular="C:/Windows/Fonts/msyh.ttc")

# 设置窗口大小（模拟手机屏幕）
Window.size = (360, 640)

# 主界面布局
class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 30
        self.spacing = 20

        self.title_label = Label(
            text="我的第一个Python安卓App",
            font_name="zh_font",
            font_size=22,
            bold=True
        )
        self.add_widget(self.title_label)

        self.btn = Button(
            text="点我试试",
            font_name="zh_font",
            font_size=18,
            background_color=(0.2, 0.6, 1, 1)
        )
        self.btn.bind(on_press=self.on_click)
        self.add_widget(self.btn)

    def on_click(self, instance):
        self.title_label.text = "恭喜！运行成功！"

class MyFirstApp(App):
    def build(self):
        self.title = "Python安卓Demo"
        return MainLayout()

if __name__ == "__main__":
    MyFirstApp().run()
