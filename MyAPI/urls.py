from django.urls import path, include
from . import views
from rest_framework import routers

#segundo ejemplo
# from MyAPI.views import Test

#nuevas vistas
from MyAPI.vistas.chapter.views import *
from MyAPI.vistas.dashboard.views import *
from MyAPI.vistas.classify.views import *
from MyAPI.vistas.tests.views import *
from MyAPI.vistas.position.views import *

router = routers.DefaultRouter()
router.register('MyAPI', views.ClasificacionesView)

app_name = 'myapi'
urlpatterns = [
    # path('form/', views.cxcontact, name = 'cxform'),
    # path('form/', views.myform, name='myform'),
    # path('api/', include(router.urls)),
    # path('status/', views.approvereject),

    # TEMPLATE ORIGINAL
    # path('', views.cxcontact2, name = 'cxform2'),

    # segundo ejemplo
    # path('test/', Test.as_view(), name = "test"),

    # prueba de template
    # path('', views.cxcontact2, name = 'main'),
    # path('', views.cxcontact2, name = 'main'),
    # path('main/clasificar', views.cxcontact3, name='clasificar'),

    # vistas basadas en funciones
    # path('app/chapter/list', chapter_list, name = 'chapter_list')

    # vistas basadas en clases
    path('chapter/list/', ChapterListView.as_view(), name = 'chapter_list'),
    path('chapter/create/', ChapterCreateView2.as_view(), name = 'chapter_create'),
    # path('app/chapter/list2/', chapter_list, name = 'chapter_list2'),
    path('chapter/edit/<int:pk>/', ChapterUpdateView2.as_view(), name= 'chapter_update'),
    path('chapter/delete/<int:pk>/', ChapterDeleteView2.as_view(), name= 'chapter_delete'),
    path('chapter/form/', ChapterFormView.as_view(), name= 'chapter_form'),
    #Home
    path('dashboard/', DashboardView.as_view(), name= 'dashboard'),

    # PROBAR CLASIFICADOR CON NUEVO TEMPLATE
    path('classification/list/', ClassificationListView.as_view(), name = 'classification_list'),
    path('classification/create/', ClassificationCreateView.as_view(), name = 'classification_create'),
    # path('main/clasificar2/', views.cxcontact, name='main'),
    path('clasificar/', views.cxcontact3, name='clasificar'),

    # test
    path('test/', TestView.as_view(), name='test'),

    # Position
    path('position/list/', PositionListView.as_view(), name='position_list'),

]
