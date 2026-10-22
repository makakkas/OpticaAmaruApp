from django.db import models


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True) ## id (clave primaria)
    intentos_fallidos = models.PositiveSmallIntegerField(default=0)
    bloqueado_hasta = models.DateTimeField(null=True, blank=True)




