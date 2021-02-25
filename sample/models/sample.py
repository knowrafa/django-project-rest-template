import uuid

from django.db import models

# Create your models here.


class Sample(models.Model):
    id = models.UUIDField(primary_key=True, verbose_name=_('uuid'), default=uuid.uuid4,
                          editable=False, unique=True)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'sample'
        unique_together = ['id', 'nome']