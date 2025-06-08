import flet as ft
import modelo as md

def main(page: ft.Page):
    #Configuración de la página
    page.title = "Farmaco"
    page.theme_mode = "light"
    page.window.width = 1200
    page.window.height = 600
    page.window_resizable = False  # Evita que la ventana cambie de tamaño
    page.scroll = True
    page.appbar = ft.AppBar(leading=ft.Icon("receipt_long"),title=ft.Text("Listado de farmaco UJAT"), center_title=True, bgcolor="blue", color="white")
    
    #Componentes de la página
    encabezado = [
        ft.DataColumn(ft.Text("Nombre", width=200)),
        ft.DataColumn(ft.Text("Descripcion", width=200)),
        ft.DataColumn(ft.Text("Categoria", width=200)),
        ft.DataColumn(ft.Text("Interacciones", width=200)),
    ]
    filas = []
    farmacos = md.Farmaco.select()
    for med in farmacos:
        celda1 = ft.DataCell(ft.Text(med.nombre, weight="bold")) 
        #celda2 = ft.DataCell(ft.Text(med.descripcion))

        celda2 = ft.DataCell(
            ft.Column(
                [ft.Text(med.descripcion)],
                scroll=True,  # Permite el desplazamiento en la columna
                width=400,  # Ancho ajustado para la descripción
                height=60  # Ajusta la altura para que el texto largo se vea completo
            )
        )


        celda3 = ft.DataCell(ft.Text(med.categoria))  
        celda4 = ft.DataCell(ft.Text(med.interacciones, color="red"))
        fila = ft.DataRow([celda1,celda2,celda3,celda4])
        filas.append(fila)
    
    tbl_farmaco = ft.DataTable(
        columns=encabezado,
        rows=filas
    )
    page.add(tbl_farmaco)
    page.update()

ft.app(target=main)    