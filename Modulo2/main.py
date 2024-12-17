# import flet as ft

# def main(page: ft.Page):
#     page.title = "Flet counter example"
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=80)

#     def minus_click(e):
#         txt_number.value = str(int(txt_number.value) - 1)
#         page.update()

#     def plus_click(e):
#         txt_number.value = str(int(txt_number.value) + 1)
#         page.update()

#     page.add(
#         ft.Row(
#             [
#                 ft.IconButton(ft.Icons.REMOVE, on_click=minus_click),
#                 txt_number,
#                 ft.IconButton(ft.Icons.ADD, on_click=plus_click),
#             ],
#             alignment=ft.MainAxisAlignment.CENTER,
#         )
#     )

# ft.app(main)



import flet as ft

def main(page: ft.Page):
    # Função para exibir os valores dos campos de texto
    def button_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()
    def clear_clicked(e):
        t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update()

    # Criação dos componentes de forma compacta
    tb1 = ft.TextField(label="E-mail", hint_text="Digite seu E-mail")
    tb2 = ft.TextField(label="Nome", hint_text="Digite seu nome")
    tb3 = ft.TextField(label="Sobrenome", hint_text="Digite seu sobrenome")
    tb4 = ft.TextField(label="Idade", hint_text="Digite a sua idade")
    tb5 = ft.TextField(label="Defina você em uma palavra", icon=ft.Icons.EMOJI_EMOTIONS)
    t = ft.Text()

    # Botão para acionar a função
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    c = ft.ElevatedButton(text="Clear", on_click=clear_clicked)

    # Adiciona os componentes à página de uma vez só
    page.add(tb1, tb2, tb3, tb4, tb5, b, c, t)

# Executa o app
ft.app(main)