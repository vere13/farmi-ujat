import flet as ft
import modelo as md

def main(page: ft.Page):
   
    page.title = "Consultas"
    page.theme_mode = "light"
    page.window.width = 800
    page.window.height = 600
    page.window_resizable = False
    page.scroll = True
    page.appbar = ft.AppBar(leading=ft.Icon("receipt_long"), title=ft.Text("Listado de medicamentos UJAT"), center_title=True, bgcolor="blue", color="white")

    encabezado = [
        ft.DataColumn(ft.Text("Descripción", width=200)),
        ft.DataColumn(ft.Text("Presentación", width=200)),
        ft.DataColumn(ft.Text("Clasificación", width=200)),
        ft.DataColumn(ft.Text("Nivel de atención", width=100)),
        ft.DataColumn(ft.Text("Sustancia activa", width=200))  
    ]
    filas = []
    try:
        medicinas = md.Medicamento.select()
        
        for med in medicinas:
            celda1 = ft.DataCell(ft.Text(med.descripcion, weight="bold"))
            celda2 = ft.DataCell(ft.Text(med.presentacion))
            celda3 = ft.DataCell(ft.Text(med.clasificacion, italic=True))
            celda4 = ft.DataCell(ft.Text(med.nivel_atencion))
            celda5 = ft.DataCell(ft.Text(med.nombre_farmaco.nombre if med.nombre_farmaco else "Sin fármaco", color="pink"))
            fila = ft.DataRow([celda1, celda2, celda3, celda4, celda5])
            filas.append(fila)

    except Exception as e:
        print(f"Error al consultar medicamentos: {e}")

    tbl_medicamentos = ft.DataTable(columns=encabezado, rows=filas)

    page.add(tbl_medicamentos)
    page.update()
    
if __name__ == "__main__":
    ft.app(target=main)    