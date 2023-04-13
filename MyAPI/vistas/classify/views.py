import joblib
from django.views.generic import CreateView, ListView
from MyAPI.models import Classification, Chapter, Position
from MyAPI.forms import ClassificationForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
#Machine learning
from sklearn.svm import SVC
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages

class ClassificationCreateView(CreateView):
    model = Classification
    form_class = ClassificationForm
    template_name = 'classification/classify.html'
    success_url = reverse_lazy('myapi:classification_list')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                # # intento de guardar clasificación arancelaria
                # classification = request.POST['classification']

                form = self.get_form()
                if form.is_valid():
                    description = form.cleaned_data['description']
                    material = form.cleaned_data['material']
                    mydata = [description+" de "+material]
                    # print('Valor de mydata: '+ str(mydata))
                    # print(machine_learning(mydata))

                    # volver a activar en caso que algo no funcione jeje
                    # answer = machine_learning(mydata)

                    # form.forms['classify'] = str(answer)
                    # form['classify'] = str(answer)
                    # valor_viejo = form.fields['classify']
                    # print(valor_viejo)

                    #probando
                    # form = ClassificationForm(initial={'classify': 9503,})

                    # messages.success(request, 'Application Status: {}'.format(answer))
                    # messages.success(request, str(answer))
                    data = form.save()

            elif action == 'search_classify':
                data = []
                description = request.POST['desc']
                material = request.POST['mat']
                mydata = [description + " de " + material]
                print(mydata)
                answer = machine_learning(mydata)
                print(answer)
                # data.append(str(answer))
                data.append({'answer': answer})
                chapter = str(answer)
                chapter2 = chapter[2:4]
                position = chapter[2:17]
                print(chapter2)
                print(position)
                # for i in Chapter.objects.filter(chapter__contains = chapter2):
                #     data.append({'Capitulo': i.chapter, 'Descripción': i.description})

                for i in Position.objects.filter(position__contains = position):
                    data.append({'Posición': i.position, 'Descripción': i.description})
                print(data)
                # messages.success(request, str(answer))
                # respuesta = str(data.get("answer")) + str(data.get("chapter")) + str(data.get("description"))
                messages.success(request, data)


                # print(data)
                # messages.success(request, str(answer))
                # form = self.get_form()
                # if form.is_valid():
                #     messages.success(request, str(answer))
                #     data = form.save()

            elif action == 'autocomplete2':
                data = []
                description = [request.POST['term']]
                # description = description.toJSON
                print(description)
                answer = machine_learning(description)
                print(answer)
                data.append(answer)
                print(data)

            else:
                data['error'] = 'No ha ingresado ninguna accion'
            # data = Chapter.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            print(str(e))
            # data['error'] = str(e)
        return JsonResponse(data, safe=False) # Cuando trabajamos con colección de elementos safe debe ser falso.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Clasificar mercadería'
        context['entity'] = 'Clasificar'
        # context['list_url'] = reverse_lazy('myapi:classification_list')
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ClassificationListView(ListView):
    model = Classification
    template_name = 'classification/list.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            data = Classification.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clasificaciones Arancelarias'
        context['create_url'] = reverse_lazy('myapi:classification_create')
        context['list_url'] = reverse_lazy('myapi:classification_list')
        context['entity'] = 'Clasificaciones Arancelarias'
        return context

@csrf_exempt
def machine_learning(unit):
    try:
        clf = SVC()
        # clf = joblib.load('modelo_entrenado.pkl')
        # tfidf = joblib.load('tfidf_entrenado.pkl')

        #Testing data
        # clf = joblib.load('trained_model_testing_data.pkl')
        # tfidf = joblib.load('trained_tfidf_testing_data.pkl')

        #Trained model six months data
        clf = joblib.load('trained_model_six_months_data.pkl')
        tfidf = joblib.load('trained_tfidf_six_months_data.pkl')

        X = tfidf.transform(unit)
        y_pred = clf.predict(X)
        # print(y_pred)
        # return({'La partida sugerida es: ': str(y_pred)})
        return(str(y_pred))

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)
