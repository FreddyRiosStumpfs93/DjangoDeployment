from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from MyAPI.forms import ChapterForm
from MyAPI.models import Chapter


# # VISTAS BASADAS EN FUNCIONES
# def chapter_list(request):
#     data = {
#         'title': 'Listado de capitulos',
#         'chapters': Chapter.objects.all()
#     }
#     return render(request, 'chapter/list.html', data)

# VISTAS BASADAS EN CLASES
class ChapterListView(ListView):
    model = Chapter
    template_name = 'chapter/list.html'

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
                for i in Chapter.objects.all():
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
        context['title'] = 'Listado de capítulos'
        context['create_url'] = reverse_lazy('myapi:chapter_create')
        context['list_url'] = reverse_lazy('myapi:chapter_list')
        context['entity'] = 'Capitulos'
        return context
    # ajax es una tecnología de tipo asíncrono (no es necesario recargar toda la página para obtener una respuesta)

class ChapterCreateView(CreateView):
    model = Chapter
    form_class = ChapterForm
    template_name = 'chapter/create.html'
    success_url = reverse_lazy('myapi:chapter_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    """
    Ejemplo de como actúa el método post al hacer submit 
    """
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna accion'
            # data = Chapter.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    #     print(request.POST)
    #     form = ChapterForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect(self.success_url)
    #     self.object = None
    #     context = self.get_context_data(**kwargs)
    #     context['form'] = form
    #     return render(request, self.template_name, context)
    #     print(form.errors)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear capítulo'
        context['entity'] = 'Capitulos'
        context['list_url'] = reverse_lazy('myapi:chapter_list')
        context['action'] = 'add'
        return context

class ChapterUpdateView(UpdateView):
    model = Chapter
    form_class = ChapterForm
    template_name = 'chapter/create.html'
    success_url = reverse_lazy('myapi:chapter_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna accion'
            # data = Chapter.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar capítulo'
        context['entity'] = 'Capitulos'
        context['list_url'] = reverse_lazy('myapi:chapter_list')
        context['action'] = 'edit'
        return context

    # los decoradores añaden funcionalidades a otra función.

class ChapterDeleteView(DeleteView):
    model = Chapter
    template_name = 'chapter/delete.html'
    success_url = reverse_lazy('myapi:chapter_list')

    # @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs): # sobreescribiendo método post
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar capítulo'
        context['entity'] = 'Capitulos'
        context['list_url'] = reverse_lazy('myapi:chapter_list')
        return context

class ChapterFormView(FormView):
    form_class = ChapterForm
    template_name = 'chapter/create.html'
    success_url = reverse_lazy('myapi:chapter_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Form | Chapter'
        context['entity'] = 'Capitulos'
        context['list_url'] = reverse_lazy('myapi:chapter_list')
        context['action'] = 'add'
        return context

class ChapterCreateView2(CreateView):
    model = Chapter
    form_class = ChapterForm
    template_name = 'chapter/create.html'
    success_url = reverse_lazy('myapi:chapter_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()

            elif action == 'autocomplete':
                data = []
                for i in Chapter.objects.filter(name__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['value'] = i.name
                    data.append(item)
            else:
                data['error'] = 'No ha ingresado ninguna accion'
            # data = Chapter.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear capítulo'
        context['entity'] = 'Capitulos'
        context['list_url'] = reverse_lazy('myapi:chapter_list')
        context['action'] = 'add'
        return context

class ChapterUpdateView2(UpdateView):
    model = Chapter
    form_class = ChapterForm
    template_name = 'chapter/create.html'
    success_url = reverse_lazy('myapi:chapter_list')

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado ninguna accion'
            # data = Chapter.objects.get(pk=request.POST['id']).toJSON()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar capítulo'
        context['entity'] = 'Capitulos'
        context['list_url'] = reverse_lazy('myapi:chapter_list')
        context['action'] = 'edit'
        return context

class ChapterDeleteView2(DeleteView):
    model = Chapter
    template_name = 'chapter/delete.html'
    success_url = reverse_lazy('myapi:chapter_list')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs): # sobreescribiendo método post
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar capítulo'
        context['entity'] = 'Capitulos'
        context['list_url'] = reverse_lazy('myapi:chapter_list')
        return context
