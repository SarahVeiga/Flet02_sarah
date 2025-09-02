import flet as ft

def main(page: ft.Page):

    page.title = "Calculadora de IMC"
    page.padding = ft.padding.only(top=40, left=20, right=20, bottom=20)
    page.theme_mode = ft.ThemeMode.LIGHT  

    peso = ft.TextField(label="🏋️ Peso (kg)", width=200, keyboard_type=ft.KeyboardType.NUMBER)
    altura = ft.TextField(label="📏 Altura (m)", width=200, keyboard_type=ft.KeyboardType.NUMBER)

    resultado = ft.Text(
        "Digite os valores e clique em Calcular",
        size=20, 
        text_align=ft.TextAlign.CENTER, 
        color=ft.Colors.GREY_600 
    )

    def calcular(e):
        try:

            p = float(peso.value)
            a = float(altura.value)

            # Verificação se altura é maior que zero para evitar divisão por zero
            if a <= 0:
                resultado.value = "❌ Erro: altura deve ser maior que zero!"
                resultado.color = ft.Colors.RED # Texto de erro aparecer em vermelho
            else:
                # Cálculo do IMC Peso / (Altura * Altura)
                imc = p / (a * a)

                # Classificação do IMC
                if imc < 18.5:
                    classificacao = "Baixo peso"
                    cor = ft.Colors.ORANGE
                elif 18.5 <= imc < 25:
                    classificacao = "Peso normal"
                    cor = ft.Colors.GREEN
                elif 25 <= imc < 30:
                    classificacao = "Sobrepeso"
                    cor = ft.Colors.AMBER
                else:
                    classificacao = "Obesidade"
                    cor = ft.Colors.RED
                # Exibição do resultado com duas casas decimais
                resultado.value = f"📊 Seu IMC é {imc:.2f} → {classificacao}"
                resultado.color = cor

        # Tratamento de erro para valores inválidos
        except ValueError:
            resultado.value = "❌ Digite números válidos!"
            resultado.color = ft.Colors.RED
        # Atualizar a página para mostrar o resultado
        page.update()

    # Função para criar a AppBar com cores dinâmicas
    def criar_appbar():
        # Definir cor do texto com base no tema atual
        cor_texto = ft.Colors.BLACK if page.theme_mode == ft.ThemeMode.LIGHT else ft.Colors.WHITE
        # Retornar a AppBar configurada
        return ft.AppBar(
            # Ícone e título
            leading=ft.Icon(ft.Icons.MULTILINE_CHART, color=cor_texto),
            # Configurações da AppBar
            leading_width=40,
            # Título da AppBar
            title=ft.Text("Calculadora IMC", color=cor_texto),
            # Configurações visuais
            center_title=False,
            # Cores de fundo e ações
            bgcolor=ft.Colors.ON_SURFACE_VARIANT,
            # Ações na AppBar
            actions=[
                ft.Row(
                    # Ícones e switch para alternar tema
                    controls=[
                        ft.Text("☾", color=cor_texto),
                        ft.Switch(value=(page.theme_mode == ft.ThemeMode.DARK), on_change=alternar_tema),
                        ft.Text("𖤓", color=cor_texto),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
        )
    
    # Alternância entre tema claro e escuro
    def alternar_tema(e):
        page.theme_mode = (
            # Se o tema atual for claro, mude para escuro, e vice-versa
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.appbar = criar_appbar()  # Atualiza AppBar com as novas cores
        # Carregar na página o tema atualizado
        page.update()

   # Definir AppBar inicial
    page.appbar = criar_appbar()


    # Função limpar
    def limpar(e):
        # Limpar os campos de entrada e o resultado
        peso.value = altura.value = ""
        resultado.value = "Digite os valores e clique em Calcular"
        resultado.color = ft.Colors.GREY_600
        # Atualizar a página para mostrar os campos limpos
        page.update()

    # Interface
    page.add(
        ft.Column([
            # Título da aplicação
            ft.Text("🧮 Calculadora de IMC", size=24, weight=ft.FontWeight.BOLD),
            altura,
            peso,
            # Linha com botões Calcular e Limpar
            ft.Row([
                ft.ElevatedButton("🟢 Calcular", on_click=calcular, width=150,
                                  bgcolor=ft.Colors.GREEN, color=ft.Colors.WHITE),
                ft.ElevatedButton("🧹 Limpar", on_click=limpar, width=150,
                                  bgcolor=ft.Colors.GREY, color=ft.Colors.WHITE),
            ],
            # Alinhamento central e espaçamento entre os botões
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20),
            ft.Divider(),
            resultado
        ],
        # Alinhamento central e espaçamento entre os elementos
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20)
    )

# Executar o app
ft.app(target=main)