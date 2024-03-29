from django.db import models
from django.contrib.auth.models import AbstractUser
from DjangoAPI.settings import MEDIA_URL, STATIC_URL
from django.forms import model_to_dict
from datetime import datetime

# Create your models here.
# Heredar los atributos de user y aumentar
class User(AbstractUser):
    image = models.ImageField(upload_to='users/%Y/%m/%d', null=True, blank=True)

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self, exclude=['password', 'groups', 'user_permissions', 'last_login', 'is_superuser',
                                            'is_active', 'is_staff'])
        if self.last_login:
            item['last_login'] = self.last_login.strftime('%Y-%m-%d')
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        return item

    # def save(self, *args, **kwargs):
        # if self.pk is None:
        #     self.set_password(self.password)
        # else:
        #     user = User.objects.get(pk=self.pk)
        #     if user.password != self.password:
        #         self.set_password(self.password)
        # super().save(*args, **kwargs)


