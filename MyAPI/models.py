from django.db import models
from django.forms import model_to_dict ## convierte entidad a diccionario
from DjangoAPI.models import BaseModel
from crum import get_current_user

# Create your models here.
class clasificacion(models.Model):
    MATERIALES = (
        ('Plastico', 'Plastico'),
        ('Vidrio', 'Vidrio'),
        ('Ceramica', 'Ceramica')
    )
    descripcion = models.CharField(max_length=20)
    material = models.CharField(max_length=20, choices=MATERIALES)

    def __str__(self):
        return self.descripcion

class Chapter(BaseModel):
    chapter = models.CharField(max_length=11, verbose_name='Capítulo', unique=True)
    description = models.CharField(max_length=500, verbose_name='Descripción')

    def __str__(self):
        return self.chapter

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Chapter, self).save()


    def toJSON(self):
        item = model_to_dict(self, exclude=['user_creation', 'user_updated'])
        return item
    class Meta:
        verbose_name = 'Capitulo'
        verbose_name_plural = 'Capitulos'
        ordering = ['chapter']

class Classification(models.Model):
    MATERIALES = (
        ('Plastico', 'Plástico'),
        ('Vidrio', 'Vidrio'),
        ('Ceramica', 'Cerámica'),
    )
    description = models.CharField(max_length=50, verbose_name='Descripción')
    material = models.CharField(max_length=25, choices=MATERIALES, verbose_name='Material')
    # classify = models.CharField(max_length=15, verbose_name='Clasificación Arancelaria', null=True, blank=True)
    classify = models.CharField(max_length=25)

    def __str__(self):
        return self.classify

    # def save(
    #     self, force_insert=False, force_update=False, using=None, update_fields=None
    # ):
    #     super(Classification, self).save()
    #     user = get_current_user()
    #     if user is not None:
    #         if not self.pk:
    #             self.user_creation = user
    #         else:
    #             self.user_updated = user
    #     super(Classification, self).save()

    def toJSON(self):
        # item = {'id': self.id, 'chapter': self.chapter, 'descripcion': self.description}
        item = model_to_dict(self)
        print("entro de método toJSON de Classification")
        return item
    class Meta:
        verbose_name = 'Clasificación'
        verbose_name_plural = 'Clasificaciones'
        ordering = ['classify']

class Position(BaseModel):
    position = models.CharField(max_length=15, verbose_name='Posición', unique=True)
    description = models.CharField(max_length=1500, verbose_name='Descripción')

    def __str__(self):
        return self.position

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Position, self).save()

    def toJSON(self):
        item = model_to_dict(self, exclude=['user_creation', 'user_updated'])
        return item

    class Meta:
        verbose_name = 'Posición arancelaria'
        verbose_name_plural = 'Posiciones arancelarias'
        ordering = ['position']

class Classification2(BaseModel):
    MATERIALES = (
        ('Plastico', 'Plástico'),
        ('Vidrio', 'Vidrio'),
        ('Ceramica', 'Cerámica'),
    )
    description = models.CharField(max_length=50, verbose_name='Descripción')
    material = models.CharField(max_length=25, choices=MATERIALES, verbose_name='Material')
    # classify = models.CharField(max_length=15, verbose_name='Clasificación Arancelaria', null=True, blank=True)
    classify = models.CharField(max_length=25)

    def __str__(self):
        return self.classify

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        user = get_current_user()
        if user is not None:
            if not self.pk:
                self.user_creation = user
            else:
                self.user_updated = user
        super(Classification2, self).save()

    def toJSON(self):
        item = model_to_dict(self, exclude=['user_creation', 'user_updated'])
        return item
    class Meta:
        verbose_name = 'Clasificación'
        verbose_name_plural = 'Clasificaciones'
        ordering = ['classify']