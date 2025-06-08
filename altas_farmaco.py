import flet as ft
from nube_dos import Farmaco

def main(page: ft.Page):
    page.title = "Alta de medicamentos"
    page.theme_mode = "light"
    page.window.width = 450
    page.window.height = 400
    page.window_resizable = False
    page.appbar = ft.AppBar(
        leading=ft.Icon("medical_services"),
        title=ft.Text("Nuevo Medicamento"),
        center_title=True,
        bgcolor="green",
        color="white"
    )

    # Campos de texto
    txt_nombre = ft.TextField(label="Nombre", multiline=True, min_lines=1, max_lines=3, width=400)
    txt_descripcion = ft.TextField(label="Descripcion", multiline=True, min_lines=1, max_lines=3, width=400)
    txt_categoria = ft.TextField(label="Categoria (separadas por comas)", multiline=True, min_lines=1, max_lines=3, width=400)
    txt_interacciones = ft.TextField(label="Interacciones", multiline=True, min_lines=1, max_lines=3, width=400)

    # Función para guardar
    def guardar_farmaco(e: ft.ControlEvent):
        nombre = txt_nombre.value.strip()
        descripcion = txt_descripcion.value.strip()
        categoria = [c.strip() for c in txt_categoria.value.split(",")] if txt_categoria.value else []
        interacciones = txt_interacciones.value.strip()

        if not nombre or not descripcion:
            page.snack_bar = ft.SnackBar(ft.Text("Nombre y descripción son obligatorios."), bgcolor="red")
            page.snack_bar.open = True
            page.update()
            return

        existentes = list(Farmaco.all())
        if any(f.nombre.lower() == nombre.lower() for f in existentes):
            page.snack_bar = ft.SnackBar(ft.Text("Ya existe un fármaco con ese nombre."), bgcolor="orange")
            page.snack_bar.open = True
            page.update()
            return

        try:
            nuevo = Farmaco(
                nombre=nombre,
                descripcion=descripcion,
                categoria=categoria,
                interacciones=interacciones
            )
            nuevo.save()  # <-- Aquí guardas el nuevo registro
            page.snack_bar = ft.SnackBar(ft.Text("Fármaco guardado correctamente."), bgcolor="green")

            # Limpiar campos
            txt_nombre.value = ""
            txt_descripcion.value = ""
            txt_categoria.value = ""
            txt_interacciones.value = ""
        except Exception as ex:
            print("Error al guardar:", ex)
            page.snack_bar = ft.SnackBar(ft.Text("Error al guardar. Revisa la consola."), bgcolor="red")

        page.snack_bar.open = True
        page.update()

    btn_guardar = ft.ElevatedButton(
        text="Guardar",
        icon="save",
        icon_color="white",
        bgcolor="blue",
        color="white",
        width=150,
        on_click=guardar_farmaco
    )

    btn_cancelar = ft.ElevatedButton(
        text="Cancelar",
        icon='close',
        icon_color="white",
        bgcolor='red',
        color='white',
        width=150,
        on_click=lambda e: page.window_destroy()
    )

    fila_boton = ft.Row([btn_guardar, btn_cancelar], alignment="Center")

    page.add(txt_nombre, txt_descripcion, txt_categoria, txt_interacciones, fila_boton)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
