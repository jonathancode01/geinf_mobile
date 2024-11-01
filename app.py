import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Definir a classe principal do aplicativo
class MeuApp(App):
    def build(self):
        # Definir a cor de fundo da janela
        Window.clearcolor = (0.9, 0.9, 0.9, 1)  # Cor de fundo cinza claro

        # Criar um layout vertical
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Criar um título 
        titulo = Label(
            text="Geinf - Gerencia de infraestrutura", 
            font_size=40, 
            size_hint=(1, 0.3),
            color=(0.1, 0.4, 0.6, 1)  # Cor do texto azul escuro
        )



        # Conectar o botão à função que será executada quando o botão for clicado
        botao.bind(on_press=self.mostrar_mensagem)

        # Adicionar o título e o botão ao layout
        layout.add_widget(titulo)  # Adicionar o título ao layout
        layout.add_widget(botao)   # Adicionar o botão ao layout

        return layout

    # Função para mostrar uma mensagem quando o botão for clicado
    def mostrar_mensagem(self, instance):
        print("Você clicou no botão! Bem-vindo ao app Kivy.")

# Executar o aplicativo
if __name__ == "__main__":
    MeuApp().run()
