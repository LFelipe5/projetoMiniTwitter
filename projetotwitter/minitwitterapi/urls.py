from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>/', PostagemListar.as_view()),
    path('', PostagemListar.as_view()),
    path('criarPostagem', PostagemCriar.as_view()),
]