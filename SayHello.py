import contextlib
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.factory import Factory
from kivy.core.window import Window

class SayHello(App):
    Window.clearcolor = ('#001427')

    def build(self):
        self.window = GridLayout()
        
        self.window.rows = 5
        self.window.size_hint = (0.6,0.7)
        self.window.pos_hint = {"center_x":0.5,"center_y":0.5}
        #add widgets to window
        
        self.janela_inicial()
       
        
        return self.window
    def guardar(self):
        self.greeting = Label(text="what's your name?",
                              font_size = 18,
                              color='#00FFCE')
        self.window.add_widget(self.greeting)
        self.vaitomanocu = Label(text=("vaitomanocu"))
        
        
        self.user = TextInput(multiline = False,
                              padding_y=(20,20),
                              size_hint = (0.5, 0.5)
                              )
        
        
        
        self.window.add_widget(self.user)
        #button
        self.button = Button(text = "Greet",
                             size_hint = (1,0.5),
                             bold = True,
                             background_color = '#00FFCE'
                             )
        
        self.button.bind(on_press=self.callback)
        self.window.add_widget(self.button)

    
    def janela_inicial(self):
        self.botao_yt_link_dl = Button(text='YT link downloader',size_hint = (1,0.5),background_color='#7D82B8',color='#3cb371')
                
        self.botao_yt_link_dl.bind(on_press=self.teste)

        self.window.add_widget(self.botao_yt_link_dl)
        
        self.window.add_widget(Label(size_hint = (0.1, 0.1)))
        
        self.botao_yt_link_dl_ct = Button(text='YT link downloader and cutter',size_hint = (1,0.5),background_color='#7D82B8',color='#3cb371')
        self.window.add_widget(self.botao_yt_link_dl_ct)
        
        self.window.add_widget(Label(size_hint = (0.1, 0.1)))
        
        self.botao_ct = Button(text='File cutter',size_hint = (1,0.5),background_color='#7D82B8',color='#3cb371')
        self.window.add_widget(self.botao_ct)
    def teste(self,instance):
        self.window.clear_widgets()
        
        
        
    def callback(self,instance):
        self.greeting.text = f"hello {self.user.text}!"

        with contextlib.suppress(Exception):
            self.window.add_widget(self.vaitomanocu)
            

        

if __name__ == "__main__":
    SayHello().run()
