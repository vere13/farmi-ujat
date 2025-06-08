from pyairtable.orm import Model
from pyairtable.orm import fields as F

class Farmaco(Model):
    nombre = F.TextField("nombre")
    descripcion = F.TextField("descripcion")
    categoria = F.MultipleSelectField("categoria")
    interacciones = F.TextField("interacciones")
    class Meta:
        api_key = "patqSlNV5SuaLcvbz.c5888705c580bb65eac6921cbef3629c0c9f36840131017cadd9c90471c3aaf5"
        base_id = "appBHRKfxAkRl6yFD"
        table_name = "farmaco"
