from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from MyAPI.forms import PositionForm
from MyAPI.models import Position

# VISTAS BASADAS EN CLASES
class PositionListView(ListView):
    model = Position
    template_name = 'position/list.html'

    # editar el dato de consulta
    # def get_queryset(self):
    #     return Chapter.objects.filter(name__startswith='01')

    # los decoradores añaden funcionalidades a otra función.
    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    # el método dispatch se encarga de redireccionar las peticiones get y post
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            # load list with ajax and datatable
            action =request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Position.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'

            # Cargar lista iterando
            # data = Chapter.objects.get(pk=request.POST['id']).toJSON()

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de posiciones arancelarias'
        context['create_url'] = '' # reverse_lazy('myapi:position_create')
        context['list_url'] = reverse_lazy('myapi:position_list')
        context['entity'] = 'Posiciones Arancelarias'
        return context
    # ajax es una tecnología de tipo asíncrono (no es necesario recargar toda la página para obtener una respuesta)