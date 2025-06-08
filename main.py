import flet as ft
import consulta_airtable as cat
import altas_farmaco as alf
import lista_medicamento as lis

def main(page: ft.Page):

    def mostrar_interacciones(e: ft.ControlEvent):
        page.clean()
        cat.main(page)
    
    def mostrar_medicamentos(e: ft.ControlEvent):
        page.clean()
        alf.main(page)
    
    def mostrar_consulta(e: ft.ControlEvent):
        page.clean()
        lis.main(page)

    page.title = "FARMI-UJAT"
    page.bgcolor = "white"  # Fondo blanco
   
    # Estilo base para los botones
    estilo_boton = ft.ButtonStyle(
        bgcolor=ft.Colors.GREY_200,  # gris claro
        shape=ft.RoundedRectangleBorder(radius=8),  # esquinas redondeadas, pero no tanto
        side=ft.BorderSide(width=0),  # sin borde visible
        overlay_color=ft.Colors.TRANSPARENT
    )
    
    # Botones para la barra lateral
    btn_home = ft.ElevatedButton(text="Cerrar sesión", width=150, style=estilo_boton,  color="black")
    btn_usuarios = ft.ElevatedButton(text="Inicio", width=150, style=estilo_boton,  color="black")
    btn_config = ft.ElevatedButton(text="Configuración", width=150, style=estilo_boton,  color="black")

    # Barra lateral izquierda
    barra_lateral = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon("ACCOUNT_CIRCLE_OUTLINED", size=80, color="black"),
                ft.Text("Farmacéutico", size=18, color="black"),
                btn_home,
                ft.Container(expand=True),
                btn_usuarios,
                btn_config,
            ],
            alignment=ft.MainAxisAlignment.START,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True,
            spacing=10
        ),
        bgcolor=ft.Colors.GREEN_ACCENT_400,
        padding=20,
        width=200,
        expand=True
    )

    #Botones principales
    btn_interacciones = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("WARNING_AMBER_OUTLINED", size=200, color=ft.Colors.RED_400),
                    ft.Text("Interacciones medicamentosas", text_align=ft.TextAlign.CENTER, color="black", size=16)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER 
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        bgcolor="white",
        color="white",
        width=400,
        on_click = mostrar_interacciones
    )

    btn_medicamento = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("MEDICAL_SERVICES_OUTLINED", size=200, color=ft.Colors.TEAL_ACCENT_700),
                    ft.Text("Alta de medicamentos", text_align=ft.TextAlign.CENTER, color="black", size=16)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        bgcolor="white",
        color="white",
        width=300,
        on_click=mostrar_medicamentos
    )

    btn_listado_medicamento = ft.FilledButton(
        content=ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon("CHECKLIST_RTL_ROUNDED", size=200, color=ft.Colors.ORANGE_400),
                    ft.Text("Listar medicamento", text_align=ft.TextAlign.CENTER, color="black", size=16)
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=10
        ),
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
        ),
        bgcolor="white",
        color="white",
        width=400,
        on_click=mostrar_consulta
    )

    fila_botones = ft.Row(
        controls=[btn_interacciones, btn_medicamento, btn_listado_medicamento],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=30,
        wrap=True
    )

    contenedor_central = ft.Column(
    controls=[
        ft.Container(
            content=ft.Text("FARMI-UJAT", size=60, weight=ft.FontWeight.BOLD, color="black"),
            padding=ft.Padding(top=10, bottom=100, left=20, right=20)  # Aumenta el espacio debajo del encabezado
        ),
        fila_botones
    ],
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    expand=True
)

    # Layout general con barra lateral + contenido
    layout = ft.Row(
        controls=[
            ft.Container(content=barra_lateral, width=200),
            ft.Container(content=contenedor_central, expand=True)
        ],
        expand=True
    )

    page.add(layout)
    page.update()

ft.app(target=main, view=ft.AppView.WEB_BROWSER)

