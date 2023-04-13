from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from MyAPI.forms import TestForm
from MyAPI.models import Chapter

# MACHINE LEARNING
from sklearn.svm import SVC
import joblib
from rest_framework.response import Response
from rest_framework import status

# LOAD DATA
import csv

class TestView(TemplateView):
    template_name = 'app/app_test.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}

        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = [{'id': '', 'text': '------------'}]
                for i in Product.objects.filter(cat_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name, 'data': i.cat.toJSON()})
            elif action == 'autocomplete':
                data = []
                for i in Chapter.objects.filter(chapter__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.chapter
                    data.append(item)
            elif action == 'autocomplete2':
                data = []
                description = [request.POST['term']]
                # description = description.toJSON
                print(description)
                answer = machine_learning(description)
                print(answer)
                data.append(answer)
                print(data)
            elif action == 'search_classification':
                pass
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            print(str(e))
            # data['error'] = str(e)
        return JsonResponse(data, safe=False)

    # enviar valores adicionales al context data
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Aninados | Django'
        context['form'] = TestForm()
        return context

def machine_learning(unit):
    try:
        clf = SVC()
        clf = joblib.load('modelo_entrenado.pkl')
        tfidf = joblib.load('tfidf_entrenado.pkl')

        X = tfidf.transform(unit)
        y_pred = clf.predict(X)
        print(y_pred)
        # return({'La partida sugerida es: ': str(y_pred)})
        return(str(y_pred))

    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)

