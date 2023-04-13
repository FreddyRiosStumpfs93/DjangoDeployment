# Original
# from django.test import TestCase

#prueba videos viejos
import pandas as pd
from DjangoAPI.wsgi import *
from MyAPI.models import Chapter, Position
import random

# LOAD DATA
import csv

# Create your tests here.

# # Listar
# query = Chapter.objects.all()
# print(query)

# obj1 = Chapter.objects.filter(description__contains = 'jug') # Diferencia mayúscula y minúsculas
# obj2 = Chapter.objects.filter(description__icontains = 'jug') # No diferencia mayúscula y minúscula
# print (obj1)
# print (obj2)

# Inserción
# ch = Chapter()
# ch.chapter = '4402'
# ch.description = 'carteras'
# ch.save()

# Edición
# ch = Chapter.objects.get(pk=1)
# ch.description = 'JUGUETES DE PLASTICO'
# ch.save()

# DELETE ALL DATA FROM CHAPTER
# Chapter.objects().all().delete()

# ch = Chapter.objects.get(pk=3)
# ch.delete()
# ALTER SEQUENCE myapi_chapter_id_seq RESTART WITH 1;

# for i in range(1,6000):
#     name = ''.join(random.choices(letters, k=5))
#     while Category.objects.filter(name=name).exists():
#         name = ''.join(random.choices(letters, k=5))
#     Chapter(name=name).save()
#     print('Guardado registro{}'.format(i))

    # df = pd.read_csv("./testing_data/"+file, delimiter=',', encoding='cp1252', low_memory=False, error_bad_lines=False,
    #                  quoting=csv.QUOTE_MINIMAL, warn_bad_lines=False)

# ch = Chapter()
# ch.chapter = '4402'
# ch.description = 'carteras'
# ch.save()

# # LOAD CHAPTERS FROM A CSV FILE
# archivo = open('./chapters/df_chapters_3.csv')
# filas = csv.reader(archivo, delimiter=",")
# lista = list(filas)
# # del (lista[0])
# for column in lista:
#     ch = Chapter()
#     chapter=str(column[0])
#     # print(chapter)
#     chapter2 = chapter[0:11]
#     # print(chapter2)
#     ch.chapter=chapter2
#     ch.description=column[0]
#     ch.save()
#     print('Guardado registro{}'.format(ch))

# LOAD POSITIONS FROM A CSV FILE
archivo = open('./positions/df_positions_2.csv')
# df_filas = pd.read_csv("./positions/df_positions_2.csv", delimiter=',', encoding='utf-8',
#                                 low_memory=False, on_bad_lines='skip', quoting=csv.QUOTE_MINIMAL)
# nombre_columnas = df_filas.columns.values
# print(nombre_columnas)
filas = csv.reader(archivo, delimiter=',')
lista = list(filas)
for column in lista:
    p = Position()
    # number=str(column[1])
    # print(number)
    # description = str(column[2])
    # print(description)

    p.position = column[1]
    p.description= column[2]
    p.save()
    print('Guardado registro{}'.format(p))