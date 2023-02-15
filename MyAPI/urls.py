
from django.urls import path, include
from . import views
from rest_framework import routers

#segundo ejemplo
from MyAPI.views import Test


router = routers.DefaultRouter()
router.register('MyAPI', views.ClasificacionesView)
urlpatterns = [
    # path('form/', views.cxcontact, name = 'cxform'),
    # path('form/', views.myform, name='myform'),
    # path('api/', include(router.urls)),
    # path('status/', views.approvereject),
    path('', views.cxcontact2, name = 'cxform2'),

    # segundo ejemplo
    # path('test/', Test.as_view(), name = "test"),

]
