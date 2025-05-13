import flet as ft

def main(page: ft.Page):
    page.title = "FARMI-UJAT"
    page.appbar = ft.AppBar(
        title=ft.Text("FARMI-UJAT", size=40),
        center_title=True
    )
    btn_interacciones = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("medication", size=40, color="black"),
                    ft.Text("Interacciones medicamentosas", text_align=ft.TextAlign.CENTER, color="black")
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            #side=ft.BorderSide(1, "white")
        ),
        bgcolor="white",
        color="white",
        width=200
    )

    btn_medicamento = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("add_box", size=40, color="black"),
                    ft.Text("Medicamento nuevo", text_align=ft.TextAlign.CENTER, color="black")
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            #side=ft.BorderSide(1, "orange")
        ),
        bgcolor="white",
        color="white",
        width=200
    )

    btn_listado_medicamento = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("VIEW_LIST", size=40, color="black"),
                    ft.Text("Listado medicamento", text_align=ft.TextAlign.CENTER, color="black")
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            #side=ft.BorderSide(1, "orange")
        ),
        bgcolor="white",
        color="white",
        width=200
    )

    # Fila de botones centrada
    fila_botones = ft.Row(
        controls=[btn_interacciones, btn_medicamento, btn_listado_medicamento],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
        wrap=True  # por si no cabe en pantallas pequeñas
    )

    page.add(ft.Divider(color = "black"))
    page.add(fila_botones)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)    