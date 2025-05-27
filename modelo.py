import peewee as pw
from peewee import IntegrityError

# Conexión correcta a SQLite
farmacia_ujat = pw.SqliteDatabase("Farmacia_ujat_P3.db")

# Modelo Farmaco
class Farmaco(pw.Model):
    nombre = pw.CharField(max_length=255, primary_key=True)
    descripcion = pw.CharField(max_length=255)
    categoria = pw.CharField(max_length=250)
    interacciones = pw.CharField(max_length=5000, null=True)  # Interacciones con otros medicamentos

    class Meta:
        database = farmacia_ujat

# Modelo Medicamento
class Medicamento(pw.Model):
    id = pw.IntegerField(primary_key=True)
    clave = pw.CharField(max_length=255)
    descripcion = pw.CharField(max_length=100)
    presentacion = pw.CharField(max_length=255)
    clasificacion = pw.CharField(max_length=255)
    nivel_atencion = pw.CharField(max_length=255)
    nombre_farmaco = pw.ForeignKeyField(
        column_name="nombre_farmaco",
        model=Farmaco,
        field="nombre",
        null=True
    )

    class Meta:
        database = farmacia_ujat

# Crear tablas si no existen
farmacia_ujat.connect()
farmacia_ujat.create_tables([Farmaco, Medicamento])

# Función para guardar un fármaco
def guardar_farmaco(nombre, descripcion, categoria, interacciones):
    try:
        if Farmaco.select().where(Farmaco.nombre == nombre).exists():
            print("Ya existe un fármaco con ese nombre.")
            return "duplicado"

        Farmaco.create(
            nombre=nombre,
            descripcion=descripcion,
            categoria=categoria,
            interacciones=interacciones
        )
        print("Fármaco guardado con éxito.")
        return "exito"

    except IntegrityError as e:
        print(f"Error de integridad: {e}")
        return "error"

    except Exception as e:
        print(f"Otro error: {e}")
        return "error"

