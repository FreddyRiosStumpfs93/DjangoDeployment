from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from .forms import ApprovalForm
from django.http import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from rest_framework.parsers import JSONParser
from .models import clasificacion
from .serializers import clasificacionSerializers
import json
import numpy as np
from sklearn.svm import SVC
from sklearn import preprocessing
import pandas as pd
import joblib

## librerias ejemplo 2
from rest_framework.views import APIView
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import joblib

# solucionar error CSRF verification failed. Request aborted.
from django.views.decorators.csrf import csrf_exempt

# Librerias para template
from django.views.generic import ListView, DetailView



class ClasificacionesView(viewsets.ModelViewSet):
    queryset = clasificacion.objects.all()
    serializer_class = clasificacionSerializers

# def ohevalue(df):
#     ohe_col = joblib.load('modelo_entrenado.pkl')
#     cat_columns = ['Descripcion', 'Material']
#     df_processed = pd.get_dummies(df, columns=cat_columns)
#     newdict = {}
#     for i in ohe_col:
#         if i in df_processed.columns:
#           newdict[i] = df_processed[i].values
#         else:
#             newdict[i] = 0
#     newdf = pd.DataFrame(newdict)
#     return newdf

def myform(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            myform = form.save(commit = False)
    else:
        form = MyForm()

# @api_view(["POST"])
# def approvereject(request):
def approvereject(unit):
    try:
        """
        TÉCNICAS DE MACHINE LEARNING
        SVM
        """
        clf = SVC()

        """
        CARGAR MODELO ENTRENADO DE MACHINE LEARNING
        X has 15705 features, but SVC is expecting 15714 features as input.
        investigar error
        """
        # Cargar modelo entrenado
        clf = joblib.load('modelo_entrenado.pkl')
        # Cargar TF-IDF entrenado
        tfidf = joblib.load('tfidf_entrenado.pkl')

        """
        PRUEBA DEL CLASIFICADOR
        """
        # PROBANDO DESDE API
        # mydata = request.data
        # mydata2 = list(mydata.values())
        # mydata3 = [mydata2[0]+" "+mydata2[1]]
        # print(mydata3)

        # PRUEBA DESDE FORMULARIO WEB
        X = tfidf.transform(unit)
        y_pred = clf.predict(X)
        print(y_pred)
        # return JsonResponse({'Your Status is ': str(y_pred)})
        return ({'La partida sugerida es: ': str(y_pred)})


    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

def cxcontact(request):
    if request.method=='POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            descripcion = form.cleaned_data['descripcion']
            material = form.cleaned_data['material']
            # myDict = (request.POST).dict()
            # df = pd.DataFrame(myDict, index=[0])

            # PRUEBA DESDE FORMULARIO
            # mydata = request.POST
            # print(mydata)
            mydata = [descripcion+" de "+material]
            # mydata2 = list(mydata.values())
            # mydata3 = [mydata2[0]+" "+mydata2[1]]
            print(mydata)

#             print(approvereject(ohevalue(df)))
            print(approvereject(mydata))
            answer = approvereject(mydata)
            messages.success(request, 'Application Status: {}'.format(answer))
            # messages.success(request, answer)

    form = ApprovalForm()
    return render(request, 'myform/cxform.html', {'form':form})

@csrf_exempt
def cxcontact2(request):
    if request.method=='POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            descripcion = form.cleaned_data['descripcion']
            material = form.cleaned_data['material']
            # myDict = (request.POST).dict()
            # df = pd.DataFrame(myDict, index=[0])

            # PRUEBA DESDE FORMULARIO
            # mydata = request.POST
            # print(mydata)

            mydata = [descripcion+" de "+material]
            print(mydata)
            cont = len(mydata.__str__())
            if cont<=25:
                messages.success(request, 'No se puede realizar la búsqueda, favor ingrese más información de la mercadería')
            else:
                print(mydata)
                print(approvereject(mydata))
                answer = approvereject(mydata)
                messages.success(request, 'Application Status: {}'.format(answer))

    form = ApprovalForm()
    # return render(request, 'myform/cxform.html', {'form':form})

    # prueba template
    return render(request, 'myform/home.html', {'form':form})

# @csrf_exempt probando si funciona en template comentando esta linea
def cxcontact3(request):
    if request.method=='POST':
        form = ApprovalForm(request.POST)
        if form.is_valid():
            descripcion = form.cleaned_data['descripcion']
            material = form.cleaned_data['material']

            mydata = [descripcion+" de "+material]
            print('Valor de mydata: '+ str(mydata))
            cont = len(mydata.__str__())
            if cont<=25:
                messages.success(request, 'No se puede realizar la búsqueda, favor ingrese más información de la mercadería')
            else:
                print(mydata)
                print(approvereject(mydata))
                answer = approvereject(mydata)
                messages.success(request, 'Application Status: {}'.format(answer))

    form = ApprovalForm()
    # return render(request, 'app/app_body.html', {'form':form})
    # return render(request, 'classification/classify.html', {'form':form})
    return render(request, 'classification/classify.html', {'form':form})


"""
Segundo ejemplo
"""
class Test(APIView):
    def get(self, response):
        return JsonResponse({"key": "Hello world"})

    def post(self, request):
        descripcion = request.data['descripcion']
        print(os.getcwd())
        print("Hi")
        # Cargar modelo entrenado
        clf = joblib.load('modelo_entrenado.pkl')
        # Cargar TF-IDF entrenado
        tfidf = joblib.load('tfidf_entrenado.pkl')

        predict = clf.predict(tfidf.transform([descripcion]))
        predicted_class = str(predict)
        return JsonResponse({'Prediccion':predicted_class})

class FileHandling(APIView):
    def post(self, request):
        pdf_file = request.FILES['pdf_file']
        fs = FileSystemStorage
        path_image_1 = fs.save(os.path.join(settings.BASE_DIR, "learning", pdf_file.name), pdf_file)
        return JsonResponse({"status":"file saved"})

class vistaClasificar(DetailView):
    model = clasificacion
    template_name = 'cxform.html'

class principal(DetailView):
    template_name = 'index.html'

def myfirstview(request):
    return render (request, 'myform/home.html')