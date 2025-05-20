from pyairtable.orm import Model
from pyairtable.orm import fields as F

class Receta(Model):
    medicamento = F.TextField("medicamento")
    interacciones = F.TextField("interacciones")
    class Meta:
        api_key = "pate7l6078wsd5TRg.ae34d9d2e445781f48ebd8bba4e083d1928c6d0dfb2bf6b87c72b09a9553ec3e"
        base_id = "appqRi1V9VbiTENdc"
        table_name = "receta"
