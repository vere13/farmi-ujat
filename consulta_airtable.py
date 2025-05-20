import flet as ft
import nube as nb 

def main(page: ft.Page):
    #Configuración de la página
    page.title = "Consultas"
    page.theme_mode = "light"
    page.window_resizable = False  # Evita que la ventana cambie de tamaño
    page.scroll = True
    page.appbar = ft.AppBar(leading=ft.Icon("receipt_long"),title=ft.Text("Recetas UJAT"), center_title=True, bgcolor="blue", color="white")
    
    #Componentes de la página
    encabezado = [
        ft.DataColumn(ft.Text("Medicamento")),
        ft.DataColumn(ft.Text("Interacciones")) 
    ]
    filas = []
    datos = nb.Receta.all()
    for d in datos:
        celda1 = ft.DataCell(ft.Text(d.medicamento)) # Descripción en negritas
        celda2 = ft.DataCell(ft.Text(d.interacciones))
        fila = ft.DataRow([celda1,celda2])
        filas.append(fila)
    
    tbl_medicamentos = ft.DataTable(
        columns=encabezado,
        rows=filas
    )
    page.add(tbl_medicamentos)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)    